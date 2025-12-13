# Fase 0 — Checklist semanal (6 semanas) + cursos/recursos (con links)

> Objetivo: terminar con un **repo plantilla “production-grade”** (CI + lint/format + tests + typing + async + packaging + observabilidad + profiling) que puedas clonar para cualquier proyecto de AI Engineer.

---

## Orden recomendado (6 semanas)
- **Semana 0:** Setup del repo + CI mínimo
- **Semana 1:** Ruff + pre-commit + estándares de proyecto
- **Semana 2:** Testing pro con pytest (fixtures/patterns, parametrización, mocking)
- **Semana 3:** Typing serio + mypy/pyright (strict progresivo)
- **Semana 4:** Concurrencia (asyncio vs threads vs multiprocessing)
- **Semana 5:** Packaging + pyproject + entornos + versionado (SemVer + changelog)
- **Semana 6:** Logging estructurado + observabilidad + profiling/performance

---

## Recursos base (usa durante toda la Fase 0)
- [Modern Python Projects: From Editor to Deployment (Talk Python)](https://training.talkpython.fm/courses/modern-python-projects) — packaging, tooling y workflow moderno.
- [Ruff — Tutorial (Astral Docs)](https://docs.astral.sh/ruff/tutorial/) — linter+formatter moderno.
- [pre-commit (sitio oficial)](https://pre-commit.com/) — hooks para estandarizar repos.
- [pytest — documentación oficial](https://docs.pytest.org/en/stable/) — referencia principal.
- [Python Packaging User Guide (PyPA)](https://packaging.python.org/) — referencia oficial de packaging.

---

# Semana 0 — Setup del repo + CI mínimo
## Cursos/recursos (elige los que te apliquen)
- [Working on projects (uv) — Astral Docs](https://docs.astral.sh/uv/guides/projects/) *(si eliges uv)*
- [The pyproject.toml file (Poetry docs)](https://python-poetry.org/docs/pyproject/) *(si eliges Poetry)*
- [Modern Python Projects (Talk Python)](https://training.talkpython.fm/courses/modern-python-projects)

## Checklist
- [ ] Crear repo `python-prod-template/`
- [ ] Elegir **1** gestor de entorno: **uv** o **Poetry** (no mezclar)
- [ ] Crear estructura base:
  - [ ] `src/<package_name>/...`
  - [ ] `tests/`
  - [ ] `README.md`
  - [ ] `pyproject.toml`
- [ ] CI mínimo (GitHub Actions o GitLab CI):
  - [ ] correr `pytest`
  - [ ] correr `ruff check` + `ruff format --check`
- [ ] Agregar comandos “de trabajo” al README (o Makefile):
  - [ ] `lint`
  - [ ] `format`
  - [ ] `test`

**Entregable:** repo inicial con CI corriendo en cada push/PR.

---

# Semana 1 — Tooling moderno: Ruff + pre-commit + estándares
## Cursos/recursos
- [Ruff — Tutorial (Astral Docs)](https://docs.astral.sh/ruff/tutorial/)
- [Ruff — Configuración (Astral Docs)](https://docs.astral.sh/ruff/configuration/)
- [Supported hooks (pre-commit)](https://pre-commit.com/hooks.html)
- [pre-commit-hooks (repo oficial)](https://github.com/pre-commit/pre-commit-hooks)

## Checklist
- [ ] Configurar Ruff (lint + format) en `pyproject.toml`
- [ ] Configurar `pre-commit` con hooks:
  - [ ] ruff (lint)
  - [ ] ruff-format
  - [ ] hooks básicos (whitespace, eof, yaml, etc.)
- [ ] Ejecutar y dejar limpio: `pre-commit run -a`
- [ ] Integrar en CI: `ruff check .` y `ruff format --check .`

**Entregable:** `pre-commit` instalado y CI “verde” con lint/format.

---

# Semana 2 — Testing pro con pytest (fixtures/patterns)
## Cursos/recursos
- [Pragmatic pytest: Getting started for Python devs (Talk Python)](https://training.talkpython.fm/courses/getting-started-with-testing-in-python-using-pytest)
- [pytest — How to use fixtures](https://docs.pytest.org/en/stable/how-to/fixtures.html)
- [pytest — Parametrize](https://docs.pytest.org/en/stable/how-to/parametrize.html)
- [Five Advanced Pytest Fixture Patterns (InspiredPython)](https://www.inspiredpython.com/article/five-advanced-pytest-fixture-patterns)

## Checklist
- [ ] Configurar pytest (ini o `pyproject.toml`)
- [ ] Aprender/aplicar:
  - [ ] fixtures (scope, factories-as-fixtures)
  - [ ] parametrización
  - [ ] monkeypatch/mocking (sin abusar)
- [ ] Escribir tests reales:
  - [ ] tests unitarios (funciones puras)
  - [ ] tests de integración ligeros (ej. sqlite in-memory o fakes)
- [ ] (Opcional recomendado) Coverage en CI

**Entregable:** suite de tests útil y mantenible (no “tests de mentira”).

---

# Semana 3 — Typing serio + mypy/pyright (strict progresivo)
## Cursos/recursos
- [Rock Solid Python: Type Hints & Modern Tools (Talk Python)](https://training.talkpython.fm/courses/python-type-hint-course-with-hands-on-examples)
- [Mypy — Getting started](https://mypy.readthedocs.io/en/stable/getting_started.html)
- [Pyright — sitio oficial](https://microsoft.github.io/pyright/)
- [Pyright — configuration (strict rules)](https://github.com/microsoft/pyright/blob/main/docs/configuration.md)
- [Python docs — typing](https://docs.python.org/3/library/typing.html)

## Checklist
- [ ] Implementar typing en 1–2 módulos “core” primero (no todo el repo de golpe)
- [ ] Dominar y usar (con ejemplos reales en tu código):
  - [ ] `TypedDict` (estructuras tipo JSON)
  - [ ] `Protocol` (interfaces)
  - [ ] `Literal`, `Final`
  - [ ] `Annotated` (metadatos/validación)
  - [ ] generics: `TypeVar`, `Generic`
- [ ] Activar type-check en CI (strict progresivo):
  - [ ] mypy `--strict` o pyright `typeCheckingMode=strict` (por carpetas o archivos)

**Entregable:** type-check pasa en módulos importantes y corre en CI.

---

# Semana 4 — Concurrencia: asyncio vs threads vs multiprocessing
## Cursos/recursos
- [Async, Threads, and Multiprocessing Deep Dive (Talk Python)](https://training.talkpython.fm/courses/python-concurrency-deep-dive)
- [Python's asyncio: A Hands-On Walkthrough (Real Python)](https://realpython.com/async-io-python/)
- [Python docs — asyncio](https://docs.python.org/3/library/asyncio.html)

## Checklist
- [ ] Claridad de decisión:
  - [ ] cuándo usar asyncio (I/O-bound)
  - [ ] cuándo threads (I/O blocking / libs no-async)
  - [ ] cuándo multiprocessing (CPU-bound)
- [ ] asyncio “de verdad”:
  - [ ] timeouts
  - [ ] cancellation (bien hecho)
  - [ ] semáforos para limitar concurrencia
  - [ ] colas para backpressure
- [ ] Mini demo:
  - [ ] simular 500–2000 tareas I/O con límite de concurrencia y retries
  - [ ] logging de errores y timeouts (sin “task leaked”)

**Entregable:** módulo `concurrency_demo/` con README explicando tus decisiones.

---

# Semana 5 — Packaging + pyproject + entornos + versionado
## Cursos/recursos
- [Writing your pyproject.toml (PyPA)](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [Packaging Python Projects (PyPA)](https://packaging.python.org/tutorials/packaging-projects/)
- [Managing Python Projects With uv (Real Python)](https://realpython.com/python-uv/) *(si eliges uv)*
- [Locking and syncing (uv) — Astral Docs](https://docs.astral.sh/uv/concepts/projects/sync/) *(si eliges uv)*
- [Poetry docs (home)](https://python-poetry.org/docs/) *(si eliges Poetry)*
- [Semantic Versioning 2.0.0](https://semver.org/)
- [Keep a Changelog 1.1.0](https://keepachangelog.com/en/1.1.0/)

## Checklist
- [ ] `pyproject.toml` completo:
  - [ ] metadata del proyecto
  - [ ] dependencias y dev-deps
  - [ ] extras (opcional)
- [ ] Reproducibilidad:
  - [ ] lockfile (uv.lock o poetry.lock) y flujo de `sync/install`
- [ ] Build de paquete:
  - [ ] generar wheel (build)
  - [ ] instalar el wheel localmente y ejecutar tests
- [ ] Versionado y releases:
  - [ ] adoptar SemVer
  - [ ] mantener `CHANGELOG.md` con Keep a Changelog

**Entregable:** proyecto empaquetable + reproducible + versionable.

---

# Semana 6 — Logging estructurado + observabilidad + profiling/performance
## Cursos/recursos
- [structlog — Getting started](https://www.structlog.org/en/stable/getting-started.html)
- [OpenTelemetry Python — Getting started](https://opentelemetry.io/docs/languages/python/getting-started/)
- [The Python Profilers (cProfile) — docs](https://docs.python.org/3/library/profile.html)
- [py-spy (GitHub)](https://github.com/benfred/py-spy)

## Checklist
- [ ] Logging estructurado:
  - [ ] logs con contexto (request_id / correlation_id)
  - [ ] niveles correctos + sin secretos en logs
  - [ ] formato consistente (JSON/logfmt o similar)
- [ ] Observabilidad (mínimo viable):
  - [ ] instrumentación con OpenTelemetry (traces a consola/collector local)
- [ ] Profiling/performance:
  - [ ] correr `cProfile` o `py-spy` sobre una parte lenta
  - [ ] identificar hot spots y aplicar 1–2 mejoras reales
- [ ] Consolidación final:
  - [ ] CI corre: lint/format + tests + type-check
  - [ ] README: “cómo correr todo” + comandos
  - [ ] checklist de Definition of Done

**Entregable final:** repo plantilla “production-grade” listo para clonar.

---

## Bonus (muy recomendado para LLM/RAG después)
- [Hypothesis — Introduction (property-based testing)](https://hypothesis.readthedocs.io/en/latest/tutorial/introduction.html)
- [Hypothesis — docs](https://hypothesis.readthedocs.io/)
- [Test-Driven Development with FastAPI and Docker (TestDriven.io)](https://testdriven.io/courses/tdd-fastapi/)

---

## Cómo marcar progreso
- Marca los checkboxes completados.
- En cada semana, intenta dejar un **PR** con:
  - Qué cambió
  - Qué aprendiste
  - Qué queda pendiente
  - Evidencia (CI verde, outputs, traces o profiling)
