import pytest
from bug3_logic import find_max


def test_positive_numbers():
    assert find_max([1, 3, 5, 2, 4]) == 5


def test_negative_numbers():
    assert find_max([-10, -3, -7, -1]) == -1


def test_single_element():
    assert find_max([42]) == 42


def test_duplicate_maximum():
    assert find_max([5, 9, 2, 9, 1]) == 9