#!/usr/bin/env python3
"""
    Take the code from wait_n and alter it into a new function task_wait_n.
    The code is nearly identical to wait_n except task_wait_random is being
    called.
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        wait_n should return the list of all the delays (float values).
        The list of the delays should be in ascending order without using
        sort() because of concurrency.
    """
    ls = []
    for i in range(n):
        num = await task_wait_random(max_delay)
        ls.append(num)

    return ls
