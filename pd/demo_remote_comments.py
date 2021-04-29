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
    Returns one URL from the list of urls.

    Args:
        location: List of repositories, can be the local or remote list.
        n: Place number of the repository in the list.
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
    Returns the repository URL(s) for the given option

    Args:
        option: Choice for local or remote repository.
                Value behind l/r to choose which repository from the list.
                Possible to choose all remote repositories.
    """
    url = None
    urls = None
    if "r" in option:
        if len(option) > 1:
            n = int(option.replace('r', ''))
            url = repository_from_list(ls.remote, n)
            if not url:
                return None
        else:
            print("Invalid option, no repository selected.")
            print("Options for remote are:")
            for i, url in enumerate(ls.remote):
                print(f"r{i}: {url}")
            return None
    elif option == 'a':
        urls = ls.remote
    elif option == 'h':
        urls = ls.local
    elif 'l' in option:
        if len(option) > 1:
            n = int(option.replace('l', ''))
            url = repository_from_list(ls.local, n)
            if not url:
                return None
            if not path.exists(path.expanduser(url)):
                print(f"Path {url} does not exist.")
                return None
        else:
            print("Invalid option, no repository selected.")
            print("Options for local are:")
            for i, url in enumerate(ls.local):
                print(f"l{i}: {url}")
            return None
    else:
        print("Invalid option: options are l (for local) or r (for remote),")
        print("h (for all local) or a (for all remote).")
        return None
    return url, urls


def dig(url: str):
    """
    Starts the mining process on the repository indicated by the given URL

    Args:
        url: Url of chosen repository.
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


def main(user_input: list = None):
    """
    Main entry point when run as script

    Args:
        user_input: argv[1]: Input from user, local vs remote repository.<br/>
        [lx] = local, [rx] = remote: where x is the number in the list;
        [a] = all remote repositories;
        [h] = all local repositories.
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
        print("Expected: [lx] for local, [rx] for remote, [a] for all remote and [h] for all local repositories.")
        for i, url in enumerate(ls.local):
            print(f"l{i}: {url}")
        for i, url in enumerate(ls.remote):
            print(f"r{i}: {url}")


if __name__ == "__main__":
    main()
