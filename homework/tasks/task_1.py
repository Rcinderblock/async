from asyncio import Task
from typing import Callable, Coroutine, Any


async def await_my_func(f: Callable[..., Coroutine] | Task | Coroutine) -> Any:
    if isinstance(f, Callable):
        coroutine = f()
        result = await coroutine
    elif isinstance(f, Task):
        result = await f
    elif isinstance(f, Coroutine):
        result = await f
    else:
        raise ValueError('invalid argument')

    return result
