#!/usr/bin/env python
"""
Common for utils.
"""
from os import path
from typing import Optional
import pathlib

location = path.join(pathlib.Path.home(), "CPS_repo_mining", "results", "repo")


def build_results_path(project: str) -> [str, Optional]:
    """
    Building the path to where the results file should be, checks if exists.

    Args:
        project: Name of the project.

    Returns:
        - Path to the project results file (containing commit hashes).
        - None if path does not exists.

    """
    project_name = str(project + '.txt')
    hash_file_location = path.join(location, project_name)
    if path.exists(hash_file_location):
        return hash_file_location
    else:
        return None


def list_file_content(file_location: str) -> list:
    """
    Reads the file and converts the content to a list, an entry for each line.

    Args:
        file_location: Location of the file.

    Returns:
        list_content_file: List of content read from the file.

    """
    list_content_file = []
    content_file = open(file_location, 'r')
    for line in content_file:
        list_content_file.append(line)
    content_file.close()
    return list_content_file
