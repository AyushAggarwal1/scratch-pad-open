---
title: Notes
nav_order: 2
has_children: true
has_toc: false
page_class: library-page
heading_anchors: false
description: "Browse Ayush Aggarwal's cloud-security product requirements, architecture notes, integration guides, and working references."
---

<p class="eyebrow">THE OPEN NOTEBOOK</p>
<h1>A little context.<br>A lot to explore.</h1>
<p class="page-lede">Product thinking, technical decisions, and things learned along the way.<br class="desktop-break"> Pick a topic, or follow a question.</p>

<div class="topic-library" data-topic-library>
  <div class="library-toolbar" hidden data-library-controls>
    <div class="filter-buttons" role="group" aria-label="Filter topics"><button type="button" class="is-active" data-filter="all" aria-pressed="true">All topics</button><button type="button" data-filter="product" aria-pressed="false">Product &amp; architecture</button><button type="button" data-filter="reference" aria-pressed="false">Guides &amp; references</button></div>
    <label class="topic-search"><span class="sr-only">Filter topics and document titles</span><input type="search" placeholder="Find a topic or document…" data-topic-query></label>
  </div>
  <p class="library-count" data-topic-count aria-live="polite"></p>
  <div class="topic-grid">
    {% assign topics = site.data.topics | where: 'section', 'notes' %}
    {% for topic in topics %}
    {% assign documents = site.html_pages | where: 'parent', topic.title | sort: 'nav_order' %}
    <article class="topic-card" data-topic-card data-category="{{ topic.category }}">
      <div class="topic-card-top"><span class="resource-icon">{% include ui/icon.html name=topic.icon %}</span><span class="topic-count">{% if documents.size > 0 %}{{ documents.size }} docs{% else %}1 note{% endif %}</span></div>
      <h2><a href="{{ topic.url | relative_url }}">{{ topic.label }} {% include ui/icon.html name="arrow" %}</a></h2>
      <p>{{ topic.description }}</p>
      {% if documents.size > 0 %}<ul class="topic-documents">{% for doc in documents %}<li><a href="{{ doc.url | relative_url }}">{{ doc.title }}<span aria-hidden="true">↗</span></a></li>{% endfor %}</ul>{% else %}<a class="topic-open" href="{{ topic.url | relative_url }}">Read the note {% include ui/icon.html name="arrow" %}</a>{% endif %}
    </article>
    {% endfor %}
  </div>
  <div class="library-empty" hidden data-topic-empty><h2>No matching topics.</h2><p>Try a different phrase or browse the full notebook.</p><button type="button" class="action-primary" data-filter-reset>Reset filters</button></div>
</div>

<div class="library-footnote">Looking for something to run? <a href="{{ '/cmds/' | relative_url }}">Explore commands &amp; scripts {% include ui/icon.html name="arrow" %}</a></div>
