#!/usr/bin/env python3
"""
tuple module
"""
from typing import List, Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    returns sum of list
    """
    tup = (k, v*v)
    return tup
