---
title: Cmds
nav_order: 3
has_children: true
has_toc: false
page_class: library-page
heading_anchors: false
description: "Practical security-scanner commands and compliance scripts, collected by Ayush Aggarwal while building cloud-security products."
---

<p class="eyebrow">THE PRACTICAL SIDE</p>
<h1>Less remembering.<br>More doing.</h1>
<p class="page-lede">Security tools and small scripts I reach for while building.<br class="desktop-break"> Working references, ready for the next time.</p>

<div class="tool-collections">
  {% assign topics = site.data.topics | where: 'section', 'cmds' %}
  {% for topic in topics %}
  <a class="tool-collection" href="{{ topic.url | relative_url }}"><span class="resource-icon">{% include ui/icon.html name=topic.icon %}</span><span class="eyebrow">0{{ forloop.index }} / THE TOOLBOX</span><h2>{{ topic.label }}</h2><p>{{ topic.description }}</p><span class="project-read">Open the collection {% include ui/icon.html name="arrow" %}</span></a>
  {% endfor %}
</div>

<h2 class="tool-list-heading">Jump straight to a tool</h2>
<div class="resource-grid">
  {% assign tools = site.html_pages | where: 'parent', 'Security Tools Cmds' | sort: 'nav_order' %}
  {% for tool in tools %}<a class="resource-row" href="{{ tool.url | relative_url }}"><span class="resource-icon">{% include ui/icon.html name="terminal" %}</span><span><strong>{{ tool.title }}</strong><small>{{ tool.description }}</small></span>{% include ui/icon.html name="arrow" %}</a>{% endfor %}
</div>
