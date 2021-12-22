import pytest
from Pizza import Pepperoni, Margherita, Hawaiian


def test_equality():
    assert Pepperoni() == Pepperoni()


def test_other_size_init():
    with pytest.raises(ValueError):
        Pepperoni(size=1)


def test_inequality():
    assert Margherita() != Hawaiian()


def test_ineq_sizes():
    assert Margherita('XL') != Margherita('L')


def test_eq_sizes():
    assert Margherita('L') == Margherita('L')


def test_dict():
    assert Margherita('L').dict() == {'Ingredients of Margherita 🧀': 'tomato sauce, mozzarella, tomatoes', 'size': 'L'}


def test_dict_with_icon():
    assert Margherita('L').dict() != {'Ingredients of Margherita': 'tomato sauce, mozzarella, tomatoes', 'size': 'L'}


def test_is_dict():
    assert isinstance(Pepperoni().dict(), dict)
