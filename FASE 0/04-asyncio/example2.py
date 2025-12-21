import time
import asyncio

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    # We only are creating a coroutine object, we are not scheldule them
    task1 = fetch_data(1)
    task2 = fetch_data(2)
    # When we await a coroutine object, we are scheldule and running it to completion at the same time. We get no concurrency here and no benefit to using asyncio 
    result1 = await task1
    print("Fetch 1 fully completed")
    result2 = await task2
    print("Fetch 2 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")