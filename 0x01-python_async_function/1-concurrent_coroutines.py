#!/usr/bin/env python3
"""
    wait_n should return the list of all the delays (float values). The list
    of the delays should be in ascending order without using sort() because
    of concurrency.
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        wait_n should return the list of all the delays (float values).
    """
    ls = []
    for i in range(n):
        num = await wait_random(max_delay)
        ls.append(num)

    return sorted(ls)
