import asyncio
from modulefinder import test
import time

def sync_function(test_params: str)-> str:
    print("This is a synchronous function")

    time.sleep(0.1)

    return f"Sync Results: {test_params}"

# ASYNC FUNCTION ALSO KNOWN AS A COROUTINE FUNCTION
# Coroutines are functions whose execution we can pause
async def async_function(test_param: str) -> str:
    print("This is an asynchronous coroutine function.")
    # We use asyncio.sleep to pause this coroutine
    await asyncio.sleep(0.1)

    return f"Async Result: {test_param}"


# Función Asincrona
async def futures():
    #sync_result = sync_function("Test")
    #print(sync_result)
    loop = asyncio.get_running_loop()
    # The future don't have any result or exception yet, puede ser cancelada con future.cancel
    future = loop.create_future() # A promise-like object
    print(f"Empty Future: {future}")
    # O finalizada con set_result()
    future.set_result("Future Result: Test")
    # await son objetos que implementan un método especial  __await__() por debajo.
    # Porque no podemos hacer await a una función sincrona o a un time.sleep()?
    # Las librerias sincronas no tienen un mecanismo para trabajar con el event loop, ellas no saben como usar yield control over (basicamente pausarse y sederle el turno al event loop) y reanudarla después. El código sincrono no tiene ese metodo __await()__ que nos permite pausar la ejecución y iniciarla después
    # Cuando tu le das await a algo, lo que le dices al código es que pause la ejecución de la función actual y le des el yield control de vuelta al event loop. 
    future_result = await future
    print(future_result)

    # Existe 3 tipos principales de objetos del tipo await
    # Coroutines: Se crean cuando llamas a una async function
    # Tasks: Son wrappers alrededor de las coroutines que están programadas en el event loop
    # Futures: Son objetos de bajo nivel que representan eventos eventuales. Son similares a promises en js, donde hay una promesa de que un resultado este disponible luego. En python nosotros no trabajamos con futures directamente, nosotros escribimos co-routines y cuando las programamos (schedule them) como tareas, asyncio usa futures por debajo para trackear esos resultados. 
    # Solo usamos futures directamente si estamos escribiendo codigo asyncio de bajo nivel.


# We have the coroutines function, that we define with async def keywords. Then is the coroutine object, which is the awaitable that gets returned when you call this funcion
async def coroutines():

    # corotine_obj <- coroutine object = async_function("Test") <- coroutine function
    # Coroutines are like generators in the sense that they suspend execution and resume later, but they're designed to work with an event loop. They have extra features that asyncio needs to schedule them, await io and coordinate multiple tasks
    coroutine_obj = async_function("Test")
    # We don't execute directly that function (async_function()), we create a coroutine objet, and we run it when we await it

    print(coroutine_obj)
    # When we await that coroutine object, we can see that's whenever it runs the print statement and then we got the result
    # When we await a coroutine object with await, it's bouth scheduled on the event loop and run to completion at the same time
    coroutine_result = await coroutine_obj
    print(coroutine_result)

async def main():

    # Tasks are wrapped coroutines that can be executed independently. Task are how we actually run coroutines concurrently. When you wrap a coroutine in a task using asyncio.create_task(), its handle over to the event loop and scheduled to run whenever it gest a chance. The task will keep track of whenever the coroutine finished succesfullt, raised an error or got cancel just like a future would. And in fact, tasks are futures under the hood, but with extra logic to actually run the coroutine and do the work that we want to do
    # But unlike coroutine objects, tasks can be scheduled on the event loop and just sit there without being run until the loop gets control. And this is the key to asyncio, you can queue up multiple tasks at once and them the event loop will be able to run them whenever it's ready or lettiing them take turns while waiting on IO.
    task = asyncio.create_task(async_function("Test"))
    print(task)

    task_result = await task
    print(task_result)

if __name__ == '__main__':
    # No la podemos llamarla, para iniciar esta función tenemos que usar algo llamado event loop. El event loop es el engranaje que ejecuta y maneja funciones asincronas. Es como un calendario, mantiene una traza de todas nuestras tareas y cuando una tarea es suspendida porque esta esperando algo más, el control regresa al event loop, para luego buscar otra tarea para iniciarla o reanudarla luego.
    asyncio.run(main())

# Pero no queremos solo correr funciones sincronas dentro de nuestro event loop, nosotros queremos usar concurrencia