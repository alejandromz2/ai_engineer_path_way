import time
import asyncio

async def fetch_data(param):
    print(f"Do something with {param}...")
    await asyncio.sleep(param)
    print(f"Done with {param}")
    return f"Result of {param}"

async def main():
    task1 = asyncio.create_task(fetch_data(1))
    task2 = asyncio.create_task(fetch_data(2))
    # When we await a coroutine object, we are scheldule and running it to completion at the same time. We get no concurrency here and no benefit to using asyncio 
    # When we await something, we are not guaranteeing that we run that particular part right at that moment. The event loop is going to run whatever is ready. What we are guaranteeing is that we are  going to be done with what we awaited before moving on. And it doesn't even need to be one of these tasks that we await
    # En el await task2 se inicia primero task1, ya que fue agendado primero. Luego se pasa a task2 por el sleep de task1, se termina de ejecutar task1 y se guarda en memoria, se termina de ejecutar task 2 y se almacena el resultado de task2 en result2. Posteriormente, cuando pasa por await task1, lo que ocurre es que el resultado task1 se extrae de memoria y se usa para setear a result1, ya que no hay nada que ejecutar porque el task1 se ejecuto en await task2. 
    result2 = await task2
    print("Fetch 2 fully completed")
    result1 = await task1
    print("Fetch 1 fully completed")
    return [result1, result2]

t1 = time.perf_counter()

results = asyncio.run(main())
print(results)

t2 = time.perf_counter()
print(f"Finished in {t2-t1:.2f} seconds")