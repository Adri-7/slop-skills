---
name: azaaroth-mode
description: "Use when the user explicitly asks to work in azaaroth-mode. Choose the playbook that fits the requested outcome and apply the target project's rules."
---

# Azaaroth mode

Read the applicable project instructions. For a substantial or ambiguous task, state the intended outcome and any assumption that could change it. Resolve routine uncertainty from the repository or a safe check.

| Requested outcome | Playbook |
| --- | --- |
| Confirm what the user wants | `in-your-own-words` |
| Resume unfinished work from a prior session or handoff | `resume-work` |
| Explain existing behavior or investigate a symptom | `investigate` |
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

Choose the most specific playbook for the requested result. Combine playbooks for distinct deliverables and carry evidence forward. For review and correction, review first, then fix confirmed findings if the request authorizes it. Use `validate-work` when a separate validation pass is requested or checks need coordination across boundaries.

Load the selected skill if available. Otherwise, follow the repository's guidance directly.
