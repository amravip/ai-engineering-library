// Site-wide settings that are not book metadata.
//
// REPO_URL is the public GitHub repository for the companion code. It is empty
// until the author decides the address. While it is empty, every repository link
// on reader pages is hidden, so no address is ever shown before it is decided.
// The repository is https://github.com/amravip/ai-engineering-library. It is private for now,
// so the address stays empty: a link to a private repository is a 404 for every reader.
// Put the address back here when the author makes the repository public.
export const REPO_URL = '';

// The public address of the site, used for the sitemap and canonical links.
// The SITE_URL environment variable overrides it, for example for a custom domain.
export const SITE_URL = process.env.SITE_URL || 'https://ai-engineering-library.pages.dev';
