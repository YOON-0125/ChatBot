import os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))
import pytest
from topic_selector import get_response

@pytest.mark.parametrize("path,expected", [
    ('/sports', 'You selected sports.'),
    ('/music', 'You selected music.'),
    ('/science', 'You selected science.'),
    ('/unknown', 'Unknown topic.'),
])
def test_get_response(path, expected):
    assert get_response(path) == expected
