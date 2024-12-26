import asyncio
from typing import Coroutine


async def limit_execution_time(coro: Coroutine, max_execution_time: float):
    try:
        await asyncio.wait_for(coro, max_execution_time)
    except asyncio.TimeoutError:
        print('Timeout!')
        return


async def limit_execution_time_many(*coros: Coroutine, max_execution_time: float) -> None:
    try:
        limited_coros = [asyncio.wait_for(coro, max_execution_time) for coro in coros]
        await asyncio.gather(*limited_coros)
    except asyncio.TimeoutError:
        print('Timeout!')
        return
