import pytest
from pd.demo_remote_comments import choose_repository as cr
from pd.demo_remote_comments import dig
import data_repo_lists as drl
import mock_git as nc
import data_commit as dm
import pd.key_list as key_list
from typing import Tuple


@pytest.mark.parametrize("remote_p, option, response", [
    pytest.param(drl.remote,
                 "r1", [drl.remote[0]],
                 id="input=r1"),
    pytest.param(drl.remote,
                 "r2", [drl.remote[1]],
                 id="input=r2"),
    pytest.param(drl.remote,
                 "r3", [drl.remote[2]],
                 id="input=r3"),
    pytest.param(drl.remote,
                 "r4", None,
                 id="invalid input=r4"),
    pytest.param(drl.remote,
                 "r-1", None,
                 id="invalid input=r-1"),
    pytest.param([],
                 "r1", None,
                 id="input=r1, empty remote list"),
    pytest.param([],
                 "r", None,
                 id="invalid input=r, missing number"),
])
def test_remote_url_list_length(remote_p, option, response, mocker):
    """
    Checks remote list usage with rx options.
    """
    mocker.patch('pd.repo_lists.remote', remote_p)
    print(f"{cr(option)}")
    assert cr(option) == response


@pytest.mark.parametrize("local_p, name, option, number, response", [
    pytest.param(drl.local, drl.local[0],
                 "l1", 0, [drl.local[0]],
                 id="input=l1"),
    pytest.param(drl.local, drl.local[1],
                 "l2", 1, [drl.local[1]],
                 id="input=l2"),
    pytest.param(drl.local, drl.local[2],
                 "l3", 2, [drl.local[2]],
                 id="input=l3"),
    pytest.param(drl.local, "foo",
                 "l-1", 1, None,
                 id="invalid input=l-1"),
    pytest.param(drl.local, "foo",
                 "l4", 4, None,
                 id="invalid input=l4"),
    pytest.param([], "foo",
                 "l1", 1, None,
                 id="input=l1, empty local list"),
    pytest.param([], "foo",
                 "l", 1, None,
                 id="input=l, missing number"),
])
def test_local_url_list_length(local_p, name, option, number, response, mocker, tmpdir):
    """
    Checks local list usage with lx options.
    """
    new_local_p = []
    response_new = []
    for each in range(len(local_p)):
        new = tmpdir.mkdir(local_p[each])
        new_local_p.append(new)
    mocker.patch('pd.repo_lists.local', new_local_p)
    if type(response) is list:
        if response[0] is not None:
            response_new = [new_local_p[number]]
    else:
        response_new = response
    assert cr(option) == response_new


def test_local_non_existing_dir(mocker):
    """
    Non-existing directory
    """
    mocker.patch('pd.repo_lists.local', ["non-existing-repo"])
    assert cr("l1") is None


@pytest.mark.parametrize("option, response", [
    pytest.param("z", None, id="Invalid input=z"),
    pytest.param("1", None, id="Invalid input=1"),
    pytest.param("&", None, id="Invalid input=&"),
])
def test_other_input(option, response):
    """
    Invalid input
    """
    print(f"{cr(option)}")
    assert cr(option) == response


@pytest.mark.parametrize("type_list, list_p, option, response", [
    pytest.param("remote", drl.remote,
                 "ra", drl.remote,
                 id="input=ra"),
    pytest.param("local", drl.local,
                 "la", drl.local,
                 id="input=la"),
])
def test_input_all(type_list, list_p, option, response, mocker):
    """
    Input: all remote repositories
    """
    patch_list = "pd.repo_lists."+type_list
    mocker.patch(patch_list, list_p)
    print(f"{cr(option)}")
    assert cr(option) == response


def use_new_commits(hs: Tuple, messages: Tuple, committer_date: Tuple, files_name: Tuple) -> list:
    """
    Helper function for mocking commit messages.

    Args:
        hs: hash commit
        messages: commit message
        committer_date: date of the commit
        files_name: name(s) of the file(s)

    Returns:
        list_nc: List of commits
    """
    list_nc = []
    for n in range(0, len(messages)):
        files_nr = len(files_name[n])
        nm = nc.MockableModifications(files_name[n])
        cm = nc.MockableCommit(hs[n], messages[n], nm, committer_date[n], files_nr)
        list_nc.append(cm)
    return list_nc


@pytest.mark.parametrize("new_keywords, hs, messages, files_name, committer_date, response", [
    pytest.param(key_list,
                 (dm.hs[0], dm.hs[1]),
                 (dm.ms[0], dm.ms[1]),
                 ((dm.fn[0], dm.fn[1]), (dm.fn[1], dm.fn[2])),
                 (dm.cd[0], dm.cd[1]),
                 2, id="2 commits"),
    pytest.param(key_list,
                 (dm.hs[2],),
                 (dm.ms[2],),
                 ((dm.fn[2],), (dm.fn[2],)),
                 (dm.cd[2],),
                 1, id="1 commit"),
    pytest.param(key_list,
                 (dm.hs[3],),
                 (dm.ms[3],),
                 ((dm.fn[3],), (dm.fn[4],)),
                 (dm.cd[3],),
                 0, id="no commit found that matches keywords"),
    pytest.param(key_list,
                 (dm.hs[3], dm.hs[4]),
                 (dm.ms[3], dm.ms[4]),
                 ((dm.fn[3],), (dm.fn[4], dm.fn[5])),
                 (dm.cd[4], dm.cd[5]),
                 0, id="no commits found that matches keywords"),
    pytest.param(key_list,
                 (dm.hs[0], dm.hs[5]),
                 (dm.ms[0], dm.ms[5]),
                 ((dm.fn[0], dm.fn[1]), (dm.fn[4], dm.fn[5])),
                 (dm.cd[0], dm.cd[5]),
                 1, id="1 commit found, 1 ignored"),
])
def test_keywords(new_keywords: list, hs: Tuple, messages: Tuple,
                  files_name: Tuple, committer_date: Tuple, response: int, mocker):
    """
    Tests for keywords in a commit message.

    Args:
        new_keywords: List of keywords
        hs: hash of the commit
        messages: message of the commit
        files_name: files adjusted in the commit
        committer_date: date of commit placed
        response: expected result from test
        mocker: mocker is being used in this test

    Returns:
        Response of the dig function with the test input.

    """
    def return_new_commits(_foo):
        return use_new_commits(hs, messages, committer_date, files_name)

    mocker.patch("pydriller.RepositoryMining.traverse_commits", return_new_commits)
    assert dig("TEST") == response
