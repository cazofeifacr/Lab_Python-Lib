#!/usr/bin/env python3

import subprocess
import sys
import os


def get_changed_files():
    """Get the list of files changed in the current commit."""
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout.splitlines()


def find_subdirectory_readmes():
    """Find all README.md files in subdirectories."""
    sub_readmes = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower() == "readme.md" and root != ".":
                sub_readmes.append(os.path.join(root, file))
    return sub_readmes


def check_readme_sync():
    """
    Check if README.md in subdirectories is modified without
    updating the root README.md."""
    changed_files = get_changed_files()
    sub_readmes = find_subdirectory_readmes()

    sub_readme_changes = [readme for readme in sub_readmes if readme in changed_files]

    root_readme_changed = "README.md" in changed_files

    if sub_readme_changes and not root_readme_changed:
        print(
            "Error: Changes detected in the following README.md files \
            in subdirectories:"
        )
        for readme in sub_readme_changes:
            print(f"  - {readme}")
        print("But no changes were detected in the root README.md.")
        sys.exit(1)

    print("README.md validation passed.")
    sys.exit(0)


if __name__ == "__main__":
    check_readme_sync()
