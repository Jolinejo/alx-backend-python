#!/usr/bin/env python3
"""time while waiting n times"""


import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """return parallel runtime"""
    start_time = time.time()
    all_async = [async_comprehension() for i in range(4)]
    await asyncio.gather(*all_async)
    end_time = time.time()
    return end_time - start_time
