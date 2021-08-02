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


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict) -> int:
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
                for m in commit.modifications:
                    """ Results are for each file in the commit """
                    p = re.compile(search_for_pattern, re.M)
                    check = re.findall(p, m.diff)
                    if check:
                        print(f"\nFile name: {m.filename}")
                        print(check)
                        print(f"File path new: {m.new_path}, File path old: {m.old_path}")

                    count += len(check)
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
    for name in dict_search_patterns:
        print(f"Searching: {name}")
        start_searching(dict_search_patterns[name], name, "selection")


if __name__ == "__main__":
    main()
