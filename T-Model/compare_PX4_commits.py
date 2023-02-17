#!/usr/bin/env python
"""
Checks if the commits are already in a PX$-Autopilot word list.
"""
import re
import os

"""
Test param
"""
# dir_path = os.path.join("..", "T-Model", "t_model_2", "dir_commits", "test")
# word_a = "a"
# word_b = "b"
# file_a = word_a+".txt"
# file_b = word_b+".txt"

"""
Real
"""
dir_path = os.path.join("..", "T-Model", "t_model_2", "dir_commits", "PX4-Autopilot_commits_words")
word_a = "unneeded"
word_b = "timeout"
file_a = word_a+".txt"
file_b = word_b+".txt"


def compare_with_file(file_name, commit_hash) -> None:
    file_path = os.path.join(dir_path, file_name)
    file_name_removed = word_a+"_to_"+word_b+"_removed"+".txt"
    file_path_removed = os.path.join(dir_path, file_name_removed)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            # print(line.strip())
            file_commit_hash_results = re.findall('([a-zA-Z0-9]+)\s', line)
            file_commit_hash = file_commit_hash_results[0]
            if file_commit_hash == commit_hash:
                # pass
                with open(file_path_removed, 'a', encoding='utf-8') as fr:
                    # print(f"removed: {line}")
                    fr.write(line)
            else:
                f.write(line)
                # print(f"write: {line}")


def main() -> None:
    print("Starting")
    print(f"{word_a} to {word_b}")
    file_path_a = os.path.join(dir_path, file_a)
    with open(file_path_a, 'r', encoding='utf-8') as f:
        for line in f:
            # print(line)
            file_commit_hash_results = re.findall('([a-zA-Z0-9]+)\s', line)
            # print(f"compare: {file_commit_hash_results}")
            compare_with_file(file_b, file_commit_hash_results[0])
    print("Ended")


if __name__ == "__main__":
    main()
