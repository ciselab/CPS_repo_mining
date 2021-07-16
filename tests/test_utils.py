#!/usr/bin/env python
"""
Tests for the search_current.py script.
"""
from pd.utils import build_results_path
from pd.utils import list_file_content
import tempfile
import re
import time
import os
import pathlib
import random


def test_existing_results_path(mocker):
    """
    Testing the build_results_path function with an existing file. Using a temporary directory and a temporary file.

    Args:
        mocker: Using a mocker to patch the location of the file to the temporary directory.

    """
    temp_suffix = '.txt'

    temp_dir_name = tempfile.mkdtemp()
    temp_file = tempfile.NamedTemporaryFile(suffix=temp_suffix, dir=temp_dir_name)

    file_name_with_extension = os.path.basename(temp_file.name)
    file_name_no_extension = pathlib.Path(temp_file.name).stem

    temp_dir_name_full = temp_file.name.replace(file_name_with_extension, "")

    mocker.patch('pd.utils.location', temp_dir_name_full)

    assert build_results_path(file_name_no_extension) == temp_file.name

    temp_file.close()
    os.removedirs(temp_dir_name)


def create_file_name_timestamped() -> str:
    """
    Helper function to create a file name with a timestamp.
    No file is being actually made.

    Returns:
        File name created.

    """
    current = str(time.time())
    result_current = re.split(r"\.", current)
    format_current = result_current[0] + result_current[1]
    file_name_test_project = 'Test_project_' + format_current
    return file_name_test_project


def test_non_existing_result_path():
    """
    Testing the build_results_path function with a non-existing file.
    """
    name_file = create_file_name_timestamped()
    added_number = random.randint(0, 100)
    non_existing_project = name_file + "_r" + str(added_number) + '.txt'
    if os.path.exists(non_existing_project):
        raise FileExistsError
    else:
        assert build_results_path(non_existing_project) is None


def test_list_file_content():
    """
    Testing reading file to convert to a list.
    """
    # noinspection SpellCheckingInspection
    input_file = [
        'C0FFEECAFEC0FFEECAFEC0FFEECAFEC0FFEECAFE\n',
        'CAFEC0FFEECAFEC0FFEECAFEC0FFEECAFEC0FFEE\n',
    ]
    temp_dir_name = tempfile.mkdtemp()
    test_file_path = os.path.join(temp_dir_name, create_file_name_timestamped())

    test_file = open(test_file_path, 'w')
    test_file.writelines(input_file)
    test_file.close()

    results = list_file_content(test_file_path)

    assert results == input_file

    os.remove(test_file_path)
    os.removedirs(temp_dir_name)
