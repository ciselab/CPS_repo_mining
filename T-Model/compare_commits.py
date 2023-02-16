#!/usr/bin/env python
"""
Checks if the commits are already manually analyzed before, then creates a list without these commits.
"""
import csv
import re
import os
import glob
import shutil

# project,commit,hash,message,antipattern,keyword
# {'node-ar-drone\n', 'grbl\n', 'Valetudo\n', 'johnny-five\n', 'cylon\n', 'Android app manager\n', 'PX4-Autopilot\n', 'dronekit-android\n', 'robonomics_contracts\n', 'turtlebot\n', 'arduino-esp32\n'}
# results.csv project name : project_commits.txt
dict_projects = {
    "node-ar-drone": "node-ar-drone_commits.txt",
    "grbl": "grbl_commits.txt",
    "Valetudo": "Valetudo_commits.txt",
    "johnny-five": "johnny-five_commits.txt",
    "cylon": "cylon_commits.txt",
    "Android app manager": "android_app_manager_commits.txt",
    "PX4-Autopilot": "PX4-Autopilot_commits.txt",
    "dronekit-android": "dronekit-android_commits.txt",
    "robonomics_contracts": "robonomics_contracts_commits.txt",
    "turtlebot": "turtlebot_commits.txt",
    "arduino-esp32": "arduino-esp32_commits.txt",
}
# Projects from which all commits can be used, none were manually analyzed.
dict_projects_nma = [
    "robonomics-js_commits.txt",
    "stofzuigerrobot_commits.txt",
    "turtlebot3_commits.txt"
]

# with open('../data-analysis/results.csv', 'r', encoding='utf-8') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     line_count = 0
#     project_names = set()
#     for row in csv_reader:
#         if line_count == 0:
#             print(f'Column names are {", ".join(row)}')
#             line_count += 1
#         elif row:
#             print(f'\tproject: {row[0]} with hash {row[2]}.')
#             line_count += 1
#             project_names.add(row[0])
#         #else:
#             #print(f'\t{row}')
#     print(f'Processed {line_count} lines.')
#     print(project_names)

# results_file_path = os.path.join("..", "T-Model", "dir_commits_2_adjusted")
# for result_files in results_file_path:
#     os.remove(result_files)
#
# src_path = os.path.join("..", "T-Model", "dir_commits_2")
# shutil.copy(src_path, results_file_path)


def compare_with_file(project_name, commit_hash):
    file_name = dict_projects[project_name]
    file_path = os.path.join("..", "T-Model", "dir_commits_2_adjusted", file_name)
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    with open(file_path, 'w', encoding='utf-8') as f:
        for line in lines:
            # print(line.strip())
            file_commit_hash_results = re.findall('([a-zA-Z0-9]+)\s', line)
            file_commit_hash = file_commit_hash_results[0]
            if file_commit_hash == commit_hash:
                pass
            else:
                f.write(line)


with open('../data-analysis/results.csv', 'r', encoding='utf-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    project_names = set()
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        elif row:
            project_name = row[0].strip()
            if row[2]:
                # print(f'\tproject: {project_name} with hash {row[2]}.')
                commit_hash_full = re.findall('\[([a-zA-Z0-9]+)', row[2])
                commit_hash = commit_hash_full[0]
                print(f"{project_name}, {commit_hash}")
                line_count += 1
                compare_with_file(project_name, commit_hash)
                # project_names.add(project_name)
            # else:
            #     print("No hash")
    print(f'Processed {line_count} lines.')
