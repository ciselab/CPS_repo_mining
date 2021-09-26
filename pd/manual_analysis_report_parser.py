#!/usr/bin/env python
"""
Collect the raw data (not yet the graphs)
Only the parser, no analysis will be done here.
Output a "large" .csv file
"""
import csv
import re
import glob
import os
import pathlib

dir_location_report = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results", "parser")


def get_csv_file():
    results_file_name = "results.csv"
    if not os.path.exists(os.path.abspath(dir_location_report)):
        os.makedirs(dir_location_report)
    full_path_results_file = os.path.join(dir_location_report, results_file_name)
    return open(full_path_results_file, "w")


def write_row(csv_writer, project: str, commit: str, dict_commit_info: dict):
    csv_line = [project, commit]
    for key in dict_commit_info.keys():
        if dict_commit_info[key] is not None:
            csv_line.append(dict_commit_info[key].strip())
        else:
            csv_line.append(dict_commit_info[key])
    csv_writer.writerow(csv_line)


def read_file(file_name: str, csv_writer):
    with open(file_name) as f:
        project = None
        commit = None
        title_topic = None
        # noinspection SpellCheckingInspection
        dict_commit_info = {"hash": None, "message": None, "antipatterncategory": None, "keyword": None}
        for line in f:
            if project is None:
                if re.match("^[#] ", line):
                    first_line = re.split("^[#] ", line)
                    project = first_line[1]
                    continue
            if re.match("^## Commit", line):
                if commit:
                    print(f"Commit: {project, dict_commit_info}")
                    write_row(csv_writer, project, commit, dict_commit_info)
                commit_sentence = re.split("^## Commit", line)
                commit = commit_sentence[1]
                dict_commit_info = {x: None for x in dict_commit_info}
            if re.match("^### ", line):
                title_topic = None
                sentence = re.split("### ", line)
                title = sentence[1]
                cleanup_title = ((title.lower()).strip()).replace(" ", "")
                if cleanup_title in dict_commit_info.keys():
                    title_topic = cleanup_title
                continue
            if title_topic is not None:
                if dict_commit_info[cleanup_title] is None:
                    dict_commit_info[cleanup_title] = line
                else:
                    dict_commit_info[cleanup_title] += line
        print(f"Last commit: {project, dict_commit_info}")
        write_row(csv_writer, project, commit, dict_commit_info)


def main():
    report_path = "../analysis"
    if os.path.exists(os.path.abspath(report_path)):
        csv_file = get_csv_file()
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for f in glob.glob(report_path + "/*.md"):
            read_file(f, csv_writer)
        csv_file.close()
    else:
        print("Warning: No analysis directory found in project...stopping.")


if __name__ == "__main__":
    main()
