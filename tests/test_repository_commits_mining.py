import shutil
import pytest
import os
import pathlib
import tempfile
from pd.repository_commits_mining import choose_repository as cr
from pd.repository_commits_mining import dig
from pd.repository_commits_mining import user_input_is_valid as uiv
from pd.repository_commits_mining import restart_results_file
from pd.repository_commits_mining import remove_files_in_dir
import data_repo_dict as drl
import mock_git as nc
import data_commit as dm
import pd.key_list as key_list
from typing import Tuple, Any, Optional
from test_utils import create_file_name_timestamped


@pytest.mark.parametrize("remote_p, option, response", [
    pytest.param(drl.remote, "r1", ["https://github.com/carla-simulator/carla"], id="input=r1"),
    pytest.param(drl.remote, "r2", ["https://github.com/microsoft/AirSim"], id="input=r2"),
    pytest.param(drl.remote, "r3", ["https://github.com/BeamNG/BeamNGpy.git"], id="input=r3"),
    pytest.param(drl.remote, "r4", None, id="invalid input=r4"),
    pytest.param(drl.remote, "r-1", None, id="invalid input=r-1"),
    pytest.param([], "r1", None, id="input=r1, empty remote list"),
    pytest.param([], "r", None, id="invalid input=r, missing number"),
])
def test_remote_url_list_length(remote_p: dict, option: str, response: Optional[list], mocker):
    """
    Checks remote list usage with rx options.

    Args:
        remote_p: List of the remote repository
        option: User input
        response: Expected response
        mocker: Using a mocker

    """
    mocker.patch('pd.dict_repo_list.remote', remote_p)
    assert cr(option) == response


@pytest.mark.parametrize("local_p, option, number, response_dict", [
    pytest.param(drl.projects, "l1", 0, drl.projects, id="input=l1"),
    pytest.param(drl.projects, "l2", 1, drl.projects, id="input=l2"),
    pytest.param(drl.projects, "l3", 2, drl.projects, id="input=l3"),
    pytest.param(drl.projects, "l-1", 1, None, id="invalid input=l-1"),
    pytest.param(drl.projects, "l4", 4, None, id="invalid input=l4"),
    pytest.param([], "l1", 1, None, id="input=l1, empty local list"),
    pytest.param([], "l", 1, None, id="input=l, missing number"),
])
def test_local_url_list_length(local_p: dict, option: str, number: int, response_dict: Optional[dict], mocker, tmpdir):
    """
    Checks local list usage with lx options.

    Args:
        local_p: Dictionary of the local repository
        option: User input
        number: Location in the list of the requested repository
        response_dict:  None or the full dictionary;
                        with the dictionary the response is in combination with number;
                        None in case the input was invalid, therefore should return None.
        mocker: Using a mocker
        tmpdir: Using a temporary directory

    """
    for each in local_p:
        new = tmpdir.mkdir(each)
        local_p[each] = new
    mocker.patch('pd.dict_repo_list.projects', drl.projects)
    mocker.patch('pd.dict_repo_list.build_repo_dict', return_value=local_p)
    if response_dict is not None:
        values_response = list(local_p.values())
        response_new = [values_response[number]]
    else:
        response_new = response_dict
    assert cr(option) == response_new


def test_local_non_existing_dir(mocker):
    """
    Non-existing directory

    Args:
        mocker: Using a mocker

    """
    mocker.patch('pd.dict_repo_list.projects', {"non-existing-repo": None})
    assert cr("l1") is None


@pytest.mark.parametrize("option", [
    pytest.param("z", id="Invalid input=z"),
    pytest.param("1", id="Invalid input=1"),
    pytest.param("&", id="Invalid input=&"),
])
def test_other_input(option: str):
    """
    Invalid input

    Args:
        option: Invalid user input.

    """
    assert cr(option) is None


