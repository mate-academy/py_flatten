"""
docstring
"""
from typing import List, Any


def flatten(lst: List[Any]) -> List[int]:
    """

    :param lst:
    :return:
    """
    return sum(([x] if not isinstance(x, list) else flatten(x) for x in lst), [])
