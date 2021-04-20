import pytest
from pd.demo_remote_comments import choose_repository as cr


@pytest.mark.parametrize("remote_p, option, response", [
    pytest.param(["https://github.com/nasa-jpl/open-source-rover.git"],
                 "r1", ("https://github.com/nasa-jpl/open-source-rover.git", None),
                 id="input=r1, length list=1"),
    pytest.param(["https://github.com/nasa-jpl/open-source-rover.git",
                  "https://github.com/netdata/netdata.git"],
                 "r2", ("https://github.com/netdata/netdata.git", None),
                 id="input=r2, length list=2"),
])
def test_remote_url_list_length(remote_p, option, response, mocker):
    mocker.patch('pd.repo_lists.remote', remote_p)
    assert cr(option) == response
