#!/usr/bin/env python
"""
Small performance checks.
"""

import cProfile
import pstats
import os

# result with 10000, lot of with 100000
# BIG_NUMBER = 1000000
BIG_NUMBER = 100000000

"""
Project: BeamNGpy
Hash: e1e0f9db91aaa948bb4832e9c5e88f3c86d164f5
Message: Implement shared memory transmission for sensors and demo scenario
"""


def one_line_dict():
    for i in range(1, BIG_NUMBER):
        _data = dict(type='test')


def two_line_dict():
    for i in range(1, BIG_NUMBER):
        _data = dict()
        _data["type"] = "TEST"


def dict_lines():
    """
    Conclusions: dict one line is faster every time (so far).
    File: src/beamngpy/beamng.py
    Line numbers:
        old: (525, 526)   two_line_dict
        new: (400)        one_line_dict
    Summary: Change was best for performance.
    """

    print("dict one line")
    cProfile.run("one_line_dict()", 'results/profile_results_dol')
    results("results/profile_results_dol", "results/formatted_profile_dol.txt")
    print_results("results/formatted_profile_dol.txt")

    print("dict two line")
    cProfile.run("two_line_dict()", 'results/profile_results_dtl')
    results("results/profile_results_dtl", "results/formatted_profile_dtl.txt")
    print_results("results/formatted_profile_dtl.txt")


def dict_not_written():
    for i in range(1, BIG_NUMBER):
        _data = {"type": "TEST"}


def dict_written():
    for i in range(1, BIG_NUMBER):
        _data = dict(type="TEST")


def dict_writing_style():
    """
    Conclusion: Dict not written fastest every time (so far)
    File: src/beamngpy/beamng.py
    Line numbers:
        old: (500)  dict_not_written
        new: (357)  dict_written
    Summary: Change was not best for performance.
    """

    print("dict not written")
    cProfile.run("dict_not_written()", 'results/profile_results_dnw')
    results("results/profile_results_dnw", "results/formatted_profile_dnw.txt")
    print_results("results/formatted_profile_dnw.txt")

    print("dict written")
    cProfile.run("dict_written()", 'results/profile_results_dw')
    results("results/profile_results_dw", "results/formatted_profile_dw.txt")
    print_results("results/formatted_profile_dw.txt")


def results(name_file: str, name_new_file: str):
    file = open(name_new_file, 'w')
    profile = pstats.Stats(name_file, stream=file)
    profile.sort_stats('cumulative')
    profile.print_stats()
    file.close()


def print_results(formatted_file_name: str):
    f = open(formatted_file_name, "r")
    print(f.read())


def create_results_dir():
    path = "results"
    if not os.path.exists(path):
        try:
            os.mkdir(path)
        except OSError:
            print(f"Failed to create directory at {path}.")
        else:
            print(f"Directory {path} created.")
    else:
        print(f"Directory already existed at {path}.")


def main():
    create_results_dir()
    print("dict one line (new) VS dict two lines (old)")
    dict_lines()
    print("dict not written(old) VS dict written(new)")
    dict_writing_style()


if __name__ == "__main__":
    main()
