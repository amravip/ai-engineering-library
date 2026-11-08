// Site-wide settings that are not book metadata.
//
// REPO_URL is the public GitHub repository for the companion code. It is empty
// until the author decides the address. While it is empty, every repository link
// on reader pages is hidden, so no address is ever shown before it is decided.
export const REPO_URL = 'https://github.com/amravip/ai-engineering-library';

// The public address of the site, used for the sitemap and canonical links.
// Set the SITE_URL environment variable when the site is deployed.
export const SITE_URL = process.env.SITE_URL || 'http://localhost:4321';