@pytest.mark.parametrize("type_list, list_p, option, response", [
    pytest.param("remote", drl.remote, "ra", drl.remote, id="input=ra"),
    pytest.param("projects", drl.projects, "la", drl.projects, id="input=la"),
])
def test_input_all(type_list: str, list_p: list, option: str, response: dict, mocker):
    """
    Input: all remote repositories

    Args:
        type_list: Using a remote or local repository
        list_p: Given the repository list
        option: User input
        response: Dictionary of the expected repository
        mocker: Using a mocker

    """
    compare_results = response.values()
    patch_list = "pd.dict_repo_list." + type_list
    mocker.patch(patch_list, list_p)
    assert cr(option) == list(compare_results)


def use_new_commits(hs: Tuple, messages: Tuple, committer_date: Tuple, files_name: Tuple, project_name: Tuple) -> list:
    """
    Helper function for mocking commit messages.

    Args:
        hs: hash commit
        messages: commit message
        committer_date: date of the commit
        files_name: name(s) of the file(s)
        project_name: name of the project

    Returns:
        list_nc: List of commits
    """
    list_nc = []
    for n in range(0, len(messages)):
        files_nr = len(files_name[n])
        nm = nc.MockableModifications(files_name[n])
        cm = nc.MockableCommit(hs[n], messages[n], nm, committer_date[n], files_nr, project_name[n])
        list_nc.append(cm)
    return list_nc


def create_file(text: str):
    """
    Create the resultsOutput.txt file in the test_results location.

    Args:
        text: Text to be written in the file.

    """
    dir_location = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "test_results")
    if not os.path.exists(os.path.abspath(dir_location)):
        os.makedirs(dir_location)
    location_sourcefile = os.path.join(dir_location, "resultsOutput.txt")
    sourcefile = open(location_sourcefile, 'w')
    print(f"{text}", file=sourcefile)
    sourcefile.close()


@pytest.mark.parametrize("new_keywords, hs, messages, files_name, committer_date, project_name, response", [
    pytest.param(key_list,
                 (dm.hs[0], dm.hs[1]),
                 (dm.ms[0], dm.ms[1]),
                 ((dm.fn[0], dm.fn[1]), (dm.fn[1], dm.fn[2])),
                 (dm.cd[0], dm.cd[1]),
                 (dm.pn[0], dm.pn[1]),
                 2, id="2 commits"),
    pytest.param(key_list,
                 (dm.hs[2],),
                 (dm.ms[2],),
                 ((dm.fn[2],), (None, )),
                 (dm.cd[2],),
                 (dm.pn[2],),
                 1, id="1 commit"),
    pytest.param(key_list,
                 (dm.hs[3],),
                 (dm.ms[3],),
                 ((dm.fn[3],), (dm.fn[4],)),
                 (dm.cd[3],),
                 (dm.pn[3],),
                 0, id="no commit found that matches keywords"),
    pytest.param(key_list,
                 (dm.hs[3], dm.hs[4]),
                 (dm.ms[3], dm.ms[4]),
                 ((dm.fn[3],), (dm.fn[4], dm.fn[5])),
                 (dm.cd[4], dm.cd[5]),
                 (dm.pn[4], dm.pn[5]),
                 0, id="no commits found that matches keywords"),
    pytest.param(key_list,
                 (dm.hs[0], dm.hs[5]),
                 (dm.ms[0], dm.ms[5]),
                 ((dm.fn[0], dm.fn[1]), (dm.fn[4], dm.fn[5])),
                 (dm.cd[0], dm.cd[5]),
                 (dm.pn[0], dm.pn[5]),
                 1, id="1 commit found, 1 ignored"),
])
def test_keywords(new_keywords: list, hs: Tuple, messages: Tuple,
                  files_name: Tuple, committer_date: Tuple, project_name: Tuple, response: int, mocker):
    """
    Tests for keywords in a commit message.
    Response of the dig function with the test input.

    Args:
        new_keywords: List of keywords
        hs: hash of the commit
        messages: message of the commit
        files_name: files adjusted in the commit
        committer_date: date of commit placed
        project_name: name of the project, used for creating file with results
        response: expected result from test
        mocker: mocker is being used in this test

    """
    def return_new_commits(_foo: Any) -> list:
        return use_new_commits(hs, messages, committer_date, files_name, project_name)

    """ Creating the starting file """
    create_file("Testing: test_keywords")

    mocker.patch("pydriller.RepositoryMining.traverse_commits", return_new_commits)

    fn_results = "resultsOutput.txt"
    patched_location_sourcefile = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "test_results", fn_results)
    mocker.patch("pd.repository_commits_mining.location_sourcefile", patched_location_sourcefile)

    patched_dir_projects = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "test_results", "repo")
    mocker.patch("pd.repository_commits_mining.dir_projects", patched_dir_projects)

    assert dig("TEST") == response
    main_dir = os.path.join(pathlib.Path.home(), "CPS_repo_mining", "test_results")
    try:
        shutil.rmtree(main_dir)
    except OSError as e:
        print(f"Error: {main_dir} : {e.strerror}")


