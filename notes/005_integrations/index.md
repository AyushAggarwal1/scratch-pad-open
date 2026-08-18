---
title: Integrations
parent: Notes
nav_order: 5
has_children: true
has_toc: false
description: "Setup notes for AccuKnox's outbound integrations — ticketing, chat/alerting, and log-forwarding targets."
---

# Integrations

Setup notes for connecting AccuKnox to external ticketing, chat, and log-forwarding systems.

## The documents

<div class="shelf">
  <a class="shelf-card" href="jira/jira/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
      <span class="shelf-path">ticketing</span>
    </span>
    <strong>Jira</strong>
    <p>APIs to fetch Epics and Stories, and how issue type maps to task vs. sub-task creation.</p>
  </a>
  <a class="shelf-card" href="sumo-logic/sumo/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg></span>
      <span class="shelf-path">log forwarding</span>
    </span>
    <strong>Sumo Logic</strong>
    <p>Hosted vs. installed collector setup, plus the rsyslog forwarding config for VM sources.</p>
  </a>
  <a class="shelf-card" href="teams/ms-teams/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg></span>
      <span class="shelf-path">chat/alerting</span>
    </span>
    <strong>Microsoft Teams</strong>
    <p>Wiring a Teams workflow webhook to an AccuKnox alert channel, on both sides of the integration.</p>
  </a>
</div>

{: .note }
> Two integrations exist only as raw reference assets so far, with no write-up: [`qradar/qradar-server.py`](qradar/qradar-server.py) (a Flask relay for QRadar) and [`service-desk-plus/`](service-desk-plus/) (request/comment JSON payload templates).
