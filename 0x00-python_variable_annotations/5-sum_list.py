#!/usr/bin/env python3
"""
sum module
"""


def sum_list(input_list: List[float]) -> float:
    """
    returns sum of list
    """
    sum = 0.0
    for num in input_list:
        sum += num
    return sum
