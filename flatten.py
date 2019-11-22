"""Understand recursion"""
from typing import List, Any


def flatten(arr: List[Any]) -> List[int]:
    """I love flat() in JS))"""
    result = []

    def flat(given_arr):
        for i in given_arr:
            if isinstance(i, int):
                result.append(i)
            else:
                flat(i)
    flat(arr)

    return result