@pytest.mark.parametrize("user_input, response", [
    pytest.param("la", True, id="la"),
    pytest.param("ra", True, id="ra"),
    pytest.param("l1", True, id="l1"),
    pytest.param("l2", True, id="l2"),
    pytest.param("r1", True, id="r1"),
    pytest.param("r9", True, id="r9"),
    pytest.param("l99", True, id="l99"),
    pytest.param("r99", True, id="r99"),
    pytest.param("l101", True, id="l101"),
    pytest.param("r101", True, id="r101"),
    pytest.param("a", False, id="False: a"),
    pytest.param("aa", False, id="False: aa"),
    pytest.param("1", False, id="False: 1"),
    pytest.param("11", False, id="False: 11"),
    pytest.param("l", False, id="False: l"),
    pytest.param("r", False, id="False: r"),
    pytest.param("l0", False, id="False: l0"),
    pytest.param("r0", False, id="False: r0"),
    pytest.param("00", False, id="False: 00"),
    pytest.param("lb", False, id="False: lb"),
    pytest.param("rb", False, id="False: rb"),
    pytest.param("l1l2", False, id="False: l1l2"),
    pytest.param("r1r2", False, id="False: r1r2"),
    pytest.param("l1r2", False, id="False: l1r2"),
    pytest.param("r1l2", False, id="False: r1l2"),
    pytest.param("", False, id="False: EMPTY"),
    pytest.param("l-1", False, id="False: l-1"),
    pytest.param("r-1", False, id="False: r-1"),
])
def test_user_input_is_valid(user_input: str, response: bool):
    """
    Tests the user_input_is_valid function against expected accepted and rejected input.

    Args:
        user_input: Different valid and invalid user input.
        response: Expected return.

    """
    assert uiv(user_input) == response


def test_restart_results_file():
    """
    Test to check the file is removed by restart_results_file.
    """
    temp_dir_name = tempfile.mkdtemp()
    test_file_path = os.path.join(temp_dir_name, create_file_name_timestamped())

    test_file = open(test_file_path, 'w')
    test_file.close()

    assert os.path.isfile(test_file_path) is True
    restart_results_file(test_file_path)
    assert os.path.isfile(test_file_path) is False

    if os.path.isfile(test_file_path):
        os.remove(test_file_path)
    os.removedirs(temp_dir_name)


def test_remove_files_in_dir():
    """
    Test that all the files in the selected dir are removed.
    """
    temp_dir_name = "TempTest"
    project_pd_dir = os.path.join(pathlib.Path.home(), "Testing_CPS_repo_mining")
    dir_location_start = os.path.join(project_pd_dir, temp_dir_name)

    if not os.path.isdir(dir_location_start):
        os.makedirs(dir_location_start)
    test_files = [
        os.path.join(dir_location_start, (create_file_name_timestamped() + "_t1.txt")),
        os.path.join(dir_location_start, (create_file_name_timestamped() + "_t2.txt")),
        os.path.join(dir_location_start, (create_file_name_timestamped() + "_t3.txt")),
    ]

    for file in test_files:
        test_file = open(file, 'w')
        test_file.close()

    for file in test_files:
        """ To be sure the setup is correct for the test """
        assert os.path.isfile(file) is True

    remove_files_in_dir(dir_location_start)

    for file in test_files:
        """ The assert to see if the remove_files_in_dir() did what it should """
        assert os.path.isfile(file) is False

    """ Directory still exists, only files have been removed """
    assert os.path.isdir(dir_location_start) is True

    os.removedirs(dir_location_start)
