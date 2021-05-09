#!/usr/bin/env python
"""
Tryout of PyDriller for remote & local repositories.
Focus on the content of commit messages.
"""

import re
from pydriller import RepositoryMining
from pydriller.domain.commit import Commit
import sys
from os import path
import pd.repo_lists as ls
from pd.key_list import keyword_list
from typing import Tuple, Optional


def print_repository_info(url: str):
    """
    Print information about current run

    Args:
        url: Repository url
    """
    print(f"Repository: {url}")
    print(f"Searching for: {keyword_list}")


def print_commit_header(commit: Commit):
    """
    Print information about the commit

    Args:
        commit: The full commit.
    """
    print(f"\nhash: {commit.hash}\ndate: {commit.committer_date}\nmessage: {commit.msg}")
    print(f"modified file(s): {commit.files}")


def repository_from_list(location: list, n: int) -> Optional[str]:
    """
    Use a list of repositories for selecting a single repository.

    Args:
        location: List of repositories, can be the local or remote list.
        n: Place number of the repository in the list.

    Returns:
        One URL from the list of urls.
    """
    if (n >= 1) and (n <= len(location)):
        url = location[n - 1]
    else:
        if not location:
            print("Empty list of repositories.")
        else:
            print(f"Invalid option, out of range, options 1 to {len(location)}.")
        return None
    return url


def choose_repository(option: str) -> Optional[Tuple[str, list]]:
    """
    Choose which repositories to use.

    Args:
        option: Choice for local or remote repository.
                Value behind l/r to choose which repository from the list.
                Possible to choose all remote repositories.

    Returns:
        The repository URL(s) for the given option.
    """
    url = None
    urls = None
    if re.fullmatch(r"[r]([1-9][0-9]*)", option):
        if len(option) > 1:
            n = int(option.replace('r', ''))
            url = repository_from_list(ls.remote, n)
            if not url:
                return None
        else:
            print_help()
            return None
    elif option == "ra":
        urls = ls.remote
    elif option == "la":
        urls = ls.local
    elif re.fullmatch(r"[l]([1-9][0-9]*)", option):
        if len(option) > 1:
            n = int(option.replace('l', ''))
            url = repository_from_list(ls.local, n)
            if not url:
                return None
            if not path.exists(path.expanduser(url)):
                print(f"Path {url} does not exist.")
                return None
        else:
            print_help()
            return None
    else:
        print_help()
        return None
    return url, urls


def dig(url: str) -> int:
    """
    Starts the mining process on the repository indicated by the given URL

    Args:
        url: Url of chosen repository.

    Returns:
        Number of commits.
    """
    mine = RepositoryMining(url)
    number_of_commits = 0

    for commit in mine.traverse_commits():
        for keyword in keyword_list:
            if re.search(r"\b" + keyword.lower() + r"\b", commit.msg.lower()):
                # Ignore merge pull request commits
                if commit.modifications:
                    print_commit_header(commit)
                    number_of_commits += 1
                    print(f"First found keyword: {keyword}")
                for modified_file in commit.modifications:
                    print(f">>> {modified_file.filename}")
                break
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


def main(user_input: list = None):
    """
    Main entry point when run as script

    Args:
        user_input: argv[1]: Input from user, local vs remote repository.<br/>
        [lx] = local, [rx] = remote: where x is the number in the list;
        [ra] = all remote repositories;
        [la] = all local repositories.
    """
    if not user_input:
        user_input = sys.argv
    if len(user_input) > 1:
        print(f"Input: {user_input[1]}")
        if user_input_is_valid(user_input[1]):
            url, urls = choose_repository(user_input[1])
            if url is not None:
                print_repository_info(url)
                dig(url)
            elif urls is not None:
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
    print(f"Maximum length: local:{len(ls.local)}, remote:{len(ls.remote)}")


if __name__ == "__main__":
    main()
