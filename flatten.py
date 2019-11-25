'''
Module
'''
from typing import List, Any


def recursion(lst, result):
    '''

    :param lst:
    :param result:
    :return:
    '''
    for element in lst:
        if isinstance(element, list):
            recursion(element, result)
        else:
            result.append(element)


def flatten(lst: List[Any]) -> List[int]:
    '''

    :param lst:
    :return:
    '''
    result = []  # type: List[int]
    recursion(lst, result)
    return result
