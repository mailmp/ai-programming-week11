import pytest
from bug3_logic import find_max


def test_normal_list():
    assert find_max([1, 3, 5, 2]) == 5


def test_max_at_first():
    assert find_max([10, 5, 3, 1]) == 10


def test_max_at_last():
    assert find_max([1, 3, 5, 10]) == 10


def test_negative_numbers():
    assert find_max([-5, -2, -8, -1]) == -1


def test_single_element():
    assert find_max([7]) == 7