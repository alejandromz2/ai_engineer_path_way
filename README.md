# Plan de aprendizaje para AI Engineer (Checklist + orden + temario profundo)  
**Objetivo:** prepararte para roles competitivos de **AI Engineer** con foco en **producción**, **MLOps/LLMOps**, **LLMs/RAG**, **cloud**, **seguridad** y **compliance**.

---

## Orden recomendado de aprendizaje (roadmap por fases)

### Fase 0 — Base imprescindible (2–6 semanas)
**Objetivo:** escribir software Python serio + hábitos de ingeniería.

**Python “production-grade” (Muy alta)**
- [ ] Python avanzado: typing (`typing`, `Protocol`, `TypedDict`), dataclasses, context managers  
- [ ] Concurrencia: `asyncio`, `httpx`, `aiohttp`, pools, backpressure  
- [X] Packaging: `pyproject.toml`, `poetry`/`uv`, versionado semver, wheels  
- [ ] Calidad: `ruff`, `mypy/pyright`, `pytest`, `hypothesis`, coverage  
- [ ] Performance: profiling (`cProfile`, `py-spy`), memoria, vectorización (NumPy)  
- [ ] Logging serio: logging JSON, correlación de requests (trace/span ids)
- [ ] Patrones de diseño “core” en Python: Strategy, Factory, Adapter, Decorator (casos reales)
- [ ] Principios SOLID + “composition over inheritance” (cuándo sí/no)
- [ ] Patrones de concurrencia: producer/consumer, fan-out/fan-in, bounded queues (backpressure)
- [ ] Patrón Result/Either para errores (evitar excepciones como flow control)
- [ ] Patrón Ports & Adapters (interfaces Protocol + adapters concretos) para aislar infra (DB/HTTP/LLM)
- [ ] Performance “bajo nivel”: Cython / PyO3 (Rust) / C-extensions (1 mini ejemplo)
- [ ] Profiling avanzado: flamegraphs, perf/py-spy, análisis de hotspots
- [ ] Estructuras de datos/algos prácticos (lo necesario para interviews): heaps, hashing, big-O, tradeoffs

**Mini-entregable**
- [ ] Repo plantilla “prod-ready” (API + tests + CI) 
- [ ] Incluir ejemplos reales de patrones en el repo: strategy/, factory/, adapter/, decorator/, result/
- [ ] Micro-módulo “perf lab”: una función lenta + 3 optimizaciones (vectorización, caching, extensión nativa)

---

### Fase 1 — Backend & APIs (4–8 semanas)
**Objetivo:** AI Engineer suele ser “backend engineer con ML/LLMs”.

**APIs (Muy alta)**
- [ ] FastAPI: routers, dependencies, background tasks, streaming responses  
- [ ] Pydantic v2: validators, settings, schemas estables  
- [ ] AuthN/AuthZ: JWT/OAuth2, scopes, RBAC básico  
- [ ] Observabilidad: OpenTelemetry (traces/metrics/logs)  
- [ ] Seguridad: rate limit, input validation, secrets, CORS, threat model básico  
- [ ] Patrones para APIs robustas: Service layer, Repository, Unit of Work (transacciones)
- [ ] Patrones de resiliencia (implementación): retry + jitter, circuit breaker, bulkhead, timeout budgets
- [ ] Patrón Idempotency-Key (Command handling) + Outbox pattern (eventos confiables)
- [ ] Patrones de integración: Anti-corruption layer (ACL), Strangler Fig (migraciones progresivas)
- [ ] Patrones de arquitectura para servicios AI: BFF, API Gateway, Backends for Frontends
- [ ] Multi-tenant serio: quotas, rate-limit por tenant, aislamiento, “plans” (free/pro)
- [ ] Feature flags (rollout seguro): feature gates + kill-switch para LLMs

**Datos de app (Alta)**
- [ ] PostgreSQL: diseño de schema, índices, `EXPLAIN ANALYZE`, migrations (Alembic)  
- [ ] Caching: Redis (TTL, cache-aside, locks)  
- [ ] Colas: Pub/Sub / SQS / Kafka (elige 1 y domina)
- [ ] Patrón CQRS-lite (separar queries/commands cuando crece)
- [ ] Patrón Cache-aside + single-flight (evitar thundering herd)
- [ ] Postgres avanzado: locks, isolation levels, deadlocks, connection pooling (pgBouncer)
- [ ] Cache patterns avanzados: write-through, write-behind, invalidación consistente

