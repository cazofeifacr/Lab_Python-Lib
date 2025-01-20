#!/usr/bin/env python3

import os
import sys
from pathlib import Path


def check_readme_changes():
    root_readme = Path("README.md")
    if not root_readme.exists():
        print("Error: Root README.md does not exist")
        sys.exit(1)

    root_readme_time = os.path.getmtime(root_readme)

    has_subdir_changes = False
    changed_readmes = []

    for root, dirs, files in os.walk("."):
        if root == ".":
            continue

        if "dist" in root or ".git" in root:
            continue

        if "README.md" in files:
            subdir_readme = Path(root) / "README.md"
            subdir_time = os.path.getmtime(subdir_readme)

            if subdir_time > root_readme_time:
                has_subdir_changes = True
                changed_readmes.append(str(subdir_readme))

    if has_subdir_changes:
        print(
            "Error: The following README.md files have been modified \
                without updating the root README.md"
        )
        for readme in changed_readmes:
            print(f"  - {readme}")
        sys.exit(1)
    else:
        print("OK: No subdirectory README.md files found newer than root README.md")
        sys.exit(0)


if __name__ == "__main__":
    check_readme_changes()
