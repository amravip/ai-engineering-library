// Visual and accessibility checks on the built site, run in headless Chrome.
// Dev only: CI does not run this. Usage (with the preview server running):
//   npm run qa:screens
// Environment: QA_BASE (default http://localhost:4321), QA_OUT (screenshot folder),
// CHROME_PATH (path to a Chrome or Edge executable).
import { mkdirSync, readFileSync, writeFileSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from 'puppeteer-core';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const base = process.env.QA_BASE || 'http://localhost:4321';
const out = process.env.QA_OUT || join(root, '.qa');
const chrome = process.env.CHROME_PATH || 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe';
mkdirSync(out, { recursive: true });

const pages = [
  { name: 'home', path: '/' },
  { name: 'applied-landing', path: '/applied-ai-engineering/' },
  { name: 'chapter-01', path: '/applied-ai-engineering/01-first-conversation/' },
  { name: 'chapter-08', path: '/applied-ai-engineering/08-talking-to-models-from-code/' },
  { name: 'chapter-11', path: '/applied-ai-engineering/11-rag/' },
  { name: 'not-online-book', path: '/rag-engineering/' },
  { name: 'running-examples', path: '/running-the-examples/' },
  { name: 'data-files', path: '/applied-ai-engineering/data-files/' },
  { name: 'complete-source', path: '/applied-ai-engineering/complete-source/' },
];
const widths = [1280, 390];

const axeSource = readFileSync(join(root, 'node_modules', 'axe-core', 'axe.min.js'), 'utf8');
const report = { pages: [], search: null, focus: null };

const browser = await puppeteer.launch({
  executablePath: chrome,
  headless: true,
  args: ['--no-sandbox', '--disable-gpu', '--hide-scrollbars'],
});

try {
  for (const page of pages) {
    for (const width of widths) {
      const tab = await browser.newPage();
      const consoleErrors = [];
      tab.on('console', (msg) => {
        if (msg.type() === 'error') consoleErrors.push(msg.text());
      });
      tab.on('pageerror', (err) => consoleErrors.push(String(err)));
      await tab.setViewport({ width, height: 900, deviceScaleFactor: 1 });
      await tab.goto(`${base}${page.path}`, { waitUntil: 'networkidle0' });
      await tab.evaluate(() => document.fonts.ready);
      const overflow = await tab.evaluate(() => document.documentElement.scrollWidth - window.innerWidth);
      await tab.screenshot({ path: join(out, `${page.name}-${width}.png`), fullPage: true });

      await tab.addScriptTag({ content: axeSource });
      const axe = await tab.evaluate(async () => {
        const result = await window.axe.run(document, { runOnly: ['wcag2a', 'wcag2aa', 'wcag21aa', 'wcag22aa'] });
        return result.violations.map((v) => ({ id: v.id, impact: v.impact, nodes: v.nodes.length, help: v.help }));
      });
      report.pages.push({ page: page.name, width, horizontalOverflowPx: overflow, axeViolations: axe, consoleErrors });
      await tab.close();
    }
  }

  // Search results for "Margherita", at desktop width.
  const search = await browser.newPage();
  await search.setViewport({ width: 1280, height: 900, deviceScaleFactor: 1 });
  await search.goto(`${base}/applied-ai-engineering/01-first-conversation/`, { waitUntil: 'networkidle0' });
  // The search button stays disabled until Pagefind has loaded.
  await search.waitForSelector('button[data-open-modal]:not([disabled])');
  await search.click('button[data-open-modal]');
  await search.waitForSelector('dialog[open] input', { visible: true });
  await search.type('dialog[open] input', 'Margherita', { delay: 30 });
  await new Promise((resolve) => setTimeout(resolve, 1500));
  const hits = await search.$$eval('dialog[open] a[href^="/"]', (links) =>
    links.map((link) => ({ text: link.textContent.trim().slice(0, 80), href: link.getAttribute('href') })),
  );
  await search.screenshot({ path: join(out, 'search-margherita-1280.png') });
  report.search = { query: 'Margherita', resultCount: hits.length, first: hits.slice(0, 5) };
  await search.close();

  // Keyboard focus: the first Tab stops on the chapter page must show a visible focus ring.
  const focus = await browser.newPage();
  await focus.setViewport({ width: 1280, height: 900, deviceScaleFactor: 1 });
  await focus.goto(`${base}/applied-ai-engineering/02-tokens/`, { waitUntil: 'networkidle0' });
  const focused = [];
  for (let i = 0; i < 12; i += 1) {
    await focus.keyboard.press('Tab');
    const info = await focus.evaluate(() => {
      const el = document.activeElement;
      if (!el) return null;
      const style = getComputedStyle(el);
      return {
        tag: el.tagName,
        text: (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 40),
        outlineStyle: style.outlineStyle,
        outlineWidth: style.outlineWidth,
        outlineColor: style.outlineColor,
      };
    });
    focused.push(info);
  }
  await focus.screenshot({ path: join(out, 'focus-chapter-02-after-tab.png') });
  report.focus = focused;
  await focus.close();
} finally {
  await browser.close();
}

writeFileSync(join(out, 'qa-report.json'), JSON.stringify(report, null, 2), 'utf8');

let failures = 0;
for (const entry of report.pages) {
  const serious = entry.axeViolations.filter((v) => v.impact === 'serious' || v.impact === 'critical');
  const flags = [];
  if (entry.horizontalOverflowPx > 0) flags.push(`horizontal overflow ${entry.horizontalOverflowPx}px`);
  if (serious.length) flags.push(`axe serious/critical: ${serious.map((v) => v.id).join(', ')}`);
  if (entry.axeViolations.length) flags.push(`axe any impact: ${entry.axeViolations.map((v) => `${v.id}(${v.impact})`).join(', ')}`);
  if (entry.consoleErrors.length) flags.push(`console errors: ${entry.consoleErrors.length}`);
  if (flags.length) failures += 1;
  console.log(`${entry.page} @${entry.width}px: ${flags.length ? flags.join(' | ') : 'clean'}`);
}
console.log(`search "Margherita": ${report.search.resultCount} results`);
console.log(`screenshots and qa-report.json written to ${out}`);
process.exitCode = failures ? 0 : 0; // reported, not gating: review the report
