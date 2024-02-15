#!/usr/bin/env python3
"""
sum module
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    returns sum of list
    """
    return lambda x: x * multiplier
