// Checks the deployed site: status codes, no leaked book pages, licence footer,
// canonical address, and screenshots at desktop and phone widths.
// Usage: node scripts/check-live.mjs [base]   (default https://ai-engineering-library.pages.dev)
import puppeteer from 'puppeteer-core';
import { mkdirSync } from 'node:fs';
import { join, dirname } from 'node:path';
import { fileURLToPath } from 'node:url';

const base = (process.argv[2] || 'https://ai-engineering-library.pages.dev').replace(/\/$/, '');
const out = join(dirname(fileURLToPath(import.meta.url)), '..', '.qa', 'live');
mkdirSync(out, { recursive: true });
const chrome = process.env.CHROME_PATH || 'C:/Program Files/Google/Chrome/Application/chrome.exe';
let failures = 0;
const fail = (msg) => { failures++; console.log('FAIL ' + msg); };

const shouldExist = ['/', '/applied-ai-engineering/', '/rag-engineering/', '/running-the-examples/',
  '/sitemap-index.xml', '/pagefind/pagefind.js', '/fonts/Inter.woff2', '/cards/llmops.svg'];
// Private book text must not be reachable.
const mustNotExist = ['/applied-ai-engineering/01-first-conversation/', '/applied-ai-engineering/complete-source/',
  '/applied-ai-engineering/data-files/', '/books/applied-ai-engineering/cover-1600x2560.png'];

for (const path of shouldExist) {
  const r = await fetch(base + path);
  r.status === 200 ? console.log(`200 ${path}`) : fail(`${path} returned ${r.status}`);
}
for (const path of mustNotExist) {
  const r = await fetch(base + path);
  const body = await r.text();
  // Cloudflare Pages serves 404.html with status 404 for unknown paths.
  if (r.status === 200 && !/404/.test(body.slice(0, 3000))) fail(`${path} is reachable (${r.status})`);
  else console.log(`${r.status} ${path} (not public, as intended)`);
}

const browser = await puppeteer.launch({ executablePath: chrome, headless: true });
for (const [name, path] of [['home', '/'], ['applied', '/applied-ai-engineering/'], ['rag', '/rag-engineering/']]) {
  for (const width of [1280, 390]) {
    const tab = await browser.newPage();
    const errors = [];
    tab.on('pageerror', (e) => errors.push(e.message));
    tab.on('requestfailed', (r) => errors.push('request failed ' + r.url()));
    await tab.setViewport({ width, height: 900 });
    await tab.goto(base + path, { waitUntil: 'networkidle0' });
    const info = await tab.evaluate(() => ({
      canonical: document.querySelector('link[rel=canonical]')?.href,
      licence: !!document.querySelector('.site-licence'),
      fonts: [...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family),
      overflow: document.documentElement.scrollWidth > window.innerWidth + 1,
    }));
    if (!info.canonical?.startsWith('https://ai-engineering-library.pages.dev')) fail(`${path} canonical ${info.canonical}`);
    if (!info.licence) fail(`${path} has no licence footer`);
    if (info.overflow) fail(`${path} scrolls sideways at ${width}px`);
    if (errors.length) fail(`${path} @${width}: ${errors.join('; ')}`);
    await tab.screenshot({ path: join(out, `${name}-${width}.png`), fullPage: true });
    console.log(`${path} @${width}px: fonts loaded ${[...new Set(info.fonts)].join(', ') || 'none yet'}`);
    await tab.close();
  }
}
await browser.close();
console.log(failures ? `Live check: ${failures} failure(s)` : 'Live check: PASS');
process.exit(failures ? 1 : 0);
