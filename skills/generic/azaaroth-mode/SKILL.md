---
name: azaaroth-mode
description: "Choose or combine engineering workflows for open-ended repository tasks. Use when work needs coordination across steps such as investigation, design, implementation, review, and verification, including project setup, maintenance, or resuming unfinished work. Also use when the user asks for azaaroth-mode."
---

# Azaaroth mode

Read the applicable project instructions. For a substantial or ambiguous task, state the intended outcome and any assumption that could change it. Resolve routine uncertainty from the repository or a safe check.

| Requested outcome | Playbook |
| --- | --- |
| Confirm what the user wants | `in-your-own-words` |
| Resume unfinished work from a prior session or handoff | `resume-work` |
| Explain existing behavior or investigate a symptom | `investigate` |
| Check a TLA+ state model or visualize a counterexample | `statechart` (optional external skill) |
| Restore expected behavior | `fix-bug` |
| Add a capability or intentionally change behavior | `implement-feature` |
| Refactor while preserving behavior | `minimal-change` |
| Choose an architecture or address a concrete design problem | `architecture-improvement` |
| Adopt the framework in a repository | `setup-project` |
| Add or maintain project verification rules, tools, or instructions | `project-verification` |
| Validate a change or existing diff | `validate-work` |
| Review a diff or PR | `review-code` |
| Learn from recent project chats | `improve-workflow` |
| Maintain agent instructions, human-facing docs, task files, or decision records | `project-guidance`, `project-docs`, `project-todo`, or `project-adr` |
| Audit, review, or update npm dependencies | `dependency-maintenance` |

Choose the most specific playbook for the requested result. Combine playbooks for distinct deliverables and carry evidence forward. For review and correction, review first, then fix confirmed findings if the request authorizes it. Use `validate-work` when a separate validation pass is requested or checks need coordination across boundaries. For performance objectives, use it before editing to capture the baseline.

After implementation, use `review-code` in independent mode for material changes to persisted data, concurrency, migrations, or public contracts, or when requested or required by the project. If `review-code` is unavailable, report the missing independent pass.

Load the selected skill if available. Otherwise, follow the repository's guidance directly. For statecharts, use the project's model checker when available and label a source-based diagram as such.
