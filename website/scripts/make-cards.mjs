// Generates one light, typographic card image per book in public/cards/.
// These are not book covers. Each card shows the series name, the volume number,
// the title and the project, in the palette of spec section 26. Run with
// `node scripts/make-cards.mjs` after changing books.yaml; the SVGs are committed.
import { readFileSync, writeFileSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';
import yaml from 'js-yaml';

const here = dirname(fileURLToPath(import.meta.url));
const root = join(here, '..');
const { books, series } = yaml.load(readFileSync(join(root, 'books.yaml'), 'utf8'));

// Palette taken from the Applied AI Engineering cover (cover/source/build_covers.py).
const PAPER = '#FBF9F4';
const RULE = '#CDC6B5';
const INK = '#1F2A37';
const MUTED = '#6B6559';
const BLUE = '#2F5D8C';
const PALE_BLUE = '#DCE7F0';

const SANS = "Inter, 'Helvetica Neue', Arial, sans-serif";

function escapeXml(text) {
  return text.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

// Greedy word wrap. The width is an approximate character count for the font size.
function wrap(text, maxChars) {
  const lines = [];
  let line = '';
  for (const word of text.split(' ')) {
    const candidate = line ? `${line} ${word}` : word;
    if (candidate.length > maxChars && line) {
      lines.push(line);
      line = word;
    } else {
      line = candidate;
    }
  }
  if (line) lines.push(line);
  return lines;
}

function card(book) {
  const titleLines = wrap(book.title, 15);
  const projectLines = wrap(book.project, 30);
  const titleY = 236;
  const titleBlock = titleLines
    .map((line, i) => `<text x="44" y="${titleY + i * 46}" font-size="40" font-weight="600" fill="${INK}">${escapeXml(line)}</text>`)
    .join('\n  ');
  // Grow the project block upwards so a two-line project never meets the author line.
  const projectY = 568 - (projectLines.length - 1) * 26;
  const projectBlock = projectLines
    .map((line, i) => `<text x="44" y="${projectY + i * 26}" font-size="19" fill="${INK}">${escapeXml(line)}</text>`)
    .join('\n  ');
  const projectLabelY = projectY - 30;
  return `<svg xmlns="http://www.w3.org/2000/svg" width="400" height="640" viewBox="0 0 400 640" role="img" aria-hidden="true" focusable="false">
  <rect width="400" height="640" fill="${PAPER}"/>
  <rect x="20" y="20" width="360" height="600" rx="4" fill="none" stroke="${RULE}" stroke-width="2"/>
  <text x="44" y="70" font-family="${SANS}" font-size="12" font-weight="600" letter-spacing="2.4" fill="${MUTED}">${escapeXml(series.toUpperCase())}</text>
  <text x="44" y="104" font-family="${SANS}" font-size="14" font-weight="700" letter-spacing="1.6" fill="${BLUE}">VOLUME ${book.number}</text>
  <rect x="44" y="124" width="312" height="2" fill="${PALE_BLUE}"/>
  <g font-family="${SANS}">
  ${titleBlock}
  </g>
  <rect x="44" y="${projectLabelY - 40}" width="312" height="2" fill="${PALE_BLUE}"/>
  <text x="44" y="${projectLabelY}" font-family="${SANS}" font-size="12" font-weight="600" letter-spacing="2" fill="${MUTED}">PROJECT</text>
  <g font-family="${SANS}">
  ${projectBlock}
  </g>
  <text x="44" y="604" font-family="${SANS}" font-size="14" fill="${MUTED}">Ravi Pal</text>
</svg>
`;
}

mkdirSync(join(root, 'public', 'cards'), { recursive: true });
for (const book of books) {
  const target = join(root, 'public', 'cards', `${book.slug}.svg`);
  writeFileSync(target, card(book), 'utf8');
}
console.log(`wrote ${books.length} card images to public/cards/`);
