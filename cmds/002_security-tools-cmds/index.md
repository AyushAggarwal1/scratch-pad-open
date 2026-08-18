---
title: Security Tools Cmds
parent: Cmds
nav_order: 2
has_children: true
has_toc: false
description: "Run commands for the security scanners used against this repo and cloud accounts — Betterleaks, Checkov, Cloudsplaining, Cloudsploit, Prowler."
---

# Security Tools Cmds

CLI invocations for the scanners run against this codebase and connected cloud accounts.

## The tools

<div class="shelf">
  <a class="shelf-card" href="betterleaks/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 15a3 3 0 1 0 0-6 3 3 0 0 0 0 6z"/><path d="M12 1v6m0 10v6m11-7h-6M7 12H1"/></svg></span>
      <span class="shelf-path">secrets</span>
    </span>
    <strong>Betterleaks</strong>
    <p>Secret scanning over a directory, SARIF output.</p>
  </a>
  <a class="shelf-card" href="checkov/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M9 9h6v6H9z"/></svg></span>
      <span class="shelf-path">IaC</span>
    </span>
    <strong>Checkov</strong>
    <p>IaC scan over a directory, all frameworks, JSON output.</p>
  </a>
  <a class="shelf-card" href="cloudsplaining/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg></span>
      <span class="shelf-path">IAM · multi-cloud</span>
    </span>
    <strong>Cloudsplaining</strong>
    <p>IAM risk scan across AWS, Azure, GCP, and OCI — setup and scan commands per provider.</p>
  </a>
  <a class="shelf-card" href="cloudsploit/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 10h-1.26A8 8 0 1 0 9 20h9a5 5 0 0 0 0-10z"/></svg></span>
      <span class="shelf-path">CSPM</span>
    </span>
    <strong>Cloudsploit</strong>
    <p>Config-driven scan, JSON output.</p>
  </a>
  <a class="shelf-card" href="prowler/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg></span>
      <span class="shelf-path">identity-access · multi-cloud</span>
    </span>
    <strong>Prowler</strong>
    <p>Identity-access category scan across AWS, Azure, GCP, and OCI, OCSF JSON output.</p>
  </a>
</div>
