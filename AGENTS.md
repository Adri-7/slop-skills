# Repository guidance

Keep shared skills simple, precise, and effective. Minimize the context needed to use them.

## Organization

- Store skills in `skills/<category>/<skill-name>/SKILL.md`. Use `generic` for cross-stack workflows and technology names such as `npm` for specific ones.
- Keep names unique across categories. Match the folder name to the frontmatter `name`, using kebab-case.
- Keep each workflow usable on its own. A mode can route to installed skills by name and fall back to repository guidance.
- Keep supporting files inside that skill. Use `references/` for detail read only under a named condition and `assets/` for files copied or adapted into a deliverable.
- Add a `scripts/` helper when deterministic execution saves repeated work or improves reliability. Prefer existing tools. Document invocation, dependencies, and side effects.

## Writing

- Write skills in English. Give each skill one clear responsibility; its `description` must say when to use it and clarify likely overlaps.
- Use short, actionable instructions. Keep only rules that affect decisions or prevent concrete mistakes; omit introductions, repetition, and obvious advice.
- Keep the main workflow in `SKILL.md`. Link supporting resources directly from `SKILL.md` using relative paths and say when to use them.
- Follow the target project's conventions. Resolve bundled resources relative to the installed skill.

## Changes

- Edit existing instructions instead of appending exceptions or history. Remove obsolete and duplicate rules; preserve useful constraints.
- Add detail only to solve a concrete need. Prefer simplifying a skill before adding files or splitting it.
- Preserve skill names unless a rename is requested. Update affected README entries and links when names, paths, or scope change.
- Before finishing changes to skills, their resources, the skill catalog, or the validator, run `uv run --script scripts/validate_skills.py` from the repository root. Exercise any other changed script on a representative case. Documentation-only edits need no new tests or tracking files.