**Mini-entregable**
- [ ] “AI API” con auth + observabilidad + postgres + redis
- [ ] Documentar 3 ADRs: “Service layer”, “Repository/UoW”, “Idempotencia + Outbox”

---

### Fase 2 — ML Fundamentals (6–10 semanas)
**Objetivo:** entender de verdad training, evaluación, generalización.

**Fundamentos (Muy alta)**
- [ ] Bias/variance, overfitting, regularización  
- [ ] Validación: train/val/test, CV, leakage, métricas por caso  
- [ ] Modelos clásicos: regresión, árboles, ensembles, calibración  
- [ ] Feature engineering y pipelines  
- [ ] Interpretabilidad básica: SHAP/LIME (cuándo sí/cuándo no)  
- [ ] Data-centric AI: label quality, noise, guidelines de etiquetado, active learning básico
- [ ] Fairness/robustez básico: métricas por segmento, evaluación bajo shift, stress tests
- [ ] Fundamentos de Reinforcement Learning (bandits + MDP a nivel conceptual)

**Librerías (Alta)**
- [ ] scikit-learn (pipelines, model selection)  
- [ ] NumPy/Pandas (sin anti-patrones)

**Mini-entregable**
- [ ] Pipeline ML reproducible + reporte de evaluación
- [ ] “Evaluation pack”: reporte con métricas globales + por segmento + checklist de leakage

---

### Fase 3 — Deep Learning (6–10 semanas)
**Objetivo:** PyTorch “real”, entrenamiento, optimización y debugging.

**PyTorch (Muy alta)**
- [ ] Autograd, módulos, dataloaders, mixed precision  
- [ ] Optimizers, schedulers, regularización  
- [ ] Debug: exploding/vanishing gradients, overfit controlado  
- [ ] Checkpoints, reproducibilidad, seeds, determinismo  
- [ ] Entrenamiento distribuido (concepto + práctica mínima)
- [ ] Entrenamiento eficiente: gradient accumulation, checkpointing, DDP conceptos + 1 práctica
- [ ] Debugging “real”: data bugs, shape bugs, NaNs, AMP issues, determinismo vs performance

**TensorFlow (Media, pero útil)**
- [ ] Keras training loops + serving básico  

**RLHF / Alignment (Media–Alta)**
- [ ] RLHF/Alignment: SFT vs DPO vs PPO (concepto + cuándo usar)
- [ ] Preference data: recolección, sesgos, evaluación

**Mini-entregable**
- [ ] Fine-tuning pequeño + tracking de experimentos

---

### Fase 4 — LLMs en producción (8–12 semanas)
**Objetivo:** LLM orchestration + RAG + evaluación seria.

**Hugging Face (Alta)**
- [ ] Transformers: tokenización, modelos, pipelines  
- [ ] Fine-tuning: LoRA/QLoRA (conceptos + 1 práctica)  
- [ ] Datasets, collation, eval básica  

**LLM APIs (Muy alta)**
- [ ] OpenAI / Azure OpenAI / Anthropic / Gemini: prompts, tools, streaming  
- [ ] Manejo de errores: timeouts, retries, idempotencia, circuit breakers  
- [ ] Costing: tokens, caching, batching, modelos por tarea 
- [ ] Patrones de orquestación: Router (modelo por tarea), Fallback chain, Circuit breaker por proveedor
- [ ] Patrón Schema-first: contrato JSON (Pydantic) + repair controlado (reintentos con límites)
- [ ] Patrón Prompt registry (versionado de prompts + changelog) + tests tipo golden
- [ ] Observabilidad LLM: tracing por paso (prompt → tools → retrieval → respuesta) + costos por request
- [ ] Red teaming básico: pruebas sistemáticas de jailbreak / prompt injection y hardening

**Prompt/Context engineering (Muy alta)**
- [ ] Instrucciones vs ejemplos vs herramientas  
- [ ] Guardrails: formato estricto (JSON schema), rechazo seguro  
- [ ] Mitigación: prompt injection, data exfiltration, jailbreaks (práctica)
- [ ] Patrones “agentic” seguros: ReAct, Plan-and-Execute, Tool sandboxing (mínimos permisos)
- [ ] Patrón Policy gate (validación antes/después del LLM: input/output filters)
- [ ] “System safety patterns”: allowlist de tools, permisos mínimos, sandboxing, tool output validation
- [ ] Evaluación de prompts: regresiones con golden tests + pruebas metamórficas (consistencia)

