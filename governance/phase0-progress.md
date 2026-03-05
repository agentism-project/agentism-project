# Phase 0 Progress Tracker

**Governance mode**: Founder + AI Collaborator
**Phase**: Phase 0: Founding
**Exit trigger**: 10+ active contributors

This document tracks progress toward Phase 0 completion. Updated as deliverables are completed.

---

## Deliverables Status

| # | Deliverable | Status | Notes |
|---|-------------|--------|-------|
| 0.1 | SRS published and accessible | COMPLETE | All 14 sections in `SRS/`, untracked from .gitignore |
| 0.2 | Repository restructured to match SRS Section 07.3 | COMPLETE | All directories created, structure matches spec |
| 0.3 | Core principles published as DRAFT documents | COMPLETE | CP-001–CP-005 all created in `principles/` with FK target summaries |
| 0.4 | Governance framework published | COMPLETE | roles.md, decision-making.md, proposals/TEMPLATE.md, 7 WG charters, phase0-decisions.md |
| 0.5 | Hugo website deployed | IN PROGRESS | hugo.toml, layouts, CSS complete. Deploy workflow created. GitHub Pages setup requires human action. |
| 0.6 | GitHub community infrastructure established | PARTIAL | Issue templates, PR template, CI workflows complete. GitHub Discussions requires human action (T039–T041). |
| 0.7 | Official communication channels established | PARTIAL | Email active. Social media accounts require human action (T052). Official channels document created. |
| 0.8 | Transparency and accountability framework in place | COMPLETE | Transparency report template, platform migration plans, phase0-decisions log, AI labeling in CoC and CONTRIBUTING |

---

## Tasks Requiring Human Action

These tasks cannot be automated and require manual action by the Founder:

| Task | What is needed | Priority |
|------|---------------|----------|
| T036 | Grant a second GitHub account admin access to the repository | P1 |
| T039 | Enable GitHub Discussions in repository Settings | P0 |
| T040 | Post welcome message in GitHub Discussions (after T039) | P1 |
| T041 | Verify GitHub Discussions export is possible (data portability) | P1 |
| T048 | Run Lighthouse audit on deployed website (after T047 deploys) | P1 |
| T049 | Verify site is accessible and readable without CSS/JS | P1 |
| T050 | Create Open Collective account | P1 |
| T052 | Create social media accounts (Twitter/X, Mastodon, LinkedIn) | P2 |
| T054 | Set up Bitwarden Teams vault for credential management | P0 |
| T055 | Verify MFA is enabled on all platform accounts | P0 |
| T057 | Verify current monthly infrastructure costs under $50 limit | P0 |

---

## Phase 0 Exit Criteria

Per SRS Section 13.1, Phase 0 is complete when:

- [ ] All 8 Phase 0 deliverables are at COMPLETE status
- [ ] At least 10 active contributors have registered (trigger for Phase 1)
- [ ] All human-action tasks above are resolved
- [ ] Readability check passes for all principle documents
- [ ] Link check passes across all published content
- [ ] GitHub Discussions is active and documented as exportable

---

## Notes

- The readability CI gate and link check CI gate are configured but have not yet run on a real PR. First PR against `main` will validate these workflows.
- All task-completable items in tasks.md have been implemented as of 2026-03-05 (Phase 0 initial commit).
