#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Expanded idea from: Tracking issue - Windows handling of unicode is buggy
# [#3890](https://github.com/pypy/pypy/issues/3890)

import fnmatch
import os
import os.path
import sys
import time
from datetime import datetime
from tabulate import tabulate

dir_names = [b"fi\xc5\x9fier.dir", u"fi\u00c5\u009fier.dir", "fişier.dir"]
# expected in all cases: fişier.dir

base_path: str = os.path.dirname(os.path.abspath(__file__))


# function to transform to StrOrBytesPath
def to_str_or_bytes_path(path) -> str:
    if isinstance(path, bytes):
        return path.decode("utf-8")
    return path


def always_create_dir(targetDir):
    global base_path

    targetDirPath = os.path.join(base_path, targetDir)
    if os.path.exists(targetDirPath):
        print(f"Deleting existing directory: '{targetDir}'")
        os.rmdir(targetDirPath)
    else:
        print(f"Directory '{targetDir}' was not detected.")
    try:
        print(f"Creating directory: '{targetDir}'")
        os.mkdir(targetDirPath)
    except FileExistsError:
        print(f"Directory '{targetDir}' already exists, so it was not created.", "\n")


def find_directories_with_prefix(prefix: str) -> set[str]:
    global base_path
    foundDirectories: set[str] = set()

    for _, dirs, _ in os.walk(base_path):
        for dir in fnmatch.filter(dirs, f"{prefix}*"):
            foundDirectories.add(dir)
    return foundDirectories


def get_datetimes_dir(folder: str) -> list[str]:
    global base_path
    folder_timestamps: list[str] = []

    folder_path = os.path.join(base_path, folder)
    # creation time
    folder_timestamps.append(
        datetime.fromtimestamp(os.path.getctime(folder_path)).isoformat(" ")
    )
    # modification time
    folder_timestamps.append(
        datetime.fromtimestamp(os.path.getmtime(folder_path)).isoformat(" ")
    )
    return folder_timestamps


if __name__ == "__main__":
    print(f"Python version: {sys.version}", "\n")

    for name in dir_names:
        folder_data: list[list[str]] = []
        name = to_str_or_bytes_path(name)
        always_create_dir(name)
        dirs = find_directories_with_prefix("fi")
        for dir in dirs:
            data: list[str] = [dir]  # create new list with directory name
            data.extend(get_datetimes_dir(dir))  # add the creation and modify datetime of it
            folder_data.append(data)
        print(tabulate(
            folder_data,
            headers=["Dir status", "Creation time", "Modification time"],tablefmt="github"))
        print()
        time.sleep(1)
