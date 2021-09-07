#!/usr/bin/env python
"""
Collect the raw data (not yet the graphs)
Only the parser, no analysis will be done here.
Output a "large" .csv file
"""
import csv
import re
import glob


def get_csv_file():
    results_file_name = "results.csv"
    return open(results_file_name, "w")
    # return csv.writer(final_csv)


def write_row(csv_writer, project, commit, dict_commit_info):
    the_array = [project, commit]
    for key in dict_commit_info.keys():
        the_array.append(dict_commit_info[key].strip())
    csv_writer.writerow(the_array)


def read_file(file_name, csv_writer):
    with open(file_name) as f:
        project = None
        commit = None
        title_topic = None
        dict_commit_info = {"hash": None, "message": None, "antipatterncategory": None, "keyword": None}
        for line in f:
            if project is None:
                if re.match("^[#] ", line):
                    first_line = re.split("^[#] ", line)
                    project = first_line[1]
                    continue
            if re.match("^## Commit", line):
                if commit:
                    print(f"dict: {dict_commit_info}")
                    write_row(csv_writer, project, commit, dict_commit_info)
                commit_sentence = re.split("^## Commit", line)
                commit = commit_sentence[1]
                dict_commit_info = {x: None for x in dict_commit_info}
            if re.match("^### ", line):
                title_topic = None
                sentence = re.split("### ", line)
                title = sentence[1]
                cleanup_title = ((title.lower()).strip()).replace(" ", "")
                # print(f"title: {cleanup_title}")
                if cleanup_title in dict_commit_info.keys():
                    title_topic = cleanup_title
                continue
            if title_topic is not None:
                if dict_commit_info[cleanup_title] is None:
                    dict_commit_info[cleanup_title] = line
                else:
                    dict_commit_info[cleanup_title] += line
        print(f"dict: {dict_commit_info}")
        write_row(csv_writer, project, commit, dict_commit_info)


def main():
    report_path = "../analysis"
    csv_file = get_csv_file()
    csv_writer = csv.writer(csv_file)
    for f in glob.glob(report_path + "/*.md"):
        read_file(f, csv_writer)
    csv_file.close()


if __name__ == "__main__":
    main()
