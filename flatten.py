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
    if not lst:
        return lst
    if isinstance(lst[0], list):
        return flatten(lst[0]) + flatten(lst[1:])
    return lst[:1] + flatten(lst[1:])
