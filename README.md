# Open Source Notepad

The public half of my scratchpad — PRDs, commands, references, and field
notes from building cloud-security products. Everything is just notes,
organized by topic.

**Live site:** https://ayushaggarwal1.github.io/scratch-pad-open/

## Repository layout

```text
index.md                  → home page
404.html                  → not-found page
notes/
  index.md                → the "Notes" section page (topic cards)
  ciem/
    index.md              → topic page (CIEM)
    01-ciem-permission.md → a note
    02-ciem-permission.md → a note
_config.yml               → site config (theme pin, search, callouts…)
_sass/                    → color schemes + custom styling
_includes/                → fonts, favicon, scheme toggle
assets/css/               → dark-scheme stylesheet entry point
```

## Publishing

Pushing to `main` is deploying. GitHub Pages (Settings → Pages →
"Deploy from a branch": `main` / root) rebuilds the site automatically,
usually within a couple of minutes. There is no build step to run locally.

## Writing notes

### Add a note to an existing topic

Create a Markdown file inside the topic folder, e.g.
`notes/ciem/jit-access.md`:

```yaml
---
title: JIT Access          # name shown in the sidebar
parent: CIEM               # must match the topic index's title
grand_parent: Notes
nav_order: 3               # position within the topic
---
```

Below the front matter, write normal Markdown: one `# Title` at the top,
`##` for sections. Sidebar, breadcrumbs, and search pick the page up
automatically on push.

### Start a new topic

Create a folder under `notes/` with an `index.md`:

```yaml
---
title: Kubernetes          # the topic's name
parent: Notes
nav_order: 2               # position within Notes
has_children: true
---
```

Pages inside the folder then use `parent: Kubernetes` and
`grand_parent: Notes`. Then add the topic to the index on
`notes/index.md` (copy an existing `index-topic` block and its document
rows) — the index is hand-curated; navigation and search work without
it.

### Optional flourishes

Copy-paste from the CIEM pages:

**"On this page" panel** (for long documents; lists `##` sections):

```markdown
## On this page
{: .no_toc .text-delta }

- TOC
{:toc}
```

**Status chips** under the title:

```markdown
Draft v0.1
{: .label .label-yellow }
CIEM · CNAPP
{: .label .label-purple }
```

**Callouts** (defined in `_config.yml`):

```markdown
{: .note }
> Something worth flagging.
```

Also available: `{: .important }`, `{: .warning }`, `{: .new }`.

**Mermaid diagrams**: uncomment the `mermaid:` block in `_config.yml`,
then use ```` ```mermaid ```` code fences.

### Edit entirely in the browser

Every page has an *Edit this page on GitHub* link in its footer. Editing
there and committing to `main` publishes automatically — no local setup
needed. This is the lowest-friction way to jot a quick note.

## Design

Built on [Just the Docs](https://just-the-docs.com), pinned in
`_config.yml` via `remote_theme: just-the-docs/just-the-docs@v0.12.0`.
Leave the pin unless deliberately upgrading (custom styling is written
against this version).

The look — pure-white light mode, dark mode behind the sidebar toggle,
graphite-ink interactive elements + a single amber (`#e0a63f`) accent, IBM Plex type:

- `_sass/color_schemes/scratchpad.scss` — light scheme (default); all
  colors live in scheme variables
- `_sass/color_schemes/scratchpad-dark.scss` — dark scheme
- `_sass/custom/custom.scss` — sidebar, home page, cards, icons, polish
- `_includes/head_custom.html` — fonts, favicon, scheme restore on load
- `_includes/nav_footer_custom.html` — the dark/light toggle
  (persists to localStorage key `osn-scheme`)

To change the accent: swap `$link-color` / `$btn-primary-color` /
`$osn-nav-active-color` in both scheme files. Card icons are small inline
Feather-style SVGs (`stroke="currentColor"`), so they recolor themselves.

## Local preview

With Ruby installed:

```sh
bundle install
bundle exec jekyll serve --livereload
# open http://localhost:4000/scratch-pad-open/
```

Without Ruby, a one-off build in Docker (mirrors the GitHub Pages
environment):

```sh
docker run --rm -v "$PWD":/src:ro ruby:3.3 bash -c \
  "cp -r /src /build && cd /build && bundle install --quiet && bundle exec jekyll build -d /tmp/site && echo OK"
```
