# Fase 0 - Semana 4: Concurrencia (asyncio vs threads vs multiprocessing)

## Asyncio (Python)

### Intuición rápida (analogía)
- **Síncrono:** como un Subway: toman tu pedido y lo preparan completo antes de atender al siguiente.
- **Asíncrono:** como un McDonald’s: toman tu pedido, lo “enciolan”, y mientras tanto atienden a otros clientes.

> Importante: **asíncrono ≠ más rápido** por defecto.  
> Asíncrono significa “mejor aprovechamiento del tiempo de espera”, no “más CPU”.

### Qué es `asyncio`
- `asyncio` habilita **concurrencia** usando **multitarea cooperativa**:
  - Las *coroutines* avanzan hasta encontrar un `await`.
  - En ese `await`, **ceden el control** al *event loop*, que puede ejecutar otras tareas.
- En la práctica, `asyncio` suele correr en **un solo hilo (single-threaded)** y típicamente en **un solo core** (salvo que explícitamente delegates trabajo a threads/procesos).

### Cuándo brilla
✅ **I/O-bound** (esperas frecuentes):
- Requests HTTP, DB, colas, sockets, lectura/escritura de archivos remotos, etc.
- Cuando el cuello de botella es **“esperar”** (red/disco), `asyncio` puede aumentar mucho el throughput.

### Cuándo NO es la herramienta principal
⚠️ **CPU-bound** (cómputo pesado):
- Si haces cálculo intenso en Python puro, bloquearás el *event loop*.
- Para CPU-bound, lo común es:
  - **Multiprocessing / ProcessPoolExecutor** (paralelismo real en múltiples cores)
  - Librerías que **liberan el GIL** (NumPy, pandas, PyTorch, etc.)
  - O mover trabajo pesado a servicios externos (batch jobs, workers)

### Regla práctica
- **Asyncio = concurrencia eficiente para I/O**
- **Procesos (o GIL-free libs) = paralelismo para CPU**
- Si “se siente lento”, primero identifica si el problema es **I/O** o **CPU**.

## 1) Función síncrona (sync)
- `sync_function(test_params: str) -> str`
- Imprime: `"This is a synchronous function"`
- Usa `time.sleep(0.1)` (bloquea el hilo).
- Retorna: `"Sync Results: ..."`

---

## 2) Función asíncrona (async) / Coroutine function
- `async_function(test_param: str) -> str`
- **ASYNC FUNCTION ALSO KNOWN AS A COROUTINE FUNCTION**
- **Coroutines are functions whose execution we can pause**
- Imprime: `"This is an asynchronous coroutine function."`
- Usa `await asyncio.sleep(0.1)` para “pausar” la coroutine.
- Retorna: `"Async Result: ..."`

---

## 3) Futures (bajo nivel)
- `async def futures():`
- Obtiene el event loop actual:
  - `loop = asyncio.get_running_loop()`
- Crea un future:
  - `future = loop.create_future()` (**A promise-like object**)
  - **The future don't have any result or exception yet**, puede ser cancelada con `future.cancel`
  - Se imprime: `Empty Future: {future}`
- Se completa manualmente:
  - **O finalizada con `set_result()`**
  - `future.set_result("Future Result: Test")`
- Espera el resultado:
  - `future_result = await future`
  - `print(future_result)`

### Apuntes clave sobre `await`
- `await` son objetos que implementan un método especial `__await__()` por debajo.
- ¿Por qué no podemos hacer `await` a una función síncrona o a un `time.sleep()`?
  - Las librerías síncronas no tienen un mecanismo para trabajar con el event loop.
  - No saben cómo **yield control** (pausarse, ceder turno al event loop) y reanudarse después.
  - El código síncrono no tiene ese método `__await()__` que permite pausar y luego continuar.
- Cuando le das `await` a algo:
  - Le dices al código que **pause** la ejecución de la función actual
  - y que **le devuelva el control** al event loop.

### Tipos principales de objetos `awaitable`
- Existen 3 tipos principales de objetos del tipo `await`:
  1. **Coroutines:** se crean cuando llamas a una `async function`
  2. **Tasks:** wrappers alrededor de las coroutines que están programadas en el event loop
  3. **Futures:** objetos de bajo nivel que representan eventos eventuales
     - similares a promises en JS
     - hay una promesa de que un resultado estará disponible luego
     - en Python normalmente no trabajamos con futures directamente:
       - escribimos co-routines y cuando las programamos como tareas, asyncio usa futures por debajo para trackear esos resultados
     - solo usamos futures directamente si estamos escribiendo código asyncio de bajo nivel

---

## 4) Coroutines (coroutine object vs coroutine function)
- `async def coroutines():`
- **We have the coroutines function**, defined with `async def`.
- Luego está el **coroutine object**, que es el awaitable que se retorna cuando llamas esa función.

### Apuntes dentro de `coroutines()`
- `coroutine_obj = async_function("Test")`
  - `corotine_obj <- coroutine object = async_function("Test") <- coroutine function`
- Las coroutines son como generators:
  - suspenden ejecución y se reanudan luego,
  - pero están diseñadas para trabajar con un event loop,
  - tienen features extra que asyncio necesita para:
    - schedule,
    - await io,
    - coordinar múltiples tasks.
- No ejecutamos directamente esa función:
  - creamos un coroutine object, y se corre cuando lo `await`eamos.
- `print(coroutine_obj)`
- `coroutine_result = await coroutine_obj`
  - Cuando `await`eamos un coroutine object:
    - se programa en el event loop
    - y se corre hasta terminar (run to completion) al mismo tiempo.
- `print(coroutine_result)`

---

## 5) Tasks (concurrencia real)
- `async def main():`
- **Tasks are wrapped coroutines that can be executed independently.**
- Las tasks son como realmente corremos coroutines concurrentemente.
- Al envolver una coroutine en una task con `asyncio.create_task()`:
  - se entrega al event loop,
  - se programa para correr cuando tenga oportunidad.
- La task trackea si la coroutine:
  - terminó con éxito,
  - lanzó error,
  - fue cancelada,
  - igual que un future.
- **Tasks are futures under the hood**, pero con lógica extra para ejecutar la coroutine y hacer el trabajo.

### Diferencia clave: coroutine object vs task
- A diferencia del coroutine object:
  - una task puede estar programada en el event loop y quedarse “ahí”
  - sin correr hasta que el loop tenga control.
- Esto es clave para asyncio:
  - puedes encolar múltiples tasks a la vez,
  - y el event loop las corre cuando esté listo
  - o las hace turnarse mientras esperan por IO.

### Uso dentro de `main()`
- `task = asyncio.create_task(async_function("Test"))`
- `print(task)`
- `task_result = await task`
- `print(task_result)`

---

## 6) Event loop y arranque del programa
- `if __name__ == '__main__':`
- No podemos “llamar” directamente a una async function para iniciarla.
- Para iniciar se usa el **event loop**.
- El event loop:
  - ejecuta y maneja funciones asíncronas,
  - es como un calendario: mantiene traza de todas nuestras tareas,
  - cuando una tarea se suspende (porque espera algo),
    - el control regresa al event loop,
    - y busca otra tarea para iniciarla o reanudarla luego.
- Se ejecuta:
  - `asyncio.run(main())`

---

## 7) Nota final
- `# Pero no queremos solo correr funciones sincronas dentro de nuestro event loop, nosotros queremos usar concurrencia`


Python Asyncio -> https://www.youtube.com/watch?v=oAkLSJNr5zY

# 53:51
