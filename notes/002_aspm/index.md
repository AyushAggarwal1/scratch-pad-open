---
title: ASPM
parent: Notes
nav_order: 2
has_children: true
has_toc: false
description: "Application Security Posture Management — phased rollout plan, SCM onboarding, quality gates, and a competitive scan of CloudDefense."
---

# ASPM

**Application Security Posture Management** — consolidating SAST, SCA, secret, and IaC scanning across GitHub, GitLab, and Bitbucket into one onboarding and workflow surface, with CI-blocking quality gates on top.

## The documents

<div class="shelf">
  <a class="shelf-card" href="01-aspm-phase-1/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
      <span class="shelf-path">phase 1</span>
    </span>
    <strong>ASPM Phase 1</strong>
    <p>Supported SCMs and scan types, the unified CLI/Action workflow, AI-SAST, and redirection rules per finding type.</p>
  </a>
  <a class="shelf-card" href="02-aspm-phase-2/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></span>
      <span class="shelf-path">phase 2</span>
    </span>
    <strong>ASPM Phase 2</strong>
    <p>Assets view, PR-based scanning, API discovery, and the organization → group → repo → branch asset model.</p>
  </a>
  <a class="shelf-card" href="clouddefense-aspm/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg></span>
      <span class="shelf-path">competitive</span>
    </span>
    <strong>CloudDefense Comparison</strong>
    <p>Feature-by-feature look at CloudDefense's ASPM, and where its gaps are worth exploiting.</p>
  </a>
  <a class="shelf-card" href="quality-gates/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span>
      <span class="shelf-path">flow</span>
    </span>
    <strong>Quality Gates Flow</strong>
    <p>How a CLI-embedded policy ID lets a CI pipeline poll AccuKnox for a pass/fail result before proceeding.</p>
  </a>
</div>

## SCM setup references

Step-by-step OAuth/App registration notes used when onboarding each source-control provider:

<div class="index-topic">
  <div class="index-topic-head">
    <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg></span>
    <span class="index-topic-title">SCM App Setup</span>
    <span class="shelf-chip">3 docs</span>
  </div>
  <p class="index-topic-desc">Registration steps, required scopes, and token/refresh API calls for each provider.</p>
  <ul class="index-docs">
    <li>
      <a href="github/github-docs/">
        <span class="index-doc-title">GitHub App Setup</span>
      </a>
    </li>
    <li>
      <a href="gitlab/docs/gitlab/">
        <span class="index-doc-title">GitLab App Setup</span>
      </a>
    </li>
    <li>
      <a href="bitbucket/bitbucket-docs/">
        <span class="index-doc-title">Bitbucket OAuth Setup</span>
      </a>
    </li>
  </ul>
</div>

{: .note }
> Also in this folder: [`gitlab/setup/gitlab.yaml`](gitlab/setup/gitlab.yaml) (self-hosted GitLab docker-compose), [`rotate-aspm-tokens.py`](rotate-aspm-tokens.py) (token rotation task), and onboarding screenshots under `prototype/`.
