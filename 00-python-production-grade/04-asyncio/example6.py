import asyncio
import re
import time
from concurrent.futures import ProcessPoolExecutor

# Regular Synchronous Function
def fetch_data(param):
    print(f"Do something with {param}...", flush=True)
    time.sleep(param)
    print(f"Done with {param}", flush=True)
    return f"Result of {param}"

async def main():
    # Run in Threads
    # When we create the task, we're wrapping our fetch data funcition here inside of asyncio.to_thread function. This will wrap our synchronous function with a future and make it awaitable. We pass sync function and arguments separately so asyncio.to_thread can execute later when it's ready. 
    task1 = asyncio.create_task(asyncio.to_thread(fetch_data,1))
    task2 = asyncio.create_task(asyncio.to_thread(fetch_data,2))
    result1 = await task1
    print("Thread 1 fully completed")
    result2 = await task2
    print("Thread 2 fully completed")

    # Run in Process Pool
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as executor:
        # We are creating the tasks with loop.run_in_excutor, and we pass the executor, the function that we want to run in a process and arguments separately 
        task1 = loop.run_in_executor(executor, fetch_data, 1)
        task2 = loop.run_in_executor(executor, fetch_data, 2)

        result1 = await task1
        print("Process 1 fully completed")
        result1 = await task2
        print("Process 2 fully completed")

    return [result1, result2]

if __name__ == "__main__":
    t1 = time.perf_counter()
    results = asyncio.run(main())
    print(results)

    t2 = time.perf_counter()
    print(f"Finished in {t2-t1:.2f} seconds")