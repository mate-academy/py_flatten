"""module flat"""
from typing import List, Any
import re


def flatten(list_item: List[Any]) -> List[int]:
    """return result"""
    res = re.findall(r"\d", str(list_item))
    return [int(i) for i in res]
