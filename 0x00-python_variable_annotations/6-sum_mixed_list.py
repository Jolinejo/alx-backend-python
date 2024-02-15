#!/usr/bin/env python3
"""
sum module
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """
    returns sum of list
    """
    sum = 0
    for num in mxd_list:
        sum += num
    return sum
