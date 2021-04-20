import pytest
from pd.demo_remote_comments import choose_repository as cr
import data_repo_lists as drl


@pytest.mark.parametrize("remote_p, option, response", [
    pytest.param(drl.remote,
                 "r1", (drl.remote[0], None),
                 id="input=r1"),
    pytest.param(drl.remote,
                 "r2", (drl.remote[1], None),
                 id="input=r2"),
    pytest.param(drl.remote,
                 "r3", (drl.remote[2], None),
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
                 "l1", 0, [drl.local[0], None],
                 id="input=l1"),
    pytest.param(drl.local, drl.local[1],
                 "l2", 1, [drl.local[1], None],
                 id="input=l2"),
    pytest.param(drl.local, drl.local[2],
                 "l3", 2, [drl.local[2], None],
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
    for each in local_p:
        new = tmpdir.mkdir(each)
        new_local_p.append(new)
    mocker.patch('pd.repo_lists.local', new_local_p)
    if type(response) is list:
        if response[0] is not None:
            response_new = (new_local_p[number], None)
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


@pytest.mark.parametrize("remote_p, option, response", [
    pytest.param(drl.remote,
                 "a", (None, drl.remote),
                 id="input=a"),
])
def test_input_all_remote(remote_p, option, response, mocker):
    """
    Input: all remote repositories
    """
    mocker.patch('pd.repo_lists.remote', remote_p)
    print(f"{cr(option)}")
    assert cr(option) == response
