# Usar Scalene con Jupyter Notebooks

Scalene tiene soporte nativo para Jupyter notebooks mediante una extensión de IPython.

## Instalación

Si ya tienes Scalene instalado (está en tu `pyproject.toml`), solo necesitas cargar la extensión en tu notebook.

## Uso en Jupyter Notebook

### 1. Cargar la extensión

En la primera celda de tu notebook:

```python
%load_ext scalene
```

Deberías ver un mensaje confirmando que se cargó correctamente.

### 2. Profilar una línea de código

Usa `%scrun` para profilear una sola línea:

```python
%scrun mi_funcion_lenta()
```

### 3. Profilar una celda completa

Usa `%%scalene` al inicio de la celda:

```python
%%scalene
# Tu código aquí
import time
import requests

def descargar_datos():
    response = requests.get("https://api.example.com/data")
    return response.json()

resultado = descargar_datos()
```

### 4. Profilar con opciones

Puedes pasar opciones a Scalene:

```python
%%scalene --cpu-only
# Solo profilear CPU (sin memoria)
mi_codigo_intensivo_cpu()
```

```python
%%scalene --memory-only
# Solo profilear memoria (sin CPU)
mi_codigo_que_usa_mucha_memoria()
```

## Ejemplo completo

```python
# Celda 1: Cargar extensión
%load_ext scalene

# Celda 2: Definir función
def process_image(image_path):
    from PIL import Image
    img = Image.open(image_path)
    # Procesamiento pesado
    data = list(img.getdata())
    # ... más código ...
    return processed_data

# Celda 3: Profilear la función
%%scalene
result = process_image("mi_imagen.jpg")
```

## Limitaciones en Jupyter

⚠️ **Importante:**
- En **macOS**, Scalene **no puede profilear procesos secundarios** en Jupyter
- Si usas `multiprocessing`, evita Scalene en el notebook
- El profiling de **memoria completo** puede estar limitado en notebooks
- Para análisis completo, usa Scalene desde línea de comandos

## Alternativa: Convertir notebook a script

Si necesitas profiling completo:

```bash
# Convertir notebook a script
jupyter nbconvert --to script mi_notebook.ipynb

# Profilear el script
uv run scalene --html mi_notebook.py
```

## Ejemplo práctico con asyncio

```python
# Celda 1
%load_ext scalene

# Celda 2
import asyncio
import requests
from pathlib import Path

async def download_image(url: str):
    response = requests.get(url)
    return response.content

# Celda 3: Profilear la descarga
%%scalene
urls = ["https://example.com/img1.jpg", "https://example.com/img2.jpg"]
results = await asyncio.gather(*[download_image(url) for url in urls])
```

## Tips

1. **Usa `%scrun`** para funciones individuales rápidas
2. **Usa `%%scalene`** para celdas completas con múltiples operaciones
3. **En macOS**, evita profilear código con `multiprocessing`
4. **Para análisis profundo**, convierte a script y usa línea de comandos
5. **El output** se muestra directamente en el notebook después de ejecutar

## Comparación

| Método | CPU | Memoria | GPU | Procesos secundarios |
|--------|-----|---------|-----|---------------------|
| `%%scalene` en notebook | ✅ | ⚠️ Limitado | ✅ | ❌ (macOS) |
| `scalene script.py` | ✅ | ✅ | ✅ | ✅ |

