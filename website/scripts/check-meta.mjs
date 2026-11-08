// Checks page metadata, heading order, image alt text, the sitemap and the search index.
// Compares each book landing page's description with books.yaml. Run after npm run build.
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, dirname, relative } from 'node:path';
import { fileURLToPath } from 'node:url';
import yaml from 'js-yaml';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
const problems = [];

function htmlFiles(dir) {
  const files = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) {
      if (name === 'pagefind' || name === '.prerender') continue;
      files.push(...htmlFiles(path));
    } else if (name.endsWith('.html')) files.push(path);
  }
  return files;
}

const decode = (s) => s.replace(/&amp;/g, '&').replace(/&quot;/g, '"').replace(/&#39;/g, "'").replace(/&lt;/g, '<').replace(/&gt;/g, '>');

const pages = htmlFiles(dist);
for (const file of pages) {
  const name = relative(dist, file);
  const html = readFileSync(file, 'utf8');
  const title = html.match(/<title>([^<]*)<\/title>/);
  if (!title || !title[1].trim()) problems.push(`${name}: empty or missing <title>`);
  const description = html.match(/<meta name="description" content="([^"]*)"/);
  if (!description || !decode(description[1]).trim()) problems.push(`${name}: empty or missing meta description`);

  const headings = [...html.matchAll(/<h([1-6])[\s>]/g)].map((m) => Number(m[1]));
  const h1Count = headings.filter((level) => level === 1).length;
  if (h1Count !== 1) problems.push(`${name}: expected one h1, found ${h1Count}`);
  for (let i = 1; i < headings.length; i += 1) {
    if (headings[i] > headings[i - 1] + 1) {
      problems.push(`${name}: heading level jumps from h${headings[i - 1]} to h${headings[i]}`);
      break;
    }
  }
  for (const img of html.matchAll(/<img\b[^>]*>/g)) {
    if (!/\salt[\s=>\/]/.test(img[0])) problems.push(`${name}: image without alt attribute: ${img[0].slice(0, 80)}`);
  }
}

// Landing pages must carry the same description as books.yaml.
const { books } = yaml.load(readFileSync(join(root, 'books.yaml'), 'utf8'));
for (const book of books) {
  const source = join(root, 'src', 'content', 'docs', book.slug, 'index.mdx');
  const text = readFileSync(source, 'utf8');
  const match = text.match(/^description: (".*")$/m);
  const expected = book.description.replace(/\s+/g, ' ').trim();
  if (!match || JSON.parse(match[1]) !== expected) {
    problems.push(`src/content/docs/${book.slug}/index.mdx: description differs from books.yaml`);
  }
}

// Sitemap and search index.
const sitemapIndex = join(dist, 'sitemap-index.xml');
if (!existsSync(sitemapIndex)) {
  problems.push('sitemap-index.xml missing');
} else {
  const urls = [...readFileSync(join(dist, 'sitemap-0.xml'), 'utf8').matchAll(/<loc>([^<]+)<\/loc>/g)];
  if (urls.length < pages.length - 1) problems.push(`sitemap lists ${urls.length} URLs for ${pages.length} pages`);
  console.log(`Sitemap: sitemap-index.xml and sitemap-0.xml list ${urls.length} URLs.`);
}
if (!existsSync(join(dist, 'pagefind', 'pagefind.js'))) problems.push('pagefind index missing');

for (const problem of problems) console.log(`FAIL: ${problem}`);
console.log(`Checked metadata, headings and alt text on ${pages.length} pages.`);
if (problems.length) {
  console.log(`${problems.length} problem(s) found.`);
  process.exit(1);
}
console.log('Page metadata, heading order, alt text, sitemap and search index: PASS');
