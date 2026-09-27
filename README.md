# Ayush's open notebook

A public notebook and work showcase by **Ayush Aggarwal**, a TPM working on
cloud-security products. Product requirements, architecture notes, practical
security commands, and references across CIEM, DSPM, and ASPM.

**Live site:** https://ayushaggarwal1.github.io/scratch-pad-open/

## How the site works

This is a static **Jekyll** site using **Just the Docs v0.12.0**, with a custom
layout and visual system. Markdown is the content source. GitHub Pages builds
and hosts the site; there is no application server or JavaScript build step.

- **Overview** introduces the author and showcases three areas of work.
- **Notes** lists every topic and its documents, with optional category and text filters.
- **Cmds** collects scanner commands and compliance scripts.
- **About** connects the product work to the person behind it.
- The theme supplies full-text search, nested navigation, code copying, and heading links.
- Custom JavaScript adds topic filters and a persistent light/dark preference.
  All document links remain usable without JavaScript.

The technical documents are working notes and specifications. Featured copy
reflects their contents, without presenting proposed features as shipped results.

## Local development

Use Ruby 3.3 or newer and the Bundler version recorded in `Gemfile.lock`.
The first build needs internet access to download the pinned remote theme.

```sh
bundle install
bundle exec jekyll serve --livereload
```

Open http://localhost:4000/scratch-pad-open/.

To build and check internal links, assets, and heading anchors:

```sh
bundle exec jekyll build
python3 scripts/check_site.py
node --check assets/js/notebook.js
```

Python 3.9+ is needed only for the link checker. Node is needed only for the
optional JavaScript syntax check. Neither is required to publish the site.

The checker also accepts another destination/base path:

```sh
python3 scripts/check_site.py /tmp/site --baseurl /scratch-pad-open
```

## Editing the site

| File | Purpose |
| --- | --- |
| `index.md` | Introduction, selected work, useful starting points, contact panel |
| `about.md` | Author introduction and links to work |
| `_data/projects.yml` | Featured work, descriptions, tags, and sidebar shortcuts |
| `_data/topics.yml` | Topic order, categories, descriptions, icons, and destinations |
| `notes/index.md` | Topic library; child links and counts come from page metadata |
| `cmds/index.md` | Tool collections and automatically listed scanner guides |
| `_config.yml` | Profile links, metadata, theme pin, search, and deployment path |
| `_layouts/default.html` | Shared layout and document reading metadata |
| `_includes/` | Branding, navigation, icons, profile, header, and footer |
| `_sass/color_schemes/` | Light/dark colors and shared typography settings |
| `_sass/custom/` | Shared styles plus shell, homepage, library, document, and responsive partials |
| `assets/js/notebook.js` | Theme persistence, search input support, and topic filtering |
| `assets/images/social-card.svg` | Editable source for the social preview |
| `assets/images/social-card.png` | 1200 × 630 social preview used by Open Graph and Twitter metadata |
| `scripts/check_site.py` | Dependency-free validation of the generated site |

The existing numbered content folders and document URLs are preserved. Raw
Python, JSON, and other references are static downloads, not site executables.

### Add a note

Create a Markdown file in the actual topic folder, for example
`notes/004_ciem/jit-access.md`:

```yaml
---
title: JIT Access
parent: CIEM
grand_parent: Notes
nav_order: 3
description: "A short, useful description of the document."
---
```

Start the body with one `#` heading. The note automatically appears in the
sidebar, search, and the Notes library under CIEM. For a long document, add:

```markdown
## On this page
{: .no_toc .text-delta }

- TOC
{:toc}
```

If an example contains literal double-brace placeholders, wrap that example in
Liquid's `raw` / `endraw` tags so Jekyll doesn't interpret it as a template.

### Add a topic

1. Create a topic index with `title`, `parent: Notes`, `nav_order`,
   `has_children: true`, and `has_toc: false` in its front matter.
2. Add an entry to `_data/topics.yml`. Use the same `title` as the topic index,
   `section: notes`, and `category: product` or `reference`.
3. Use a full site path for `url`, such as `/notes/018_new-topic/`.
4. Child pages use the topic title as `parent` and `grand_parent: Notes`.

A standalone note can also be a topic: link its page directly from the data
file. The library shows it as one note. Add featured work to `_data/projects.yml`
and choose a corresponding homepage diagram if you add a new visual category.

For template links, use Jekyll's `relative_url` filter so the site works under
its GitHub Pages project path. Raw Markdown links within existing topic folders
also work; avoid links to folders that have no index page.

## Design and checks

Warm paper, charcoal type, and terracotta accents give the notebook a consistent
identity. Typography uses IBM Plex Sans/Mono and an italic Newsreader accent,
with system fallbacks. The notebook and project illustrations are HTML/CSS/SVG.

The theme preference uses the existing `osn-scheme` localStorage key, falls back
to the system preference, and follows system changes until a preference is saved.
Controls have keyboard focus states, filters announce result counts, and motion
respects `prefers-reduced-motion`.

Before publishing, preview the overview, library, commands, and a long document
at desktop and mobile widths. Check search (Ctrl/Cmd+K), navigation, filters and
reset, code copying, theme persistence, and internal links. If you update the
social-card SVG, export a matching 1200 × 630 PNG before publishing.

## Publishing

With GitHub Pages configured to deploy from `main` at the repository root,
pushing to `main` publishes the site. Review and run the build/link checks before
pushing. This refactor does not require a hosting migration or a new service.
