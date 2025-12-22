# Ruff y Pre-commit

## Solución al warning de `uv sync`

Si ves este warning:
```
warning: `VIRTUAL_ENV=/Users/.../FASE 0/.venv` does not match the project environment path
```

**Solución:** Desactiva el entorno virtual activo antes de hacer `uv sync`:

```bash
# Desactivar el entorno virtual actual
deactivate

# Luego hacer sync
uv sync
```

O simplemente ignora el warning - `uv` creará y usará su propio entorno virtual en `.venv`.

## Usar ruff

Después de `uv sync`, usa ruff con `uv run`:

```bash
# Verificar errores
uv run ruff check main.py

# Auto-fix errores
uv run ruff check --fix main.py

# Formatear código
uv run ruff format main.py
```

## Alternativa: Activar el entorno de uv

Si prefieres usar el entorno directamente:

```bash
# Activar el entorno de uv
source .venv/bin/activate

# Ahora puedes usar ruff directamente
ruff check main.py
```

