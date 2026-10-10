---
name: dependency-maintenance
description: Audit and update npm dependencies, fix dependency vulnerabilities, or handle Dependabot updates with necessary migrations and repository validation.
---

# Dependency maintenance

## Inspect

- Follow repository guidance. Read `package.json`, the lockfile, and `.npmrc`; preserve existing user changes.
- Read relevant dated dependency decisions in the target project's `.agents/dependencies/`; the latest decision for each package supersedes earlier entries.
- Use the project's package manager and pinned Node/npm versions. Check `npm outdated --json` and `npm audit --json`; a nonzero exit can indicate findings rather than a command failure.
- For audit-only requests, report findings without editing files. For updates, stay within the requested packages or Dependabot change.

## Update

- When scope is unspecified, prefer stable patch and minor updates in small coherent batches. Handle majors separately; consult official release notes and migration guides, check engines and peer dependencies, and implement migrations when requested.
- Keep related packages compatible, especially Prisma client/adapter/CLI and Vitest/coverage/UI. Semver compatibility alone does not guarantee a harmless update.
- Prefer targeted updates over updating everything to `latest`. Preserve version-range conventions and the lockfile; inspect the diff for unrelated changes.
- For vulnerabilities, inspect the advisory and dependency path (`npm explain <package>`). Prefer updating the introducing dependency; use a narrow override only with a compatibility check and a recorded reason. Review existing overrides for removal when no longer needed.
- Do not use `npm audit fix --force` or `--legacy-peer-deps` to bypass incompatibilities. Review newly required install scripts before changing permissions.
- Investigate unused dependencies or bundle size only when relevant or requested. Confirm actual usage before removing a package, including Nuxt auto-imports, modules, configuration, and scripts.

## Validate and report

- Follow the project's validation rules and run a production build when build or runtime dependencies change. Verify a lockfile-based clean install in an isolated environment when needed to check reproducibility.
- If a batch fails, fix within scope or undo only your changes for that batch. Do not weaken checks; distinguish pre-existing failures from regressions.
- Summarize versions changed, migrations, validation results, and unresolved vulnerabilities or deferred updates with reasons. State checks that could not run.
- Dependabot handles recurring monitoring; do not add another scheduler or change its configuration unless requested.

## Decision record

When changing overrides or deferring updates, use `.agents/dependencies/YYYY-MM-DD-topic.md` with today's date and a short topic in kebab-case, following the [template](assets/dependency-decisions-template.md). Update the existing file for the same date and topic; keep older records. Record decisions only, without a work log.
