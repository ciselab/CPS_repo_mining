#!/usr/bin/env python
"""
Tryout of PyDriller for remote & local repositories.
Focus on the content of commit messages.
"""
import glob
import os
import pathlib
import re
import sys
from pydriller import RepositoryMining
from pydriller.domain.commit import Commit
import pd.dict_repo_list
from pd.key_list import keyword_list
from typing import Optional

location_sourcefile = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results", "resultsOutput.txt")
dir_projects = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results", "repo")


def print_repository_info(project: str, location: str):
    """
    Print information about current run

    Args:
        project: Name project
        location: Repository url
    """
    try:
        sourcefile = open(location_sourcefile, 'a')
        print(f"Name: {project}", file=sourcefile)
        print(f"Repository: {location}", file=sourcefile)
        print(f"Searching for: {keyword_list}", file=sourcefile)
        sourcefile.close()
    except FileNotFoundError:
        print("File to print repository information does not exist.")


def print_commit_header(commit: Commit):
    """
    Print information about the commit

    Args:
        commit: The full commit.
    """
    try:
        sourcefile = open(location_sourcefile, 'a')
        print(f"\nhash: {commit.hash}\ndate: {commit.committer_date}\nmessage: {commit.msg}", file=sourcefile)
        print(f"modified file(s): {commit.files}", file=sourcefile)
        sourcefile.close()
    except FileNotFoundError:
        print("File to print commit header does not exist.")

    """ Ready for search_selection.py """
    project_name = commit.project_name
    if not os.path.exists(os.path.abspath(dir_projects)):
        os.makedirs(dir_projects)
    file_name = str(project_name + '.txt')
    project_file_name = os.path.join(dir_projects, file_name)
    try:
        hash_file = open(project_file_name, 'a')
        print(f"{commit.hash}", file=hash_file)
        hash_file.close()
    except FileNotFoundError:
        print("Hash file does not exist.")


def choose_repository(option: str) -> Optional[dict]:
    """
    Choose which repositories to use.

    Args:
        option: Choice for local or remote repository.
                Value behind l/r to choose which repository from the list.
                Possible to choose all local/remote repositories.

    Returns:
        The repository project(s) selection with location for the given option.
        Or None is returned, in case the input is not according to expectation.
    """
    projects = {}
    if len(option) < 1 or not pd.dict_repo_list.projects:
        print_help()
        return None
    repo_choice = option[0]
    full_choice_desc = {"l": "local", "r": "remote"}
    if re.fullmatch(r"[lr]([1-9][0-9]*)", option):
        """ Selection of repositories """
        n = int(option.replace(repo_choice, ''))
        projects_list = list(pd.dict_repo_list.projects.keys())
        if n > len(projects_list):
            print_help()
            return None
        project_selection = projects_list[n - 1]
        projects = {project_selection: pd.dict_repo_list.projects[project_selection][full_choice_desc[repo_choice]]}
    elif option == "ra" or option == "la":
        """ All remote repositories """
        for project in pd.dict_repo_list.projects:
            projects.update({project: pd.dict_repo_list.projects[project][full_choice_desc[repo_choice]]})
    else:
        print_help()
        return None
    print(f"Keywords: {keyword_list}")
    return projects


def dig(project: str, url: str) -> int:
    """
    Starts the mining process on the repository indicated by the given URL

    Args:
        project: Name project
        url: Url of chosen repository.

    Returns:
        Number of commits and list of commit hashes.
    """
    mine = RepositoryMining(url)
    number_of_commits = 0

    for commit in mine.traverse_commits():
        for keyword in keyword_list:
            if re.search(r"\b" + keyword.lower() + r"\b", commit.msg.lower()):
                """ Ignore merge pull request commits """
                if commit.modifications:
                    print_commit_header(commit)
                    number_of_commits += 1
                    try:
                        sourcefile = open(location_sourcefile, 'a')
                        print(f"First found keyword: {keyword}", file=sourcefile)
                        sourcefile.close()
                    except FileNotFoundError:
                        print("File for commit information, to add keyword list, does not exist.")
                for modified_file in commit.modifications:
                    try:
                        sourcefile = open(location_sourcefile, 'a')
                        print(f">>> {modified_file.filename}", file=sourcefile)
                        sourcefile.close()
                    except FileNotFoundError:
                        print("File for commit information, to add list of files, does not exist.")
                break
    print(f"{project}: {number_of_commits}")
    return number_of_commits


def user_input_is_valid(user_input: str) -> bool:
    """
    User input validation.

    Args:
        user_input: Input the user has given for running against which repositories.

    Returns:
        If the user input matches the possible options.
    """
    if re.fullmatch(r"[lr]([1-9][0-9]*|[a])", user_input):
        return True
    else:
        print_help()
        return False

 
def restart_results_file(check_file: str):
    """
    Check if a file exists and remove this file.

    Args:
        check_file: File to check, remove if exists.

    """
    if os.path.isfile(check_file):
        os.remove(check_file)


def remove_files_in_dir(check_dir: str):
    """
    Remove all files in dir, keep dir.

    Args:
        check_dir: Dir to check for files.
    """
    files_location = glob.glob(os.path.join(check_dir, "*"))
    files = files_location
    for f in files:
        try:
            os.remove(f)
        except OSError as e:
            print(f"Error: {f}, {e.strerror}")


def main(user_input: list = None):
    """
    Main entry point when run as script

    Args:
        user_input: argv[1]: Input from user, local vs remote repository.<br/>
        [lx] = local, [rx] = remote: where x is the number in the list;
        [ra] = all remote repositories;
        [la] = all local repositories.
    """
    restart_results_file(os.path.join(pathlib.Path.home(), "CPS_repo_mining", "resultsOutput.txt"))
    remove_files_in_dir(os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results", "repo"))

    pd.dict_repo_list.build_repo_dict()

    if not user_input:
        user_input = sys.argv
    if len(user_input) > 1:
        print(f"Input: {user_input[1:]}")
        dir_location = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results")
        if not os.path.exists(os.path.abspath(dir_location)):
            os.makedirs(dir_location)
        try:
            sourcefile = open(location_sourcefile, 'w')
            print(f"Start with input: {user_input[1:]}", file=sourcefile)
            sourcefile.close()
        except OSError as e:
            print(f"Error: {location_sourcefile}, {e.strerror}")
        if user_input_is_valid(user_input[1]):
            projects = choose_repository(user_input[1])
            for project in projects:
                print_repository_info(project, projects[project])
                dig(project, projects[project])
    else:
        print_help()


def print_help():
    """
    Print help text for wrong user input.
    """
    print("Expected: [lx] for local, [rx] for remote")
    print("Where x can be a number for selecting a repository, or 'a' for all of that type.")
    print(f"Maximum length: {len(pd.dict_repo_list.projects)}")


if __name__ == "__main__":
    main()
