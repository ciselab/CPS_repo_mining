#!/usr/bin/env python
"""
Tryout of PyDriller for remote & local repositories.
Focus on the content of commit messages.
"""

from pydriller import RepositoryMining
import datetime
import sys
from os import path


keyword_list = ['performance', 'Added', 'Ubuntu']
starting_date = datetime.datetime(2020, 2, 1, 0, 0)

remote = ["https://github.com/nasa-jpl/open-source-rover.git",
          "https://github.com/netdata/netdata.git"]
local = ""


def print_repository_info(url):
    """Print information about current run"""
    print(f"Repository: {url}")
    print(f"Searching for: {keyword_list}")


def print_commit_header(commit):
    """Print information about the commit"""
    print(f"\nhash: {commit.hash}\ndate: {commit.committer_date}\nmessage: {commit.msg}")
    print("modified file(s):")


def choose_repository(option):
    """Returns the repository URL for the given option"""
    if "r" in option:
        n = int(option.replace('r', ''))
        if (n >= 1) and (n <= len(remote)):
            url = remote[n-1]
        else:
            if not remote:
                print("Empty list of repositories.")
            else:
                print(f"Invalid option, out of range, options 1 to {len(remote)}.")
            return None
    elif option == 'l':
        if local and path.exists(path.expanduser(local)):
            url = local
        else:
            print("Empty string for local repository.")
            return None
    else:
        print("Invalid option, options are l (for local) or r (for remote).")
    return url


def dig(url):
    """Starts the mining process on the repository indicated by the given URL"""
    mine = RepositoryMining(url, since=starting_date)

    for commit in mine.traverse_commits():
        if any(keyword.lower() in commit.msg.lower() for keyword in keyword_list):
            print_commit_header(commit)

            for file_number, modified_file in enumerate(commit.modifications):
                print(f">>> {modified_file.filename}")
        else:
            continue


def main():
    """Main entry point when run as script"""
    if len(sys.argv) > 1:
        print(f"Input: {sys.argv[1]}")
        url = choose_repository(sys.argv[1])
        if url is not None:
            print_repository_info(url)
            dig(url)
    else:
        print("Expected: l=local, r1=remote NASA robot, r2=remote netdata")


if __name__ == "__main__":
    main()
