# Decision-Making Process

**Layer**: Durable (Layer 2)
**Version**: 0.1.0
**Status**: DRAFT — Phase 0 (Founder governance mode)

## Overview

This document defines voting thresholds, debate periods, conflict resolution procedures, and the constitutional crisis procedure for the Agentism project.

---

## Proposal Workflow

Every formal change to the project follows this sequence:

```
SUBMIT → TRIAGE → DEBATE → RESOLVE → MERGE or ARCHIVE
```

| Stage | Actor | Time Limit |
|-------|-------|-----------|
| **SUBMIT** | Author fills proposal template | — |
| **TRIAGE** | Working Group Lead assigns reviewers; or rejects with written rationale | 7 days from submission |
| **DEBATE** | Community discussion, time-bounded by layer | 14–60 days |
| **RESOLVE** | Vote or consensus; all records public | At debate close |
| **MERGE / ARCHIVE** | Core Maintainer executes outcome | Within 7 days of resolution |

**If triage does not happen within 7 days**, the proposal auto-escalates to Core Maintainers.

The author may revise the proposal once during the debate period. Rejected proposals include written rationale; authors may resubmit after addressing it.

---

## Voting Thresholds

| Layer | Threshold | Quorum | Debate Period | Cooling Period |
|-------|-----------|--------|---------------|----------------|
| Layer 1 (Immutable) | >80% supermajority | 50% of registered active contributors | 60 days | 60 days after vote |
| Layer 2 (Durable) | >60% majority | 30% of registered active contributors | 30 days | 14 days after vote |
| Layer 3 (Adaptive) | Working group consensus + maintainer approval | No formal quorum | 14 days | None |

All voting records (individual votes, totals, dissenting opinions) are public.

---

## Conflict Resolution

When debate does not converge within the time bound, the Working Group Lead produces a decision summary containing:
1. The majority position
2. The minority position(s)
3. A recommended resolution with rationale

If the recommendation is contested, it escalates to Core Maintainers for binding resolution.

If Core Maintainers are split, the matter goes to a community vote with a simple majority (>50%) threshold.

Dissenting opinions are always recorded alongside decisions. Minority positions have permanent visibility — they are never deleted or hidden.

---

## AI Summarization

AI Collaborators generate summary documents of debate threads at:
- Day 7 of the debate period
- At debate close

These summaries are clearly labeled as AI-generated and include the model used. They are advisory — they do not replace the debate record and cannot be used as a substitute for human review.

---

## Constitutional Crisis Procedure

### Triggered Responses

| Scenario | Trigger | Response |
|----------|---------|----------|
| **Compromised maintainers** | Evidence that >50% of Core Maintainers are acting in bad faith or under external influence | Any 3 active contributors may call an emergency community vote (simple majority) to replace the entire Core Maintainer team |
| **Hostile majority** | A coordinated faction uses legitimate governance to steer the project against its own principles | The Founder (or 3 longest-serving contributors if Founder is unavailable) may freeze governance for 30 days and call a community-wide principle reaffirmation vote |
| **Deadlocked governance** | No proposals pass for 6 consecutive months due to systematic blocking | Core Maintainers may temporarily lower voting thresholds by 10 percentage points for 90 days, with mandatory public justification |
| **Appeals process** | A contributor believes a governance decision was procedurally flawed | Written appeal to Core Maintainers within 14 days of decision. Response required within 14 days. If unresolved, community vote. |

Emergency governance actions are time-limited and require post-hoc community ratification within 60 days.

---

## Decision Logging

All decisions — regardless of phase — are logged in [`phase0-decisions.md`](phase0-decisions.md) during Phase 0, and in dedicated decision logs from Phase 1 onward.

Each log entry includes:
- Decision ID and date
- What was decided
- Rationale
- Any dissenting views
- Who made the decision (with role disclosure)

---

*This document was co-developed with an AI Collaborator (Claude Sonnet 4.6 via GitHub Copilot). Reviewed and approved by the Founder. Per CP-004 and HAI-001.*

