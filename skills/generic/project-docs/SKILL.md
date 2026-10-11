---
name: project-docs
description: Write or shorten repository documentation when requested, or correct guidance made inaccurate by a change. Excludes ADRs, task files, and AGENTS.md.
---

# Project documentation

Read applicable AGENTS.md and only the affected references. Follow local paths and language policy; otherwise preserve the document's language.

## Decide what belongs

- Unless requested, add information only if it enables a concrete action, prevents a likely mistake, or explains a necessary constraint missing from current guidance. Leaving documentation unchanged is a valid outcome.
- Verify facts against code, configuration, or authoritative sources. Distinguish planned behavior from implemented behavior.
- Update the existing source. Create a document only for a distinct need or to extract a topic that benefits from separate reading. Do not document code that is already clear to the intended reader.

## Edit minimally

- State the useful fact or action directly, with precise names and short sentences.
- Preserve necessary prerequisites, exceptions, and limitations. Use examples only to remove ambiguity.
- With each edit, simplify the sections you touch: remove repetition, introductions, generic advice, and obsolete text; merge overlapping instructions. Replace affected text rather than append a change log. Keep cleanup within the affected sections unless a broader rewrite is requested.
- Keep one source per fact; link instead of copying. If a document becomes hard to navigate because of its length, move self-contained topics into focused files when useful, leaving concise summaries and links so the original becomes readable again.
- Before finishing, reread the changed sections and cut anything that adds length without helping the reader act or understand a necessary constraint.
- Check changed links and documented commands without starting services or mutating data just to verify prose. Do not create tasks or ADRs as a side effect.
