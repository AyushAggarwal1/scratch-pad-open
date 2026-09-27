---
title: Overview
nav_order: 1
description: "I'm Ayush, a TPM working on cloud-security products. Explore my product requirements, architecture notes, and practical security tools."
permalink: /
page_class: home-page
heading_anchors: false
has_toc: false
---

<section class="home-hero" aria-labelledby="hero-title">
  <div class="hero-copy">
    <p class="eyebrow"><span class="status-dot"></span>PRODUCT THINKING. PRACTICAL BUILDING.</p>
    <h1 id="hero-title">Cloud security.<br><em>From the inside out.</em></h1>
    <p class="hero-intro">I'm <a href="{{ '/about/' | relative_url }}">Ayush</a>, a TPM working on cloud-security products.<br class="desktop-break"> This is where I share the thinking behind the work.</p>
    <p class="hero-description">Product requirements, architecture decisions, and the commands I keep coming back to. Written while building. Open for you to explore.</p>
    <div class="hero-actions"><a class="action-primary" href="#selected-work">Explore my work {% include ui/icon.html name="arrow" %}</a><a class="action-text" href="{{ '/notes/' | relative_url }}">Browse the notebook {% include ui/icon.html name="arrow" %}</a></div>
    <div class="hero-signoff"><span aria-hidden="true">↳</span> A working notebook, not a finished story.</div>
  </div>
  <div class="hero-visual" aria-hidden="true">
    <div class="notebook-sheet sheet-back"></div><div class="notebook-sheet sheet-middle"></div>
    <div class="notebook-sheet sheet-front">
      <div class="sheet-heading"><span class="tiny-cross">+</span> FIELD NOTES <span>001 — ∞</span></div>
      <div class="sheet-title">Make the complex<br><em>make sense.</em></div>
      <div class="sketch-flow"><span>{% include ui/icon.html name="cloud" %}</span><i></i><span class="sketch-focus">{% include ui/icon.html name="shield" %}</span><i></i><span>{% include ui/icon.html name="code" %}</span></div>
      <div class="sheet-check"><span>✓</span> Understand the problem</div><div class="sheet-check"><span>✓</span> Connect the systems</div><div class="sheet-check"><span class="check-empty"></span> Keep asking better questions</div>
      <div class="sheet-bottom"><span>ideas → decisions → systems</span><span>↗</span></div>
    </div>
    <span class="notebook-caption">a little structure for big questions</span>
  </div>
</section>

{% assign note_pages = site.html_pages | where_exp: "item", "item.path contains 'notes/'" | where_exp: "item", "item.has_children != true" %}
{% assign tool_pages = site.html_pages | where: "parent", "Security Tools Cmds" %}
<div class="notebook-stats" aria-label="Inside the notebook"><span class="stats-label">A LOOK INSIDE</span><span><strong>{{ note_pages.size }}</strong> notes &amp; references</span><span><strong>{{ site.data.projects.size }}</strong> core security domains</span><span><strong>{{ tool_pages.size }}</strong> security tool guides</span><a href="https://github.com/{{ site.repository }}" target="_blank" rel="noopener noreferrer">All in the open {% include ui/icon.html name="external" %}</a></div>

