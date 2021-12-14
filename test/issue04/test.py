import pytest
from one_hot_encoder import fit_transform


def test_eq_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [('Moscow', [0, 0, 1]),
     ('New York', [0, 1, 0]),
     ('Moscow', [0, 0, 1]),
     ('London', [1, 0, 0])]
    assert actual == expected


def test_not_eq_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    expected = [('New York', [0, 0, 1]),
     ('New York', [0, 1, 0]),
     ('Moscow', [0, 0, 1]),
     ('London', [1, 0, 0])]
    assert actual != expected


def test_not_in_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    assert 'Ryazan'not in actual


def test_in_cities():
    cities = ['Moscow', 'New York', 'Moscow', 'London']
    actual = fit_transform(cities)
    assert ('Moscow', [0, 0, 1]) in actual


def test_exception():
    error_ = 123
    with pytest.raises(TypeError):
        fit_transform(error_)
