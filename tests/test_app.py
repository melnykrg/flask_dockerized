import pytest
import requests


@pytest.fixture
def url(request):
    url = request.config.getoption("--url")
    if not url:
        raise ValueError('HITS URL was not provided. Use \'--url\' option to set up')
    return url


def test_default_url(url):
    response = requests.get(url)
    assert int(response.text), 'The root page always has to contain only number'


def test_logs(url):
    response = requests.get(url + '/logs')
    assert 'My Hostname is:' in response.text, 'Logs do not have Hostname'