---

### Fase 5 — RAG “de verdad” (8–12 semanas)
**Objetivo:** retrieval, chunking, reranking, evaluación.

**Componentes (Muy alta)**
- [ ] Ingesta: parsing, normalización, deduplicación, metadata  
- [ ] Chunking: por estructura, por tokens, overlap, híbridos  
- [ ] Embeddings: selección, dimensionalidad, normalización, batching  
- [ ] Vector DB: **Qdrant** o **pgvector** (elige 1 profundo)  
- [ ] Híbrido: BM25 + vector (OpenSearch/Elasticsearch o equivalente)  
- [ ] Reranking: cross-encoders / LLM-as-reranker (pros/cons)  
- [ ] Query rewriting: multi-query, HyDE, decomposición  
- [ ] Citations y grounding: evidencias, trazabilidad  
- [ ] Patrón Retrieval pipeline modular (ingest → index → retrieve → rerank → generate) con interfaces
- [ ] Patrón Query planner (decomposición) + tool routing (SQL vs vector vs BM25)
- [ ] Patrón Grounded answer contract: “respuesta + citas + confianza + ‘no sé’” como esquema estable
- [ ] RAG para documentos complejos: PDFs con tablas/imágenes, layout parsing, document QA
- [ ] Pipelines de ingesta “enterprise”: incremental updates, versionado de chunks, invalidación de embeddings
- [ ] Multimodal RAG (nivel introductorio): embeddings de imagen + texto, búsqueda cruzada, casos de uso

**Frameworks (Alta)**
- [ ] LangChain (velocidad) **y/o** LangGraph (control, agentes)  
- [ ] Evaluación RAG: recall@k, MRR, faithfulness, answer relevance  
- [ ] Frameworks de evaluación RAG/LLM (elige 1): Ragas / TruLens / DeepEval (1 integrado en CI)


**Mini-entregable**
- [ ] RAG con evaluación automática + panel de métricas
- [ ] “RAG eval harness” con suites por componente (chunking/retrieval/rerank/generation) y regressions

---

### Fase 6 — Serving & Performance (6–10 semanas)
**Objetivo:** servir LLMs y modelos con latencia/costo controlado.

**Serving (Alta/Muy alta)**
- [ ] vLLM o TGI (elige 1): batch, KV cache, throughput  
- [ ] Cuantización: int8/int4 (conceptos + impacto real)  
- [ ] GPU basics: VRAM, batch size, OOM debugging  
- [ ] Streaming responses (UX + costos)  
- [ ] Serving en GPU en serio: colas, batch scheduler, límites de concurrencia, warmup, OOM playbook
- [ ] Model routing por latencia/costo: cheap model → fallback a strong model (políticas)

**Optimización (Alta)**
- [ ] Caching semántico / response cache  
- [ ] RAG caching (embeddings, retrieval results)  
- [ ] Profiling de endpoints y colas
- [ ] Patrones de performance: batching, request coalescing, token budgeter, streaming-first UX
- [ ] Patrón Rate limiting por tenant + priority queues (SLA por tipo de cliente)
- [ ] “Speculative decoding / prompt caching” (conceptos + cuándo sirve)
- [ ] Performance testing: k6/locust para endpoints (p95/p99, SLOs)

---

### Fase 7 — MLOps/LLMOps (8–12 semanas)
**Objetivo:** lifecycle completo: experimentos → registry → deploy → monitoreo.

**MLflow (Muy alta)**
- [ ] Tracking: params/metrics/artifacts  
- [ ] Model Registry: stages, versionado, approvals  
- [ ] Serving/packaging: pyfunc, reproducibilidad  

**Pipelines y calidad (Alta)**
- [ ] Orquestación: Airflow / Prefect (elige 1 profundo)  
- [ ] Data quality: Great Expectations (o similar)  
- [ ] Feature store: Feast / Vertex Feature Store (según cloud)
- [ ] Patrones de release: blue/green, canary, shadow testing (especialmente para LLMs)
- [ ] Patrón Model/Prompt registry unificado (versionado + aprobaciones + rollback)
- [ ] Experiment design: A/B testing y evaluación offline vs online (tradeoffs)
- [ ] Dataset/versioning: DVC/LakeFS (elige 1) para datasets y artefactos grandes
- [ ] CI para LLMs: suites de evaluación + “gates” por calidad/costo/latencia antes de deploy

