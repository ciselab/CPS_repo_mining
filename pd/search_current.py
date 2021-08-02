#!/usr/bin/env python
"""
Searching through the diffs of each commit
"""
import os
import re
from chardet.universaldetector import UniversalDetector
import pd.dict_repo_list
from datetime import datetime
from graph_creation import create_graph


def dig_for_code(key_project: str, search_for_pattern: str, repo_dictionary: dict) -> int:
    """
    Starts the mining process on the repository indicated by the given URL
    Through the current state of the repository. Only looking at files with specified extensions.

    Args:
        key_project: Project name from the dictionary.
        search_for_pattern: Pattern to find in the code to occur.
        repo_dictionary: Dictionary of with the project name and local location.

    Returns:
        count: How often the keyword occurs in the code of specified project.
    """
    url = repo_dictionary[key_project]["local"]
    count = 0

    p = re.compile(search_for_pattern, re.M)
    for root, directories, files in os.walk(url):
        for name in files:
            file = os.path.join(root, name)

            file_name, file_extension = os.path.splitext(file)
            # noinspection SpellCheckingInspection
            search_in_ext = ['.c', '.cpp', '.h', '.hpp', '.cxx', '.hxx', '.cc', '.hh', '.h++',
                             '.ipp', '.inl', '.txx', '.tpp', '.tpl',
                             '.c++m', '.cppm', '.cxxm', '.kt',
                             '.java', '.go', '.py', '.rb', '.rs',
                             '.scala', '.sc', '.swift', '.js', '.ts', '.tsx', '.sh']

            if file_extension.lower() in search_in_ext:
                try:
                    content_file = open(file, 'r')
                    for line in content_file:
                        check = re.findall(p, line)
                        count += len(check)
                    content_file.close()
                except UnicodeDecodeError:
                    """
                    Some files are using an encoding that cannot be immediately read.
                    Most of these files, seem to be using Windows-1252 encoding.
                    To keep the duration of this script as short as possible, this encoding will be tried first.
                    """
                    try:
                        enc = 'Windows-1252'
                        content_file = open(file, 'r', encoding=enc)
                        for line in content_file:
                            check = re.findall(p, line)
                            count += len(check)
                        content_file.close()
                    except UnicodeDecodeError:
                        """
                        When the Windows-1252 encoding is not correct, chardet is being used.
                        This tool tries to detect which encoding is used.
                        """
                        try:
                            rd_file = open(file, "rb")
                            raw_data = rd_file.readlines()
                            detector = UniversalDetector()
                            for rd_line in raw_data:
                                detector.feed(rd_line)
                                if detector.done:
                                    break
                            detector.close()
                            rd_file.close()
                            if detector.result:
                                enc = detector.result["encoding"]
                                if enc:
                                    print(f"encoding: {enc}")
                                    content_file = open(file, 'r', encoding=enc)
                                    for line in content_file:
                                        check = re.findall(p, line)
                                        count += len(check)
                                    content_file.close()
                                else:
                                    print("No encoding result.")
                            else:
                                print("No Result from detector.")
                        except UnicodeDecodeError:
                            """
                            In case chardet is not able to detect which encoding was used.
                            """
                            print(f"UnicodeDecodeError: {file}")
                        except Exception as e:
                            print(f"Different error encountered: {file}, error: {e}")
                except Exception as e:
                    print(f"Different error encountered: {file}, error: {e}")
    return count


def start_searching(search_for_pattern: str, title_graph: str, search_type: str):
    """
    Start the search with received pattern.

    Args:
        search_for_pattern: Pattern to search with in this current round.
        title_graph: Title connected to the search pattern.
        search_type: Searching through the current state of the repository.
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
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"Start time: {current_time}")

    dict_search_patterns = {
        "sleep function": r'^(.*)(sleep\()',
        "Sleep function": r'^(.*)(Sleep\()',
        "sleep_for": r'^(.*)(sleep_for)',
        "setTimeout": r'^(.*)(setTimeout)',
        "sleep space": r'^(.*)(sleep" ")',
    }
    for name in dict_search_patterns:
        print(f"Searching: {name}")
        start_searching(dict_search_patterns[name], name, "current")

    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print(f"End time: {current_time}")


if __name__ == "__main__":
    main()
