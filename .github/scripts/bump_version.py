import os
import re
import sys


def update_file_version(file_path, version_pattern, new_version):
    """Function for update version in file.

    Args:
        file_path (_type_): _description_
        version_pattern (_type_): _description_
        new_version (_type_): _description_
    """
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()

    new_content = re.sub(version_pattern, new_version, content)

    with open(file_path, "w", encoding="utf-8") as file:
        file.write(new_content)


def update_versions(base_dir, new_version):
    """Function for update meta.yaml and __version__.py.

    Args:
        base_dir (_type_): _description_
        new_version (_type_): _description_
    """
    meta_pattern = r'{% set version = ".*?" %}'
    version_py_pattern = r'__version__ = ".*?"'

    for root, _, files in os.walk(base_dir):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            if file_name == "meta.yaml":
                update_file_version(
                    file_path, meta_pattern, f'{{% set version = "{new_version}" %}}'
                )
                print(f"Updated: {file_path}")
            elif file_name == "__version__.py":
                update_file_version(
                    file_path, version_py_pattern, f'__version__ = "{new_version}"'
                )
                print(f"Updated: {file_path}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Using: python bump_version.py <new_version>")
        sys.exit(1)

    new_version = sys.argv[1]
    base_directory = os.getcwd()
    update_versions(base_directory, new_version)
