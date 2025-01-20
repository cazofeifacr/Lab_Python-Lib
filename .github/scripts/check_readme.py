#!/usr/bin/env python3

import subprocess
import sys


def get_changed_files():
    result = subprocess.run(
        ["git", "diff", "--cached", "--name-only"],
        stdout=subprocess.PIPE,
        text=True,
    )
    return result.stdout.splitlines()


def check_readme_sync():
    changed_files = get_changed_files()

    sub_readme_changed = "my_hw/README.md" in changed_files

    root_readme_changed = "README.md" in changed_files

    if sub_readme_changed and not root_readme_changed:
        print(
            "Error: Cambios detectados en my_hw/README.md \
            pero no en README.md en la raíz."
        )
        sys.exit(1)

    print("Validación de README.md pasada.")
    sys.exit(0)


if __name__ == "__main__":
    check_readme_sync()
