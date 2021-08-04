#!/usr/bin/env python
"""
Searching trough the diffs of each commit
"""
import re
from pydriller import RepositoryMining
import pd.dict_repo_list
from graph_creation import create_graph
from utils import build_results_path
from utils import list_file_content
import os
import pathlib
from typing import Optional

"""Change this location if the results should be printed or found elsewhere."""
location_results_dir = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results")
location_results_file = os.path.join(location_results_dir, "resultsOutputSelection.txt")
location_repo_results_dir = os.path.join(location_results_dir, "repo")


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict) -> Optional[int]:
    """
    Starts the mining process on the repository indicated by the given URL
    Uses list of hashes from previous selection script.

    Args:
        key_project: Project name from the dictionary.
        search_for_pattern: Pattern to find in the code to occur.
        repo_dictionary: Dictionary of with the project name and local location.

    Returns:
        count: How often the keyword occurs in the code of specified project.
    """
    url = repo_dictionary[key_project]["local"]
    hash_file_location = build_results_path(key_project)

    count = 0

    if hash_file_location:
        list_of_hashes_project = list_file_content(hash_file_location)

        for each_hash in list_of_hashes_project:
            stripped_each_hash = str.rstrip(each_hash)
            for commit in RepositoryMining(url, single=stripped_each_hash).traverse_commits():
                reset = True
                for m in commit.modifications:
                    """ Results are for each file in the commit """
                    p = re.compile(search_for_pattern, re.M)
                    check = re.findall(p, m.diff)
                    if check:
                        if reset:
                            try:
                                results_file = open(location_results_file, 'a')
                                print(f"\nCommit hash: {commit.hash}", file=results_file)
                                results_file.close()
                            except FileNotFoundError:
                                print("File to print results does not exist.")
                            reset = False
                        try:
                            results_file = open(location_results_file, 'a')
                            print(f"\nFile name: {m.filename}", file=results_file)
                            print(check, file=results_file)
                            print(f"File path new: {m.new_path}, File path old: {m.old_path}", file=results_file)
                            results_file.close()
                        except FileNotFoundError:
                            print("File to print results does not exist.")

                    count += len(check)
    else:
        print(f"No file found for project: {key_project}")
        return None
    return count


def start_searching(search_for_pattern: str, title_graph: str, search_type: str):
    """
    Gather data to generate a graph with the results.

    Args:
        search_for_pattern: Pattern to search through the code for.
        title_graph: Name for the resulting graph.
        search_type: This script is using a selection of commits to search through.

    """
    data_graph = {}
    pd.dict_repo_list.build_repo_dict()
    repo_dictionary = pd.dict_repo_list.projects
    for key_repo_name in repo_dictionary.keys():
        counted = dig_for_code(key_repo_name, search_for_pattern, repo_dictionary)
        if counted:
            print(f"{key_repo_name}: {counted}")
            if counted > 0:
                data_graph[key_repo_name] = counted
    if data_graph:
        create_graph(data_graph, title_graph, search_type)


def main():
    """
    Main function; containing a dictionary with the regex search pattern.
    Which will be used to search trough the code later.
    dictionary = {Name graph : regex pattern}
    """
    dict_search_patterns = {
        "selection sleep add": r'^(\+)(.*)(sleep\()',
        "selection sleep remove": r'^(\-)(.*)(sleep\()',
    }
    if os.path.exists(location_repo_results_dir):
        if os.listdir(location_repo_results_dir):
            print("Start analysis.")
            try:
                results_file = open(location_results_file, 'w')
                print(f"Running search_selection.py", file=results_file)
                print(f"Patterns: {dict_search_patterns}", file=results_file)
                results_file.close()
            except OSError as e:
                print(f"Error: {location_results_file}, {e.strerror}")
            for name in dict_search_patterns:
                try:
                    results_file = open(location_results_file, 'a')
                    print(f"Searching: {name}", file=results_file)
                    results_file.close()
                except FileNotFoundError:
                    print("File to print results does not exist.")
                print(f"Searching: {name}")
                start_searching(dict_search_patterns[name], name, "selection")
        else:
            print("No files found in the repo directory to analyse.")
    else:
        print("Directory with repository results does not exist.")


if __name__ == "__main__":
    main()
