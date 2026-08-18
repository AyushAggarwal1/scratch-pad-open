---
title: Backend Requirements
parent: Rule Engine for Assets
grand_parent: Notes
nav_order: 1
description: "Full requirement doc for extending the Rule Engine to run in the context of Assets — is_new, triggers, actions, and open questions."
---

# Requirement Document — Rule Engine for Assets

| | |
|---|---|
| **Status** | Draft |
| **Owner** | Ayush Aggarwal |
| **Last updated** | 2026-06-16 |
| **Affected components** | `source/models/rule_engine.py`, `source/tasks.py`, `source/serializers/rule_engine.py`, `source/signals/triggers.py`, `source/managers.py`, `source/models/asset.py` |

---

## 1. Overview

The Rule Engine lets users define **Rules** (a `data_type` + `conditions`) that, when matching
objects are created or changed, fan out **Actions** (create ticket, notify, change status, etc.).
Today the engine supports `Finding`, `Check`, and `DataList` only.

This document specifies extending the engine to operate **in the context of Assets**, so users
can be notified and act when assets appear or change (e.g. a new unmanaged AI asset, an asset
tagged `Public`), including actions that target the asset's **findings**.

## 2. Background & problem statement

The engine fires from the `manager_method_called` signal, emitted by `RuleEngineCustomManager`
on create/update/bulk writes (`source/managers.py`). `run_rule_engine` (`source/tasks.py:2838`)
matches the changed objects against each enabled rule via `FILTER_SET_MAPPING`, then dispatches
actions through the transactional outbox (`OutboxEvents`).

**Current limitation:** there is no way to react to asset lifecycle changes. Users cannot be
notified when an asset is newly discovered or when an asset's attributes (e.g. tags) change.

## 3. Goals / non-goals

**Goals**
- Add an `Is New` concept for Assets (and reuse it for Findings).
- Allow Rules with `data_type = Asset`.
- Support actions triggered by asset matches, including actions that apply to the asset's findings.
- Support count/threshold conditions ("total findings > / < X").

**Non-goals**
- Reworking the notification delivery layer.
- Changing the Finding/Check/DataList rule behaviour beyond the shared `is_new` addition.
- A general cross-model rule language (only the specific Asset↔Finding hop in scope).

## 4. Glossary

| Term | Meaning |
|---|---|
| Rule | `data_type` + JSON `conditions`, with one or more Actions. |
| Action | An executable (`create_ticket`, `change_status`, …) with `arguments`. |
| Trigger | A DB write routed through `RuleEngineCustomManager` that emits `manager_method_called`. |
| `is_new` | Marker indicating an asset/finding was discovered in the current scan cycle. |
| Outbox | `OutboxEvents` rows that drive reliable, transactional action dispatch. |

---

## 5. Functional requirements

### FR-1 — `Is New` for Assets and Findings
- **FR-1.1** Add an `is_new` capability for Assets. Decision required (see Open Question OQ-1):
  derived (created within window) **or** persisted boolean with an explicit reset step.
- **FR-1.2** Reuse / expose `is_new` for Findings (Finding already has `date_discovered`,
  `source/models/vulnerability.py:195`).
- **FR-1.3** If persisted: define who clears the flag and when (e.g. end of scan cycle or on
  acknowledgement), and guarantee a "new" object notifies **at most once** (idempotency).
- **FR-1.4** `is_new` must be filterable in `AssetFilterSet` / `FindingDashboardFilterSet` so it
  can be used as a rule condition.

### FR-2 — Rule Engine runs in the context of Assets
- **FR-2.1** Add `Asset` to `Rule.DataTypeChoices`.
- **FR-2.2** Register `Asset: AssetFilterSet` in `FILTER_SET_MAPPING` (filterset exists at
  `source/filters/asset.py:44`).
- **FR-2.3** Ensure asset writes trigger the engine. `Asset` currently uses the default manager
  and does **not** emit `manager_method_called`. Wire it via `RuleEngineCustomManager` or an
  explicit trigger. Must account for bulk scan ingestion volume (see NFR-1).
- **FR-2.4** Tag changes must trigger evaluation. Asset tags are a `GenericRelation` via
  `TagItem`; adding a tag does not write the `Asset` row, so a `TagItem`-level trigger scoped to
  assets is required (covers the `Public` tag use case).

### FR-3 — Actions
- **FR-3.1** Create Ticket — reuse `rule_engine_create_ticket`.
- **FR-3.2** Send to Notification — reuse `rule_engine_send_to_cwpp_channels`.
- **FR-3.3** Change Status / Change Severity / Ignore — these operate on **Findings**. When the
  matched `data_type` is `Asset`, the engine must resolve asset → findings
  (`Finding.objects.filter(asset_id__in=...)`) before the action runs. Resolution should live in
  the action dispatch keyed by `model_name`, not inline in `run_rule_engine`.
