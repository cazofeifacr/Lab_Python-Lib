#!/usr/bin/env python3

import subprocess
import sys


def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"], stdout=subprocess.PIPE
    )
    return result.stdout.decode("utf-8").splitlines()


def main():
    changed_files = get_changed_files()
    readme_file_changed = any("README.file" in file for file in changed_files)
    readme_md_changed = "README.md" in changed_files

    if readme_file_changed and not readme_md_changed:
        print("Error: README.md in the root directory has not been modified.")
        sys.exit(1)

    sys.exit(0)


if __name__ == "__main__":
    main()
