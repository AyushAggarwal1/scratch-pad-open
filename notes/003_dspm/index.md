---
title: DSPM
parent: Notes
nav_order: 3
has_children: true
has_toc: false
description: "Data Security Posture Management — onboarding, scan engine design, supported file formats, and the Presidio recognizer catalog."
---

# DSPM

**Data Security Posture Management** — scans cloud storage (S3, Blob, Cloud Storage, Object Storage) for sensitive data using Presidio recognizers plus a lightweight ML pass, and reports findings back through Event-Trail.

## The documents

The [finding catalog references](refs/) collect the research behind finding names, recognizers, and enrichment fields.

<div class="shelf">
  <a class="shelf-card" href="dspm/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 6c0-1.1 3.6-2 8-2s8 .9 8 2-3.6 2-8 2-8-.9-8-2z"/><path d="M4 6v6c0 1.1 3.6 2 8 2s8-.9 8-2V6"/><path d="M4 12v6c0 1.1 3.6 2 8 2s8-.9 8-2v-6"/></svg></span>
      <span class="shelf-path">overview</span>
    </span>
    <strong>DSPM Overview &amp; Onboarding</strong>
    <p>Cloud account onboarding, MVP scan services per provider, supported file formats, and the DSPM engine's Event-Trail log types.</p>
  </a>
  <a class="shelf-card" href="recognizers/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></span>
      <span class="shelf-path">reference</span>
    </span>
    <strong>Presidio Recognizers Reference</strong>
    <p>The full table of country-specific PII recognizers the scan engine draws on — 19 countries/regions, 65 recognizers.</p>
  </a>
</div>
