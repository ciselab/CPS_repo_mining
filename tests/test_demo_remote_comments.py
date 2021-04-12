import pytest
from pd.demo_remote_comments import choose_repository as cr


@pytest.mark.parametrize("remote, option, response", [
    pytest.param(["https://github.com/nasa-jpl/open-source-rover.git"],
                 "r1", "https://github.com/nasa-jpl/open-source-rover.git",
                 id="input=r1, length list=1"),
    pytest.param(["https://github.com/nasa-jpl/open-source-rover.git",
                  "https://github.com/netdata/netdata.git"],
                 "r2", "https://github.com/netdata/netdata.git",
                 id="input=r2, length list=2"),
])
def test_remote_url_list_length(remote, option, response):
    assert cr(option) == response
