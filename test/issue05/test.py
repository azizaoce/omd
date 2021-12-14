import urllib.request
import pytest
from unittest.mock import patch
from io import StringIO
from what_is_year_now import what_is_year_now


def test_year_now():
    with patch.object(urllib.request, 'urlopen', return_value=StringIO('{"currentDateTime": "2019-03-01"}')):
        actual_year = what_is_year_now()
        assert actual_year == 2019


def test_valueerror():
    with pytest.raises(IndexError):
        with patch.object(urllib.request, 'urlopen', return_value=StringIO('{"currentDateTime": "123%"}')):
            what_is_year_now()
