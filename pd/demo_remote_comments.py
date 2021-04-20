#!/usr/bin/env python
"""
Tryout of PyDriller for remote & local repositories.
Focus on the content of commit messages.
"""

from pydriller import RepositoryMining
import datetime
import sys
from os import path
import pd.repo_lists as ls
from pd.key_list import keyword_list
from typing import Tuple


starting_date = datetime.datetime(2020, 2, 1, 0, 0)


def print_repository_info(url: str):
    """
    Print information about current run

    Args:
        url: Repository url
    """
    print(f"Repository: {url}")
    print(f"Searching for: {keyword_list}")


def print_commit_header(commit: object):
    """
    Print information about the commit

    Args:
        commit: The full commit.
    """
    print(f"\nhash: {commit.hash}\ndate: {commit.committer_date}\nmessage: {commit.msg}")
    print("modified file(s):")


def choose_repository(option: str) -> Tuple[str, list]:
    """
    Returns the repository URL(s) for the given option

    Args:
        option: Choice for local or remote repository.
                Value behind l/r to choose which repository from the list.
                Possible to choose all remote repositories.
    """
    url = None
    urls = None
    if "r" in option:
        n = int(option.replace('r', ''))
        if (n >= 1) and (n <= len(ls.remote)):
            url = ls.remote[n-1]
        else:
            if not ls.remote:
                print("Empty list of repositories.")
            else:
                print(f"Invalid option, out of range, options 1 to {len(ls.remote)}.")
            return None
    elif option == 'a':
        urls = ls.remote
    elif 'l' in option:
        n = int(option.replace('l', ''))
        if (n >= 1) and (n <= len(ls.local)):
            url_check = ls.local[n-1]
        else:
            if not ls.remote:
                print("Empty list of repositories.")
            else:
                print(f"Invalid option, out of range, options 1 to {len(ls.remote)}.")
            return None
        if path.exists(path.expanduser(url_check)):
            url = url_check
        else:
            print(f"Path {url_check} does not exist.")
            return None
    else:
        print("Invalid option, options are l (for local) or r (for remote).")
        return None
    return url, urls


def dig(url: str):
    """
    Starts the mining process on the repository indicated by the given URL

    Args:
        url: Url of chosen repository.
    """
    mine = RepositoryMining(url, since=starting_date)

    for commit in mine.traverse_commits():
        if any(keyword.lower() in commit.msg.lower() for keyword in keyword_list):
            print_commit_header(commit)

            for file_number, modified_file in enumerate(commit.modifications):
                print(f">>> {modified_file.filename}")
        else:
            continue


def main(user_input: list = None):
    """
    Main entry point when run as script

    Args:
        user_input: argv[1]: Input from user, local vs remote repository.<br/>
        [lx] = local, [rx] = remote: where x is the number in the list;
        [a] = all remote repositories.
    """
    if not user_input:
        user_input = sys.argv
    if len(user_input) > 1:
        print(f"Input: {user_input[1]}")
        url, urls = choose_repository(user_input[1])
        if url is not None:
            print_repository_info(url)
            dig(url)
        elif urls is not None:
            for url in urls:
                print_repository_info(url)
                dig(url)
    else:
        print("Expected: [lx] for local, [rx] for remote or [a] for all remote repositories.")
        for i, url in enumerate(ls.local):
            print(f"l{i}: {url}")
        for i, url in enumerate(ls.remote):
            print(f"r{i}: {url}")


if __name__ == "__main__":
    main()
