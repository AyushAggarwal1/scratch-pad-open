---
title: Rule Engine for Assets
parent: Notes
nav_order: 7
has_children: true
has_toc: false
description: "Extending the Rule Engine to run in the context of Assets — is_new detection, asset-scoped triggers, and cross-entity conditions."
---

# Rule Engine for Assets

The Rule Engine today only reacts to `Finding`, `Check`, and `DataList` writes. This work extends it to run **in the context of Assets** too, so a rule can fire on asset discovery or attribute change, including actions that reach through to the asset's findings.

## The documents

<div class="shelf">
  <a class="shelf-card" href="RuleEngineForAssetsBE/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/></svg></span>
      <span class="shelf-path">requirements</span>
    </span>
    <strong>Backend Requirements</strong>
    <p>The full requirement doc: functional/non-functional requirements, data model changes, risks, and open questions.</p>
  </a>
  <a class="shelf-card" href="RuleEngineForAssets/">
    <span class="shelf-head">
      <span class="shelf-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 20h9"/><path d="M16.5 3.5a2.12 2.12 0 0 1 3 3L7 19l-4 1 1-4z"/></svg></span>
      <span class="shelf-path">working notes</span>
    </span>
    <strong>Notes &amp; Use Cases</strong>
    <p>The earlier, rougher pass — limitations and use cases that fed into the backend requirements doc.</p>
  </a>
</div>

{: .note }
> [`asset_template.json`](asset_template.json) holds a sample asset payload referenced by the requirements doc.
