---
title: CIEM
parent: Notes
nav_order: 1
has_children: true
has_toc: false
description: "PRDs for CIEM — Cloud Identity & Entitlement Management: permission discovery, usage analysis, and least-privilege recommendations."
---

# CIEM

**Cloud Identity & Entitlement Management** — the part of a CNAPP that answers *"who can do what in our cloud, and how much of that do they actually use?"* These PRDs describe a permission-optimization capability spanning AWS, GCP, Azure, and OCI.

## The documents

<div class="shelf">
  <a class="shelf-card" href="01-ciem-permission/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
      <span class="shelf-path">phase 1</span>
      <span class="shelf-chip">draft v0.1</span>
    </span>
    <strong>Permission Optimization</strong>
    <p>The full product vision: effective-permission calculation, activity-log analysis, risk and confidence scoring, safety guardrails, and the recommendation lifecycle.</p>
  </a>
  <a class="shelf-card" href="02-ciem-permission/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="10"/><circle cx="12" cy="12" r="6"/><circle cx="12" cy="12" r="2"/></svg></span>
      <span class="shelf-path">phase 2</span>
      <span class="shelf-chip">draft v0.1</span>
    </span>
    <strong>Permission Recommendation MVP</strong>
    <p>The narrow first cut: for one selected user, list assigned permissions, check X days of audit logs, and recommend keep or remove.</p>
  </a>
</div>

## Reading order

Start with **Phase 1** for the full problem space and product principles. Then read **Phase 2** for the deliberately small MVP slice: three backend components — permission collector, log analyzer, recommendation engine — and the three questions they must answer.

{: .note }
> The terminology used across both documents — *assigned*, *effective*, *used*, and *unused* permissions — is defined in [Phase 1 · Key Concepts](01-ciem-permission/#5-key-concepts).
