#!/usr/bin/env python3
"""Defines wait_n"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous coroutine that spawns n instances of
    wait_random with specified max_delay"""
    delays = await asyncio.gather(*tuple(map(lambda _: wait_random(
        max_delay), range(n))))
    sorted_delays = sorted(delays)
    return sorted_delays
