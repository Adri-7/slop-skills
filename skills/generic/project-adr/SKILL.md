---
name: project-adr
description: Write or supersede an ADR when requested or when a lasting technical choice needs its rationale preserved. Excludes routine implementation notes and general documentation.
---

# Architecture decisions

Read local ADR conventions and only related decisions. Follow existing paths, numbering, statuses, and language policy.

## Decide whether a record is useful

Unless requested, create an ADR only for a lasting choice whose non-obvious trade-off or constraint a future maintainer needs to understand. Routine refactors, obvious implementation choices, and dependency updates alone do not justify a record. Reuse an existing record when clarifying the same proposal; do not create one per change.

## Write the record

- Use the local template, or adapt the bundled [template](assets/adr-template.md) when creating or restructuring a record.
- Keep the determining context, the decision and its reason, and practical consequences. Include alternatives only when they explain the choice.
- Do not copy architecture documentation, narrate the discussion, invent rationale, or fill empty sections. State material uncertainty.
- Mark a decision accepted only when the user or project evidence establishes acceptance.
- To supersede an accepted decision, retain its rationale, create the replacement, and link both ways. Correct factual errors without rewriting history.
- Check numbering and links; update an existing index if required. Change current guidance only where the decision makes it inaccurate. Do not initialize other workflows.
