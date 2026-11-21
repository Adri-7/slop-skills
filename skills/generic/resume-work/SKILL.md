---
name: resume-work
description: "Resume an unfinished task from a previous chat, handoff, task record, branch, or worktree. Reconstruct the current state and continue the remaining work."
---

# Resume work

1. Recover the original goal and the latest relevant handoff or task record. Read only the history for this task when available, starting with the last checkpoint and decisions. If the record is missing, reconstruct what you can from the repository and state any material uncertainty.
2. Confirm the branch and worktree when applicable. Compare commits, the working diff, and affected files with the handoff. Preserve in-flight edits and identify what is complete, pending, or blocked.
3. Reuse prior results when the evidence still applies to the current code, configuration, and inputs. Rerun checks affected by later changes or needed to establish an unverified claim.
4. Continue from the first unfinished step under the project's rules. For a status-only request, report the resume point, relevant evidence, and blockers.
