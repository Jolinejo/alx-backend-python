#!/usr/bin/env python3
"""waiting n times"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """wait for n"""
    spawned = []
    for _ in range(n):
        spawned.append(wait_random(max_delay))
    ret = []
    for res in asyncio.as_completed(spawned):
        compl = await res
        ret.append(compl)
    return ret