- **FR-3.4** Register valid Asset actions in `ACTION_MAPPINGS` so serializer validation accepts
  them (`source/serializers/rule_engine.py:22`).
- **FR-3.5** All new action tasks must follow the existing contract: `autoretry_for`,
  `retry_kwargs`, outbox-driven dispatch, and RabbitMQ audit logging via
  `send_notification_log_to_rabbitmq`.
- **FR-3.6** (Recommended) Add asset-native actions: add tag, assign owner, add to group/label.

### FR-4 — New condition types
- **FR-4.1** Threshold condition: total findings for an asset `>` / `<` X. This is an **aggregate**,
  not a per-object filter — it needs a grouped count query and a dedicated evaluation path
  (the current engine matches per object via `filterset.qs`).
- **FR-4.2** Cross-entity condition: Finding `is_new` AND Asset `is_new`. Modelled as a Finding
  rule with asset-prefixed filters joining `Finding.asset`, or an Asset rule carrying a nested
  finding condition. Pick one shape (see OQ-2).

### FR-5 — Action precedence & dedup
- **FR-5.1** Define precedence when a rule both ignores a finding and creates a ticket/notifies.
- **FR-5.2** De-duplicate notifications for `is_new` matches during bulk ingest (per-rule cooldown
  or batched summary, reusing `create_rule_engine_execution_notification`).

---

## 6. Non-functional requirements

- **NFR-1 — Throughput:** Asset/finding writes occur in bulk during scans. Triggering must not
  enqueue an unbounded number of rule-engine tasks; batch where possible and avoid per-row fan-out.
- **NFR-2 — Reliability:** Actions continue to dispatch via the transactional outbox; no action is
  lost or double-executed on retry.
- **NFR-3 — Multi-tenancy:** All evaluation and dispatch run within the correct tenant schema
  (`replica_aware_schema_context`); no cross-tenant leakage.
- **NFR-4 — Auditability:** Every executed action emits a structured RabbitMQ log entry.
- **NFR-5 — Backward compatibility:** Existing Finding/Check/DataList rules behave unchanged.

---

## 7. Use cases

| # | Scenario | Trigger | Condition | Action | New work |
|---|---|---|---|---|---|
| UC-1 | New unmanaged AI asset | Asset create | `asset_type = Unmanaged AI` AND `is_new` | Send notification | FR-1, FR-2.1/2.2/2.3 |
| UC-2 | `Public` tag added to asset | TagItem create on asset | tag = `Public` | Notify / asset action | FR-2.4 |
| UC-3 | New finding on new asset | Finding create | Finding `is_new` AND Asset `is_new` | Notify / finding action | FR-4.2 |
| UC-4 | Asset finding count crosses threshold | Finding create/update | count of findings `>`/`<` X | Notify / ticket | FR-4.1 |

## 8. Data model changes (indicative)

- `Asset`: add `is_new` (and/or `first_seen`) per OQ-1; switch to / wrap with
  `RuleEngineCustomManager` per FR-2.3.
- `Rule.DataTypeChoices`: add `ASSET = "Asset"`.
- Registries: `FILTER_SET_MAPPING`, `ACTION_MAPPINGS`, `ACTION_TASK_MAPPING` extended for Asset.
- Migrations must use `SmartAddIndex` / `SmartRemoveIndex` if any index is added.

## 9. Risks

| Risk | Impact | Mitigation |
|---|---|---|
| Asset trigger not wired | Rules silently never fire | FR-2.3 explicit wiring + test |
| Stale `is_new` flag | Repeated/duplicate notifications | FR-1.3 reset + idempotency |
| Bulk-ingest task storm | Worker saturation | NFR-1 batching, FR-5.2 dedup |
| Asset→Finding action hop missed | Status/severity/ignore no-op for asset rules | FR-3.3 dispatch-level resolution |

## 10. Open questions

- **OQ-1:** Is `is_new` **derived** (created within a window) or **persisted** (boolean + reset)?
- **OQ-2:** Is the cross-entity rule (UC-3) modelled as a Finding rule with asset filters, or an
  Asset rule with a nested finding condition?
- **OQ-3:** For UC-4, is the threshold evaluated per asset, per asset-type, or globally?
- **OQ-4:** Should `is_new` notifications be per-object or batched per scan?

## 11. Out of scope / future

- General multi-model rule composition beyond Asset↔Finding.
- UI for rule authoring (assumed handled separately).
