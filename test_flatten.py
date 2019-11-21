"""
docstring
"""
import flatten


def test_empty():
    """

    :return:
    """
    assert flatten.flatten([]) == []


def test_two_levels():
    """

    :return:
    """
    assert flatten.flatten([[1, 2, 3], [4, 5, 6], 7]) == [1, 2, 3, 4, 5, 6, 7]


def test_arbitrary():
    """

    :return:
    """
    assert flatten.flatten([[2, 3], [[3, 4], 5], [[[5]]], 7]) == [2, 3, 3, 4, 5, 5, 7]
