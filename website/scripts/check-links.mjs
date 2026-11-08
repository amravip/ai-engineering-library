// Checks every internal link, asset reference and #fragment in the built site.
// Standard library only. Run after `npm run build`: node scripts/check-links.mjs
import { readFileSync, readdirSync, statSync, existsSync } from 'node:fs';
import { join, dirname, relative, sep } from 'node:path';
import { fileURLToPath } from 'node:url';

const root = join(dirname(fileURLToPath(import.meta.url)), '..');
const dist = join(root, 'dist');
if (!existsSync(dist)) {
  console.error('FAIL: dist/ not found. Run npm run build first.');
  process.exit(1);
}

function htmlFiles(dir) {
  const files = [];
  for (const name of readdirSync(dir)) {
    const path = join(dir, name);
    if (statSync(path).isDirectory()) files.push(...htmlFiles(path));
    else if (name.endsWith('.html')) files.push(path);
  }
  return files;
}

// Map a site path such as /a/b/ or /a/b.css to a file in dist/.
function resolveTarget(urlPath) {
  const clean = decodeURIComponent(urlPath);
  const candidates = clean.endsWith('/')
    ? [join(dist, clean, 'index.html')]
    : [join(dist, clean), join(dist, clean, 'index.html'), join(dist, `${clean}.html`)];
  return candidates.find((candidate) => existsSync(candidate) && statSync(candidate).isFile()) ?? null;
}

const pages = htmlFiles(dist);
const idsByFile = new Map(
  pages.map((file) => {
    const text = readFileSync(file, 'utf8');
    const ids = new Set([...text.matchAll(/\sid="([^"]+)"/g)].map((m) => m[1]));
    for (const m of text.matchAll(/\sname="([^"]+)"/g)) ids.add(m[1]);
    return [file, ids];
  }),
);

const problems = [];
let checked = 0;
let external = 0;

for (const file of pages) {
  const text = readFileSync(file, 'utf8');
  const refs = [...text.matchAll(/\s(?:href|src)="([^"]*)"/g)].map((m) => m[1]);
  for (const raw of refs) {
    const value = raw.replace(/&amp;/g, '&');
    if (/^(mailto:|tel:|data:|javascript:)/.test(value)) continue;
    if (/^https?:\/\//.test(value) || value.startsWith('//')) {
      external += 1;
      continue;
    }
    const [pathPart, fragment] = value.split('#', 2);
    const pathOnly = pathPart.split('?')[0];
    let targetFile = file;
    if (pathOnly !== '') {
      if (!pathOnly.startsWith('/')) {
        // relative link: resolve against the page's location in dist
        const base = '/' + relative(dist, dirname(file)).split(sep).join('/');
        const joined = new URL(pathOnly, `http://site${base === '/.' ? '/' : base + '/'}`).pathname;
        targetFile = resolveTarget(joined);
      } else {
        targetFile = resolveTarget(pathOnly);
      }
      checked += 1;
      if (!targetFile) {
        problems.push(`${relative(dist, file)}: broken link ${raw}`);
        continue;
      }
    }
    if (fragment && targetFile.endsWith('.html')) {
      const ids = idsByFile.get(targetFile);
      if (ids && !ids.has(decodeURIComponent(fragment))) {
        problems.push(`${relative(dist, file)}: missing anchor #${fragment} in ${relative(dist, targetFile)}`);
      }
    }
  }
}

for (const problem of problems) console.log(`FAIL: ${problem}`);
console.log(`Checked ${checked} internal references in ${pages.length} pages; ${external} external links not fetched.`);
if (problems.length) {
  console.log(`${problems.length} broken internal reference(s).`);
  process.exit(1);
}
console.log('Internal links and anchors: PASS');
