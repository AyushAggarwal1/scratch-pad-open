#!/usr/bin/env python3
"""Check built HTML links, assets, and fragment targets without dependencies."""

import argparse
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit


class Page(HTMLParser):
    def __init__(self, source):
        super().__init__()
        self.ids = set()
        self.links = []
        self.feed(source)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if attrs.get("id"):
            self.ids.add(attrs["id"])
        if tag in {"a", "link", "img", "script"}:
            url = attrs.get("href") if tag in {"a", "link"} else attrs.get("src")
            if url:
                self.links.append(url)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", nargs="?", default="_site")
    parser.add_argument("--baseurl", default="/scratch-pad-open")
    args = parser.parse_args()
    root = Path(args.directory).resolve()
    baseurl = args.baseurl.rstrip("/")
    pages = {path: Page(path.read_text()) for path in root.rglob("*.html")}
    if not pages:
        parser.error("No HTML found. Run bundle exec jekyll build first.")
    errors = []
    checked = 0
    for path, page in pages.items():
        relative = path.relative_to(root).as_posix()
        page_url = baseurl + "/" + relative.removesuffix("index.html")
        for link in page.links:
            parts = urlsplit(link)
            if parts.scheme or parts.netloc:
                continue
            target = urlsplit(urljoin(page_url, link))
            target_path = unquote(target.path)
            if baseurl and not target_path.startswith(baseurl + "/"):
                errors.append(f"{relative}: outside baseurl: {link}")
                continue
            destination = root / target_path.removeprefix(baseurl).lstrip("/")
            if destination.is_dir():
                destination /= "index.html"
            checked += 1
            if not destination.is_file():
                errors.append(f"{relative}: missing file: {link}")
            elif target.fragment and destination in pages:
                fragment = unquote(target.fragment)
                if fragment not in pages[destination].ids:
                    errors.append(f"{relative}: missing anchor: {link}")
    if errors:
        print("\n".join(errors))
        print(f"\n{len(errors)} broken references in {len(pages)} pages.")
        return 1
    print(f"Checked {len(pages)} pages and {checked} local links/assets: all valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
