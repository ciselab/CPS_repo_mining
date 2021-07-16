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


def print_repository_info(url: str):
    """
    Print information about current run

    Args:
        url: Repository url
    """
    sourcefile = open(location_sourcefile, 'a')
    print(f"Repository: {url}", file=sourcefile)
    print(f"Searching for: {keyword_list}", file=sourcefile)
    sourcefile.close()


def print_commit_header(commit: Commit):
    """
    Print information about the commit

    Args:
        commit: The full commit.

    Returns:
        The commit hash.
    """
    sourcefile = open(location_sourcefile, 'a')
    print(f"\nhash: {commit.hash}\ndate: {commit.committer_date}\nmessage: {commit.msg}", file=sourcefile)
    print(f"modified file(s): {commit.files}", file=sourcefile)
    sourcefile.close()

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
        print("File does not exist.")


def repository_from_list(location: list, n: int) -> Optional[list]:
    """
    Use a list of repositories for selecting a single repository.

    Args:
        location: List of repositories, can be the local or remote list.
        n: Place number of the repository in the list.

    Returns:
        One URL from the given list of urls.
    """
    if (n >= 1) and (n <= len(location)):
        url = [location[n - 1]]
    else:
        if not location:
            print("Empty list of repositories.")
        else:
            print(f"Invalid option, out of range, options 1 to {len(location)}.")
        return None
    return url


def choose_repository(option: str) -> Optional[list]:
    """
    Choose which repositories to use.

    Args:
        option: Choice for local or remote repository.
                Value behind l/r to choose which repository from the list.
                Possible to choose all remote repositories.

    Returns:
        The repository URL(s) for the given option.
    """
    if re.fullmatch(r"[r]([1-9][0-9]*)", option):
        """ Remote repository """
        n = int(option.replace('r', ''))
        remote_dict_repo = pd.dict_repo_list.build_repo_dict(type_remote=True)
        if not remote_dict_repo:
            print_help()
            return None
        url_list = list(remote_dict_repo.values())
        urls = repository_from_list(url_list, n)
        if not urls:
            print_help()
            return None
    elif option == "ra":
        """ All remote repositories """
        remote_dict_repo = pd.dict_repo_list.build_repo_dict(type_remote=True)
        if not remote_dict_repo:
            print_help()
            return None
        urls = list(remote_dict_repo.values())
    elif option == "la":
        """ All local repositories """
        local_dict_repo = pd.dict_repo_list.build_repo_dict()
        if not local_dict_repo:
            print_help()
            return None
        urls = list(local_dict_repo.values())
    elif re.fullmatch(r"[l]([1-9][0-9]*)", option):
        """ Local repository """
        n = int(option.replace('l', ''))
        local_dict_repo = pd.dict_repo_list.build_repo_dict()
        if not local_dict_repo:
            print_help()
            return None
        url_list = list(local_dict_repo.values())
        urls = repository_from_list(url_list, n)
        if not urls:
            print_help()
            return None
        if not os.path.exists(os.path.expanduser(urls[0])):
            print(f"Path {urls[0]} does not exist.")
            return None
    else:
        print_help()
        return None
    print(f"URL: {urls}")
    return urls


def dig(url: str) -> int:
    """
    Starts the mining process on the repository indicated by the given URL

    Args:
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
                    sourcefile = open(location_sourcefile, 'a')
                    print(f"First found keyword: {keyword}", file=sourcefile)
                    sourcefile.close()
                for modified_file in commit.modifications:
                    sourcefile = open(location_sourcefile, 'a')
                    print(f">>> {modified_file.filename}", file=sourcefile)
                    sourcefile.close()
                break
    print(f"Number of commits: {number_of_commits}")
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

    if not user_input:
        user_input = sys.argv
    if len(user_input) > 1:
        print(f"Input: {user_input[1:]}")
        dir_location = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results")
        if not os.path.exists(os.path.abspath(dir_location)):
            os.makedirs(dir_location)
        sourcefile = open(location_sourcefile, 'w')
        print(f"Start with input: {user_input[1:]}", file=sourcefile)
        sourcefile.close()
        if user_input_is_valid(user_input[1]):
            urls = choose_repository(user_input[1])
            if urls is not None:
                for url in urls:
                    print_repository_info(url)
                    dig(url)
    else:
        print_help()


def print_help():
    """
    Print help text for wrong user input.
    """
    print("Expected: [lx] for local, [rx] for remote")
    print("Where x can be a number for selecting a repository, or 'a' for all of that type.")
    print(f"Maximum length: local:{len(pd.dict_repo_list.projects)}, remote:{len(pd.dict_repo_list.remote)}")


if __name__ == "__main__":
    main()