<section class="home-section" id="selected-work" aria-labelledby="work-heading">
  <div class="section-heading"><div><p class="eyebrow">01 / SELECTED WORK</p><h2 id="work-heading">Deep dives from the workbench.</h2></div><a class="section-link" href="{{ '/notes/' | relative_url }}">All notes {% include ui/icon.html name="arrow" %}</a></div>
  <div class="project-grid">
    {% for project in site.data.projects %}
    <a class="project-card project-{{ project.slug }}" href="{{ project.url | relative_url }}">
      <div class="project-art" aria-hidden="true">
        <div class="art-topline"><span>{{ project.topic }} / WORKING DOCUMENTS</span><span>{{ project.number }}</span></div>
        {% case project.slug %}
        {% when 'ciem' %}<div class="identity-diagram"><div class="diagram-source">{% include ui/icon.html name="shield" %}</div><div class="diagram-branches"><span>Assigned <b>→</b></span><span>Observed <b>→</b></span><span class="diagram-result">Recommended <b>✓</b></span></div></div>
        {% when 'dspm' %}<div class="data-diagram"><div class="data-column"><span>.csv</span><span>.json</span><span>.pdf</span></div><span class="diagram-connector">→</span><div class="data-scanner">{% include ui/icon.html name="database" %}<span>DISCOVER</span></div><span class="diagram-connector">→</span><div class="data-finding"><span class="status-dot"></span>PII</div></div>
        {% when 'aspm' %}<div class="pipeline-diagram"><span>{% include ui/icon.html name="branch" %}<small>COMMIT</small></span><i></i><span>{% include ui/icon.html name="code" %}<small>SCAN</small></span><i></i><span class="pipeline-gate">{% include ui/icon.html name="shield" %}<small>GATE</small></span></div>
        {% endcase %}
        <div class="art-bottomline">{{ project.type }}<span>↗</span></div>
      </div>
      <div class="project-copy"><span class="project-topic">{{ project.topic }}</span><h3>{{ project.title }}</h3><p>{{ project.description }}</p><div class="project-tags">{% for tag in project.tags %}<span>{{ tag }}</span>{% endfor %}</div><span class="project-read">Explore the documents {% include ui/icon.html name="arrow" %}</span></div>
    </a>
    {% endfor %}
  </div>
</section>

<section class="home-section notebook-section" aria-labelledby="notebook-heading">
  <div class="section-heading"><div><p class="eyebrow">02 / THE OPEN NOTEBOOK</p><h2 id="notebook-heading">A few useful places to start.</h2></div><span class="section-aside">Less searching. More building.</span></div>
  <div class="resource-grid">
    <a class="resource-row" href="{{ '/notes/007_rule-engine-assets/' | relative_url }}"><span class="resource-icon">{% include ui/icon.html name="workflow" %}</span><span><strong>From requirements to rules</strong><small>Asset triggers, conditions, and backend design</small></span>{% include ui/icon.html name="arrow" %}</a>
    <a class="resource-row" href="{{ '/cmds/002_security-tools-cmds/' | relative_url }}"><span class="resource-icon">{% include ui/icon.html name="terminal" %}</span><span><strong>The security toolbox</strong><small>Scanner commands worth keeping close</small></span>{% include ui/icon.html name="arrow" %}</a>
    <a class="resource-row" href="{{ '/notes/005_integrations/' | relative_url }}"><span class="resource-icon">{% include ui/icon.html name="link" %}</span><span><strong>Connecting the pieces</strong><small>Jira, Microsoft Teams, and Sumo Logic</small></span>{% include ui/icon.html name="arrow" %}</a>
    <a class="resource-row" href="{{ '/cmds/001_compliance-custom-script/' | relative_url }}"><span class="resource-icon">{% include ui/icon.html name="code" %}</span><span><strong>Small scripts, useful shortcuts</strong><small>Extract, enrich, and convert compliance data</small></span>{% include ui/icon.html name="arrow" %}</a>
  </div>
</section>

<section class="connect-panel" aria-labelledby="connect-heading"><div><p class="eyebrow">GOOD WORK STARTS WITH A CONVERSATION</p><h2 id="connect-heading">Building in this space, too?</h2><p>I'm always happy to exchange ideas on cloud security,<br class="desktop-break"> product thinking, and turning complex problems into useful systems.</p></div><div class="connect-actions"><a class="action-primary" href="{{ site.profile.linkedin }}" target="_blank" rel="noopener noreferrer">Let's connect {% include ui/icon.html name="external" %}</a><a class="action-text" href="mailto:{{ site.profile.email }}">Or send me a note {% include ui/icon.html name="mail" %}</a></div></section>
