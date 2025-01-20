#!/usr/bin/env python3

import subprocess
import sys
import os


def get_last_commit_hash(file_path):
    result = subprocess.run(
        ["git", "log", "-n", "1", "--pretty=format:%H", "--", file_path],
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").strip()


def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        stdout=subprocess.PIPE,
    )
    return result.stdout.decode("utf-8").splitlines()


def find_readme_files():
    readme_files = []
    for root, dirs, files in os.walk("."):
        for file in files:
            if file.lower() == "readme.md" and root != ".":
                readme_files.append(os.path.join(root, file))
    return readme_files


def check_readme_sync():
    changed_files = get_changed_files()

    subdir_readmes = find_readme_files()

    for readme in subdir_readmes:
        if readme in changed_files:
            root_readme_commit = get_last_commit_hash("README.md")
            subdir_readme_commit = get_last_commit_hash(readme)

            if subdir_readme_commit != root_readme_commit:
                print(f"Error: Check file README.md {readme}")
                sys.exit(1)

    print("All files README.md are synced.")


if __name__ == "__main__":
    check_readme_sync()
