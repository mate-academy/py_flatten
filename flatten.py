"""doc"""
from typing import List, Any


def flatten(input_list: List[Any]) -> List[int]:
    """doc"""
    result = []

    def remove_nested(lis):
        """ loop through input list and checks type
        of its elements. If element is nested list, call this
         function again until element is not list, than append element
         to resulting list"""
        for element in lis:
            if isinstance(element, list):
                remove_nested(element)
            else:
                result.append(element)

    remove_nested(input_list)
    return result
