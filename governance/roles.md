# Governance Roles

**Layer**: Durable (Layer 2)
**Version**: 0.1.0
**Status**: DRAFT — Phase 0 (Founder governance mode)

## Overview

The Agentism project uses a structured role system designed for progressive decentralization. During Phase 0: Founding, the Founder and AI Collaborator make decisions directly. As the community grows, governance expands through defined phase transitions.

## Current Phase: Phase 0 (Founding)

**Mode**: Founder + AI Collaborator make all decisions.
**Transition trigger**: 10+ active contributors.

All Phase 0 decisions are documented in [`phase0-decisions.md`](phase0-decisions.md) and are subject to retroactive community review when Phase 1 begins.

---

## Defined Roles

### Founder

| Attribute | Detail |
|-----------|--------|
| Selection | Project creator (not elected) |
| Count | 1 |
| Term | Until Phase 3, at which point role becomes honorary |

**Responsibilities:**
- Draft and steward the initial Layer 1 (Immutable) principles
- Make all Phase 0 decisions (documented for retroactive review)
- Enforce transitions between governance phases
- Resist extending Phase 0 beyond its trigger point

**Veto power:**
The Founder holds veto power ONLY over proposals that violate Immutable (Layer 1) principles. This veto is overridable by >90% community vote.

---

### Core Maintainers

| Attribute | Detail |
|-----------|--------|
| Selection | Nominated by existing maintainers + community vote (>60%) |
| Count | 3–7 |
| Term | 12 months, renewable by vote |

**Responsibilities:**
- Merge authority for all Layer 2 and Layer 3 content
- Process enforcement and conflict resolution
- Platform administration
- Cannot unilaterally change Layer 2 (Durable) content — all changes require community vote

---

### Working Group Leads

| Attribute | Detail |
|-----------|--------|
| Selection | Elected within each working group annually |
| Count | 1 per working group |
| Term | 12 months; replaced if <50% confidence vote |

**Responsibilities:**
- Coordinate their working group's activities
- Curate and triage proposals within their domain
- Produce decision summaries when debate does not converge
- Escalate unresolved disputes to Core Maintainers

---

### Contributors

| Attribute | Detail |
|-----------|--------|
| Selection | Self-selected — anyone who registers |
| Count | Unlimited |
| Term | Active as long as they participate |

**Responsibilities:**
- Submit proposals using the [proposal template](proposals/TEMPLATE.md)
- Participate in debates on open proposals
- Vote on resolutions (subject to quorum requirements)
- Disclose relevant conflicts of interest

---

### AI Collaborators

| Attribute | Detail |
|-----------|--------|
| Selection | Configured by Core Maintainers |
| Count | Per task |
| Labeling | Always labeled as AI with model/system identified |

**Responsibilities:**
- Summarize debate threads (generated at day 7 and at debate close)
- Draft content, translate, identify inconsistencies
- Play devil's advocate role on proposals
- Generate accessibility-focused plain-language summaries

**Constraint**: AI Collaborators do not hold votes in any governance process. All AI contributions must be labeled with the model and system used.

---

### Reviewers

| Attribute | Detail |
|-----------|--------|
| Selection | Assigned by Working Group Leads |
| Count | Per proposal |
| Term | Per assignment |

**Responsibilities:**
- Technical and content review of proposals before community debate
- Produce written review with findings
- Disclose any conflicts of interest relevant to the proposal

---

## Conflict of Interest Requirements

All role holders must disclose relevant conflicts of interest (financial, institutional, and ideological affiliations). Role holders with a disclosed COI on a specific proposal must recuse themselves from voting on that proposal. Recusal is public and recorded.

If a COI is discovered after a vote, the decision may be challenged and re-voted. Undisclosed COI is grounds for role removal.

---

## Governance Phase Transitions

| Phase | Mode | Transition Trigger |
|-------|------|--------------------|
| Phase 0: Founding | Founder + AI Collaborator | Until 10+ active contributors |
| Phase 1: Seeding | Founder + 2-3 Core Maintainers; simplified voting | Until 50+ active contributors |
| Phase 2: Operating | Full governance as specified | Until sustained for 6 months |
| Phase 3: Mature | Community self-governs; Founder role becomes honorary | Steady state |

Transitions are not automatic. Each transition requires explicit community acknowledgment.

---

*This document was co-developed with an AI Collaborator (Claude Sonnet 4.6 via GitHub Copilot). Reviewed and approved by the Founder. Per CP-004 and HAI-001.*

