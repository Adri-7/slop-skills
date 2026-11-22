# /// script
# requires-python = ">=3.11"
# dependencies = ["skills-ref @ git+https://github.com/agentskills/agentskills.git@83021e2be457a9b6679148719c1f6074f0ad975e#subdirectory=skills-ref"]
# ///

"""Validate skill frontmatter, catalog entries, routes, and local links."""

import re
from collections import Counter
from pathlib import Path
from urllib.parse import unquote, urlsplit

from skills_ref.errors import ParseError
from skills_ref.parser import parse_frontmatter
from skills_ref.validator import validate_metadata

ROOT = Path(__file__).resolve().parents[1]
MARKDOWN_LINK = re.compile(r"\[[^\]\n]+\]\((<[^>\n]+>|[^\s)]+)(?: +\"[^\"\n]*\")?\)")
ROUTE_SKILL = re.compile(r"`([a-z0-9-]+)`")


def local_targets(document, content):
    for link in MARKDOWN_LINK.findall(content):
        target = urlsplit(link.strip("<>"))
        if not target.scheme and not target.netloc and target.path:
            yield (document.parent / unquote(target.path)).resolve()


def check_frontmatter(path, content, errors):
    try:
        metadata, _ = parse_frontmatter(content)
    except ParseError as error:
        errors.append(f"{path}: {error}")
        return

    for problem in validate_metadata(metadata, path.parent):
        errors.append(f"{path}: {problem}")


def check_catalog(path, content, skills, errors):
    listed = Counter(target for target in local_targets(path, content) if target.name == "SKILL.md")
    for skill in sorted(set(skills) | set(listed)):
        count = listed[skill]
        if skill not in skills:
            errors.append(f"{path}: unknown skill {skill}")
        elif count != 1:
            errors.append(f"{path}: expected one entry for {skill.parent.name}, found {count}")


def check_routes(path, content, skill_names, errors):
    for line_number, line in enumerate(content.splitlines(), 1):
        if not line.startswith("|"):
            continue

        columns = line.split("|")
        playbook = columns[2] if len(columns) > 2 else ""
        if "(optional external skill)" in playbook:
            continue

        for name in ROUTE_SKILL.findall(playbook):
            if name not in skill_names:
                errors.append(f"{path}:{line_number}: unknown workflow {name!r}")


def main():
    errors = []
    skills_dir = ROOT / "skills"
    skill_files = sorted(skills_dir.glob("*/*/SKILL.md"))
    names = Counter(path.parent.name for path in skill_files)
    for name, count in sorted(names.items()):
        if count > 1:
            errors.append(f"skills: duplicate skill name {name!r}")

    documents = sorted([*ROOT.glob("*.md"), *skills_dir.rglob("*.md")])
    docs = {path: path.read_text(encoding="utf-8") for path in documents}
    for path in skill_files:
        check_frontmatter(path.relative_to(ROOT), docs[path], errors)
    for document, content in docs.items():
        for target in local_targets(document, content):
            if not target.exists():
                errors.append(f"{document.relative_to(ROOT)}: broken link to {target}")

    catalog_path = skills_dir / "README.md"
    mode_path = skills_dir / "generic/azaaroth-mode/SKILL.md"
    for required in (catalog_path, mode_path):
        if required not in docs:
            errors.append(f"{required.relative_to(ROOT)}: required file missing")
    if catalog_path in docs:
        check_catalog(catalog_path, docs[catalog_path], set(skill_files), errors)
    if mode_path in docs:
        check_routes(mode_path.relative_to(ROOT), docs[mode_path], names, errors)

    if errors:
        print("\n".join(errors))
        return 1
    print(f"Validated {len(skill_files)} skills, catalog entries, routes, and local links.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
