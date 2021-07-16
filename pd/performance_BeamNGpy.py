#!/usr/bin/env python
"""
Small performance checks.
"""

import cProfile
import pstats
import os
import pathlib

# result with 10000, lot of with 100000
# BIG_NUMBER = 1000000
BIG_NUMBER = 100000000
path_results = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "results")

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
    file_dol = os.path.join(path_results, "profile_results_dol")
    cProfile.run("one_line_dict()", file_dol)
    formatted_file_dol = os.path.join(path_results, "formatted_profile_dol.txt")
    results(file_dol, formatted_file_dol)
    print_results(formatted_file_dol)

    print("dict two line")
    file_dtl = os.path.join(path_results, "profile_results_dtl")
    cProfile.run("two_line_dict()", file_dtl)
    formatted_file_dtl = os.path.join(path_results, "formatted_profile_dtl.txt")
    results(file_dtl, formatted_file_dtl)
    print_results(formatted_file_dtl)


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
    file_dnw = os.path.join(path_results, "profile_results_dnw")
    cProfile.run("dict_not_written()", file_dnw)
    formatted_file_dnw = os.path.join(path_results, "formatted_profile_dnw.txt")
    results(file_dnw, formatted_file_dnw)
    print_results(formatted_file_dnw)

    print("dict written")
    file_dw = os.path.join(path_results, "profile_results_dw")
    cProfile.run("dict_written()", file_dw)
    formatted_file_dw = os.path.join(path_results, "formatted_profile_dw.txt")
    results(file_dw, formatted_file_dw)
    print_results(formatted_file_dw)


def results(name_file: str, name_new_file: str):
    """
    Convert profile data to readable data.

    Args:
        name_file: Location file with profile data.
        name_new_file:  Location where the readable profile data will be stored.
    """
    file = open(name_new_file, 'w')
    profile = pstats.Stats(name_file, stream=file)
    profile.sort_stats('cumulative')
    profile.print_stats()
    file.close()


def print_results(formatted_file_name: str):
    """
    Print the results.

    Args:
        formatted_file_name: Location of the results.
    """
    f = open(formatted_file_name, "r")
    print(f.read())
    f.close()


def main():
    if not os.path.exists(os.path.abspath(path_results)):
        os.makedirs(path_results)
    print("dict one line (new) VS dict two lines (old)")
    dict_lines()
    print("dict not written(old) VS dict written(new)")
    dict_writing_style()


if __name__ == "__main__":
    main()