**Monitoreo (Muy alta)**
- [ ] Model monitoring: drift, performance, data quality  
- [ ] LLM monitoring: safety signals, calidad, costo por request  
- [ ] Observabilidad: OpenTelemetry + Prometheus/Grafana
- [ ] Patrones de monitoreo LLM: SLOs (latencia/costo/calidad), error budgets, alertas por regresión
- [ ] Monitoreo de seguridad LLM: señales de exfiltración, PII leakage, tool misuse, anomalías
- [ ] Feedback loop: thumbs up/down + triage + dataset de mejora continua

---

### Fase 8 — Cloud + DevOps + Seguridad (continuo)
**Objetivo:** en Suiza/Alemania se valora muchísimo “operar” soluciones.

**Contenedores y K8s (Muy alta)**
- [ ] Docker: multi-stage, slim images, SBOM  
- [ ] Kubernetes: deployments, HPA, configmaps, secrets, ingress  
- [ ] CI/CD: GitHub Actions/GitLab CI (tests, build, deploy)  
- [ ] IaC: Terraform (mínimo 1 cloud)
- [ ] Patrones K8s: sidecar, init containers, pod disruption budgets, graceful shutdown
- [ ] Patrones “12-factor app” (config/ports/logs) aplicado a servicios de AI

**Cloud (Muy alta)**
- [ ] AWS o GCP (elige 1 profundo, el otro “funcional”)  
  - [ ] IAM, networking, logging/monitoring  
  - [ ] Compute: Cloud Run/ECS/EKS  
  - [ ] Storage: S3/GCS, lifecycle, encryption  
  - [ ] Data: BigQuery/Redshift + pipelines  
  - [ ] Networking serio: VPC/VNet, private endpoints, NAT, service perimeter, egress control
  - [ ] Secrets & keys: KMS + Secret Manager + rotación + “least privilege” IAM
  - [ ] Compliance ops: auditoría, access logs, immutable logs, trazabilidad end-to-en
**Seguridad/Privacidad (Muy alta en Europa)**
- [ ] GDPR: principios/obligaciones (minimización, finalidad, etc.)  
- [ ] Suiza nFADP (nuevo marco suizo)  
- [ ] EU AI Act: marco, categorías de riesgo, obligaciones clave  
- [ ] PII redaction: DLP (GCP DLP / AWS Macie o equivalente)  
- [ ] Policy & governance: retention, access logs, audit trails
- [ ] Threat modeling aplicado a LLM apps (STRIDE-lite) + controles
- [ ] Secure SDLC: SAST/DAST, dependencia (SBOM), políticas de PR, firmas de artifacts
- [ ] On-prem / air-gapped constraints (muy EU): despliegue sin salida a internet, artefactos firmados
---

## Checklist “Herramientas a aprender” (importancia + orden)

### Nivel 1 (Sí o sí, base)
- [ ] **Python** (typing, async, testing)
- [ ] **FastAPI + Pydantic**
- [ ] **PostgreSQL** (+ migrations)
- [ ] **Git + CI/CD**
- [ ] **Docker**
- [ ] **PyTorch**
- [ ] **Hugging Face Transformers**
- [ ] **LLM APIs** (OpenAI/Azure/Anthropic/Gemini)
- [ ] **Vector DB** (Qdrant o pgvector)
- [ ] **Observabilidad** (OpenTelemetry + logs/metrics)
- [ ] **LLM/RAG eval frameworks** (Ragas/TruLens/DeepEval)
- [ ] **Prompt testing** (promptfoo o equivalente)
- [ ] **OCR / Document parsing** (OpenCV + extracción de PDFs/tablas)

### Nivel 2 (Para puestos competitivos)
- [ ] **Kubernetes**
- [ ] **Terraform**
- [ ] **MLflow**
- [ ] **LangGraph** (o LangChain + patrones sólidos)
- [ ] **Reranking + hybrid search** (OpenSearch/Elasticsearch)
- [ ] **Serving LLM** (vLLM o TGI)
- [ ] **Spark / PySpark** (ETL + feature engineering a escala)
- [ ] **OpenSearch/Elasticsearch** (operación + tuning para híbrido)
- [ ] **Secrets/KMS + IAM avanzado** (políticas, least privilege, auditoría)

