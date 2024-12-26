async def task_1(i: int, result: list):
    result.append("1")
    if i == 0:
        return
    if i > 5:
        await task_2(i // 2, result)
    else:
        await task_2(i - 1, result)


async def task_2(i: int, result: list):
    result.append("2")
    if i == 0:
        return
    if i % 2 == 0:
        await task_1(i // 2, result)
    else:
        await task_2(i - 1, result)


async def coroutines_execution_order(i: int = 42) -> int:
    result = []
    await task_1(i, result)
    return int("".join(result))
