"""flatten the nesting module"""

from typing import List, Any


def flatten(array: List[Any]) -> List[int]:
    """flatten the nesting func"""
    result = []
    def recursion(arguments):
        """recursion func"""
        for i in arguments:
            if isinstance(i, list):
                recursion(i)
            else:
                result.append(i)
    recursion(array)
    return result
