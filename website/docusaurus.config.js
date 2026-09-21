const {themes} = require('prism-react-renderer');

/** @type {import('@docusaurus/types').Config} */
module.exports = {
  title: 'LavaLM',
  tagline: 'Neurosemantic computing, built on an open foundation',
  favicon: 'img/mark.svg',
  url: 'https://darbotlm.github.io',
  baseUrl: '/LavaLM/',
  organizationName: 'DarbotLM',
  projectName: 'LavaLM',
  trailingSlash: true,
  onBrokenLinks: 'throw',
  onBrokenAnchors: 'throw',
  markdown: {
    format: 'detect', mermaid: true,
    hooks: {onBrokenMarkdownLinks: 'throw', onBrokenMarkdownImages: 'throw'},
  },
  themes: ['@docusaurus/theme-mermaid'],
  presets: [['classic', {
    docs: {
      routeBasePath: '/',
      sidebarPath: require.resolve('./sidebars.js'),
      editUrl: 'https://github.com/DarbotLM/LavaLM/edit/main/website/',
    },
    blog: false,
    theme: {customCss: require.resolve('./src/css/custom.css')},
  }]],
  themeConfig: {
    colorMode: {defaultMode: 'dark', respectPrefersColorScheme: true},
    navbar: {
      title: 'LavaLM',
      logo: {alt: 'LavaLM mark', src: 'img/mark.svg'},
      items: [
        {type: 'doc', docId: 'getting-started', label: 'Start', position: 'left'},
        {type: 'doc', docId: 'architecture', label: 'Architecture', position: 'left'},
        {type: 'doc', docId: 'engineering/overview', label: 'Engineering', position: 'left'},
        {href: 'https://github.com/DarbotLM/LavaLM', label: 'GitHub', position: 'right'},
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {title: 'Build', items: [{label: 'API guide', to: '/api'}, {label: 'Contributing', to: '/contributing'}]},
        {title: 'Explore', items: [{label: 'Specifications', to: '/engineering/overview'}, {label: 'Roadmap', to: '/roadmap'}]},
        {title: 'Project', items: [{label: 'Source', href: 'https://github.com/DarbotLM/LavaLM'}, {label: 'Lineage and licenses', to: '/migration'}]},
      ],
      copyright: 'LavaLM · DarbotLM contributors. Built on Lava; upstream attribution and component licenses retained.',
    },
    prism: {theme: themes.github, darkTheme: themes.dracula, additionalLanguages: ['python', 'bash', 'toml']},
  },
};
