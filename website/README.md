# LavaLM Docusaurus wiki

The wiki lives in this repository so code, specifications, and documentation can be reviewed together. It is a Docusaurus site, not the separate GitHub `.wiki.git` service.

## Local development

Use Node.js 22+ and run `npm ci`, then `npm start` in this directory. `npm run build` creates `build/` and fails on broken internal links. `npm run serve` previews that production build at `/LavaLM/`. Commit `package-lock.json`; do not commit `node_modules/`, `.docusaurus/`, or `build/`.

Pages are in `docs/`; navigation is in `sidebars.js`. Use ordinary Markdown (`.md`), or `.mdx` when a page needs JSX. Keep all `@docusaurus/*` packages on the same version. The initial scaffold uses Docusaurus 3.10.2.

## Deployment

1. In the repository Settings → Pages, set the source to **GitHub Actions**.
2. Merge the documentation workflow and content into `main` after review.
3. The Documentation workflow builds and publishes using the `github-pages` environment. Repository or environment rules may require an approver.
4. Confirm the workflow's deployment URL. The configured URL is `https://darbotlm.github.io/LavaLM/`.

Pull requests only build and upload `documentation-preview`; they never publish the site. No custom domain or DNS change is made by this scaffold. If a domain is later configured, update `url`, `baseUrl`, and the host settings together.

## Specification maintenance

Every engineering specification retains its original audited revision, source evidence, acceptance criteria, and compatibility challenge. Its implementation status is separate from that historical evidence. Update the individual specification and `docs/engineering/implementation.md` when a patch lands. Do not relabel baseline failure evidence as post-fix validation.

Official references: [installation](https://docusaurus.io/docs/installation), [configuration](https://docusaurus.io/docs/api/docusaurus-config), and [Pages workflows](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
