# slop-skills

Shared agent skills and templates for development workflows across projects.

## Skills

| Category | Skill | Purpose |
| --- | --- | --- |
| Generic | [project-docs](skills/generic/project-docs/SKILL.md) | Keep documentation accurate and concise. |
| Generic | [project-adr](skills/generic/project-adr/SKILL.md) | Record lasting technical decisions and their rationale. |
| Generic | [project-todo](skills/generic/project-todo/SKILL.md) | Prepare and close tracked tasks. |
| Generic | [project-guidance](skills/generic/project-guidance/SKILL.md) | Maintain focused agent instructions. |
| npm | [dependency-maintenance](skills/npm/dependency-maintenance/SKILL.md) | Audit and update npm dependencies. |

Skills are grouped under `skills/<category>/<skill>/`. The CLI discovers them automatically; select them by skill name, regardless of category.

## Usage

Install with the [skills CLI](https://github.com/vercel-labs/skills) (requires Node.js and Git):

```sh
npx skills add Adri-7/slop-skills
```

Choose the skills and agents when prompted. Add `-g` to install across all your projects, or `--agent codex` to target Codex.

Update installed skills:

```sh
npx skills update
```

Skills work independently and follow the target project's conventions.

## License

[MIT](LICENSE).
