"""Docstring"""
from typing import List, Any


def flatten(lis: List[Any]) -> List[int]:
    """Flatten given list"""
    string = str(lis)
    string = ''.join(string.split('['))
    string = ''.join(string.split(']'))
    res = []
    for char in string:
        try:
            res.append(int(char))
        except ValueError:
            continue

    return res
