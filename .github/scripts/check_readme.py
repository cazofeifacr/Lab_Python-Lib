#!/usr/bin/env python3

import os
import subprocess


def get_last_commit_hash(file_path):
    """Get the last commit hash for a given file."""
    result = subprocess.run(
        ["git", "log", "-n", "1", "--pretty=format:%H", "--", file_path],
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()


def find_readme_files():
    """Find all README.md files in subdirectories."""
    readme_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower() == "readme.md" and root != ".":
                readme_files.append(os.path.join(root, file))
    return readme_files


def check_readme_updated():
    """Check if the root README.md is updated based on other README.md files.

    Raises:
        Exception: If the root README.md is not updated.
    """
    root_readme_last_commit = get_last_commit_hash("README.md")
    readmes_to_monitor = find_readme_files()

    for readme in readmes_to_monitor:
        readme_last_commit = get_last_commit_hash(readme)
        if readme_last_commit > root_readme_last_commit:
            raise Exception(f"Root README.md is not updated for changes in {readme}")

    print("Root README.md is up to date.")


if __name__ == "__main__":
    check_readme_updated()
