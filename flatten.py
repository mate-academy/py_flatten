"""
flatten module
"""
from typing import List, Any


def flatten(lst: List[Any]) -> List[int]:
    """
    Flatten the nesting in an arbitrary list of values.
    :param lst: List[Any]
    :return: List[int]
    """
    for i, element in enumerate(lst):
        while i < len(lst) and isinstance(lst[i], list):
            lst[i:i + 1] = lst[i]
    return lst