### Nivel 3 (Diferenciadores top)
- [ ] **Evaluación LLM/RAG** (framework + métricas + datasets)
- [ ] **LLMOps** (monitoring seguridad/costo/calidad)
- [ ] **Data quality** (Great Expectations)
- [ ] **Security scanning** (Trivy/Snyk), SBOM, supply chain security
- [ ] **Multi-tenant SaaS patterns** (auth, cuotas, aislamiento, billing)
- [ ] **Databricks/Delta Lake** (si apuntas a enterprise US/EU)
- [ ] **Rust/C++ para performance** (1 integración real)
- [ ] **LLM Security** (red teaming + guardrails + auditoría de tools)

---

## Temario detallado por bloques (lo que debes dominar)

### A) Software Engineering (Python)
- Arquitectura: clean architecture, hexagonal, DDD-lite  
- Testing: unit/integration/contract tests, mocks, golden tests para prompts  
- APIs: versionado, pagination, idempotency keys  
- Resiliencia: retries/backoff, circuit breakers, bulkheads  
- Performance: profiling, async IO, colas, caching  
- Documentación: ADRs, runbooks, diagrams (C4)
- Patrones GoF aplicados a AI systems: Strategy (selección de modelo), Factory (clients/providers), Adapter (proveedores), Decorator (telemetría/caching), Observer (eventos), Command (jobs), Template Method (pipelines)
- Patrones de arquitectura: Service layer, Repository, UoW, Ports & Adapters, CQRS-lite, Event-driven (cuando escala)
- Patrones de testing para LLM/RAG: golden tests, contract tests, metamorphic tests (consistencia), replay fixtures
- Patrones de configuración: settings schema + feature flags (rollout seguro)

### B) ML / Deep Learning
- Data prep: leakage, feature drift, label noise  
- Training: early stopping, schedulers, regularización  
- Evaluación: métricas por segmento, calibración, fairness básico  
- Reproducibilidad: seeds, tracking, model cards

### C) NLP / LLMs
- Tokenización, contexto, embeddings vs generativos  
- Fine-tuning: LoRA/QLoRA, instrucciones, overfit en pocos datos  
- Tool use: function calling, schema enforcement, error handling  
- Seguridad LLM: prompt injection, untrusted retrieval, sandboxing de tools

### D) RAG & Search
- Indexación: chunking por estructura, metadata, incremental updates  
- Retrieval: dense, sparse, hybrid; tuning de k  
- Reranking: cross-encoder y tradeoffs latencia/costo  
- Grounding: citas, verificación, “don’t know” behavior  
- Evaluación: datasets, judge models, métricas automáticas + revisión humana

### E) Serving / Infra
- Deploy: cloud run / k8s, autoscaling, blue-green, canary  
- GPU: scheduling, batch, KV cache, OOM handling  
- Observabilidad: tracing end-to-end (API → retrieval → LLM)  
- Cost: token budgeting, caching, rate limiting por tenant

### F) MLOps/LLMOps & Governance
- MLflow: tracking + registry + packaging  
- Monitoreo: drift, data quality, performance, alerting  
- Compliance: GDPR/nFADP + AI Act (riesgos, documentación, trazabilidad)  
- Privacidad: PII discovery/redaction, retention, access control

---

## 6 proyectos de portafolio que te abren puertas (DE/AI Engineer)
- [ ] **RAG empresarial** con Qdrant + reranking + evaluación + panel  
- [ ] **Agente LangGraph** con tools (SQL, web, tickets) + guardrails  
- [ ] **MLflow en cloud** (tracking + registry) + CI/CD deploy  
- [ ] **Serving** con vLLM/TGI (latencia/throughput medidos)  
- [ ] **Multi-tenant SaaS AI** (cuotas, auth, observabilidad, billing simple)  
- [ ] **Compliance pack**: data flow diagram + DPIA-lite + redaction pipeline
- [ ] **Multimodal Doc Agent**: RAG sobre PDFs con tablas/imágenes + OCR + citas verificables
- [ ] **LLM Red-Team Harness**: batería de ataques + reportes + hardening + métricas
- [ ] **Big Data + ML pipeline**: ETL en Spark + training + MLflow + deploy + monitoreo