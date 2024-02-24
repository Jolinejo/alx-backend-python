#!/usr/bin/env python3
"""first aysnc mod"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """wair for delay"""
    for i in range(10):
        delay = random.uniform(0, 10)
        await asyncio.sleep(1)
        yield delay
