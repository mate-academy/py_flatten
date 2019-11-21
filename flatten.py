"""Docstring"""
from typing import List, Any


def flatten(lis: List[Any]) -> List[int]:
    """Flatten given list"""
    string = str(lis)
    string = ''.join(string.split('['))
    string = ''.join(string.split(']'))

    return list(eval(string)) if lis else []
