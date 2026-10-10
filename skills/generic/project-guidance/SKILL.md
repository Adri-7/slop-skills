---
name: project-guidance
description: Create, shorten, or reorganize AGENTS.md and its references when agent guidance changes. Enable only the requested documentation, ADR, or task workflows.
---

# Agent guidance

Read existing instructions and inspect only the areas relevant to the requested change.

- Enable only the requested workflows. Preserve existing paths, policies, and languages; migrate files or change global configuration only when requested.
- Keep AGENTS.md to actionable repository constraints and conditional links. Include rules that affect agent decisions, not generic advice or facts easily found in code.
- Keep one source per rule. Remove duplication, contradictions, and obsolete references without losing intentional constraints.
- Load detailed references only for the task that needs them. Do not route agents through several indexes or require reading every skill.
- For a new layout, keep AGENTS.md at the root and create only needed references under .agents/docs/, .agents/adr/, or .agents/todo/.
- Require correcting inaccurate guidance, not producing text after every edit. Add an ADR only when its rationale has lasting value, and a task only when work needs tracking.
- Define agent-content and human-documentation languages separately when needed. An English skill does not impose English output on every project.
- Keep task history and procedures out of AGENTS.md. Use specialized skills only for the artifacts needed; do not enable them all as a side effect.
- Check changed paths and links. Do not add explanatory files or usage tutorials unless requested.
