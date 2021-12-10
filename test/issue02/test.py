import pytest
from morse import decode


@pytest.mark.parametrize('test, expected', [
    ('... --- ...', 'SOS'),
    ('-.- --- ... .... -.- .-', 'KOSHKA'),
    ('----- ----. .-.-.- ----- ...-- .-.-.- ..--- ----- ----- .----', '09.03.2001'),
    ('--..--', ', ')
])
def test_decode(test, expected):
    assert decode(test) == expected
    
