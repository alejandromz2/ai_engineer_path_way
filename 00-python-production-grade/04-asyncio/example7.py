import asyncio
import re
import time
from concurrent.futures import ProcessPoolExecutor
from unittest import result

# Regular Synchronous Function
async def fetch_data(param):
    await asyncio.sleep(param)
    return f"Result of {param}"


async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))

    result1 = await task1
    result2 = await task2
    print(f"Task 1 and 2 awaited results: {[result1, result2]}")

    # Gather Coroutines
    coroutines = [fetch_data(i) for i in range(1,3)]
    results = await asyncio.gather(*coroutines, return_exceptions=True) # If you use the default of return exceptions = false, when one task fails, then it raises the first exception that it saw, you don't get a bundle of errors. And if it fails, other tasks won't be cancelled. So you risk having  orphaned task
    # When you use return_exceptions=True, you still runs the other tasks. Every awaitaable in the gather finished whether it succeeds or fails. So you obtain a list where each position is either, the result of success or the exception of the failure
    print(f"Coroutine Results: {results}")

    # Gather Tasks
    tasks = [asyncio.create_task(fetch_data(i)) for i in range(1,3)]
    results = await asyncio.gather(*tasks)
    print(f"Task Results: {results}")

    # Task Group: 
    # It also fails quickly, but it gives better erros and handles cleanups a bit better
    # If one of the tasks fails, raises an exception group containing all exceptions from the failed tasks. We use it when we want all our tasks to run successfully
    async with asyncio.TaskGroup() as tg: 
        results = [tg.create_task(fetch_data(i))for i in range(1,3)]
        # All tasks are awaited when the context manager exits.
    print(f"Task Group Results: {[result.result() for result in results]}")

    return "Main Coroutine Done"

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")
