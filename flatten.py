"""
implemented unpack of nested array
"""
from typing import List, Any


def flatten(init_list: List[Any]) -> List[int]:
    """

    :param init_list: [] list of nested arrays
    :return: [] unpacked array
    """
    result_list = []
    for item in init_list:
        if isinstance(item, list):
            for sub_item in flatten(item):
                result_list.append(sub_item)
        else:
            result_list.append(item)

    return result_list
