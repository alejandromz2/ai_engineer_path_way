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

**Mini-entregable**
- [ ] Repo plantilla “prod-ready” (API + tests + CI)

---

### Fase 1 — Backend & APIs (4–8 semanas)
**Objetivo:** AI Engineer suele ser “backend engineer con ML/LLMs”.

**APIs (Muy alta)**
- [ ] FastAPI: routers, dependencies, background tasks, streaming responses  
- [ ] Pydantic v2: validators, settings, schemas estables  
- [ ] AuthN/AuthZ: JWT/OAuth2, scopes, RBAC básico  
- [ ] Observabilidad: OpenTelemetry (traces/metrics/logs)  
- [ ] Seguridad: rate limit, input validation, secrets, CORS, threat model básico  

**Datos de app (Alta)**
- [ ] PostgreSQL: diseño de schema, índices, `EXPLAIN ANALYZE`, migrations (Alembic)  
- [ ] Caching: Redis (TTL, cache-aside, locks)  
- [ ] Colas: Pub/Sub / SQS / Kafka (elige 1 y domina)

**Mini-entregable**
- [ ] “AI API” con auth + observabilidad + postgres + redis

---

### Fase 2 — ML Fundamentals (6–10 semanas)
**Objetivo:** entender de verdad training, evaluación, generalización.

**Fundamentos (Muy alta)**
- [ ] Bias/variance, overfitting, regularización  
- [ ] Validación: train/val/test, CV, leakage, métricas por caso  
- [ ] Modelos clásicos: regresión, árboles, ensembles, calibración  
- [ ] Feature engineering y pipelines  
- [ ] Interpretabilidad básica: SHAP/LIME (cuándo sí/cuándo no)  

**Librerías (Alta)**
- [ ] scikit-learn (pipelines, model selection)  
- [ ] NumPy/Pandas (sin anti-patrones)

**Mini-entregable**
- [ ] Pipeline ML reproducible + reporte de evaluación

---

### Fase 3 — Deep Learning (6–10 semanas)
**Objetivo:** PyTorch “real”, entrenamiento, optimización y debugging.

**PyTorch (Muy alta)**
- [ ] Autograd, módulos, dataloaders, mixed precision  
- [ ] Optimizers, schedulers, regularización  
- [ ] Debug: exploding/vanishing gradients, overfit controlado  
- [ ] Checkpoints, reproducibilidad, seeds, determinismo  
- [ ] Entrenamiento distribuido (concepto + práctica mínima)

**TensorFlow (Media, pero útil)**
- [ ] Keras training loops + serving básico  

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

**Prompt/Context engineering (Muy alta)**
- [ ] Instrucciones vs ejemplos vs herramientas  
- [ ] Guardrails: formato estricto (JSON schema), rechazo seguro  
- [ ] Mitigación: prompt injection, data exfiltration, jailbreaks (práctica)

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

**Frameworks (Alta)**
- [ ] LangChain (velocidad) **y/o** LangGraph (control, agentes)  
- [ ] Evaluación RAG: recall@k, MRR, faithfulness, answer relevance  

**Mini-entregable**
- [ ] RAG con evaluación automática + panel de métricas

---

### Fase 6 — Serving & Performance (6–10 semanas)
**Objetivo:** servir LLMs y modelos con latencia/costo controlado.

**Serving (Alta/Muy alta)**
- [ ] vLLM o TGI (elige 1): batch, KV cache, throughput  
- [ ] Cuantización: int8/int4 (conceptos + impacto real)  
- [ ] GPU basics: VRAM, batch size, OOM debugging  
- [ ] Streaming responses (UX + costos)  

**Optimización (Alta)**
- [ ] Caching semántico / response cache  
- [ ] RAG caching (embeddings, retrieval results)  
- [ ] Profiling de endpoints y colas

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

**Monitoreo (Muy alta)**
- [ ] Model monitoring: drift, performance, data quality  
- [ ] LLM monitoring: safety signals, calidad, costo por request  
- [ ] Observabilidad: OpenTelemetry + Prometheus/Grafana

---

### Fase 8 — Cloud + DevOps + Seguridad (continuo)
**Objetivo:** en Suiza/Alemania se valora muchísimo “operar” soluciones.

**Contenedores y K8s (Muy alta)**
- [ ] Docker: multi-stage, slim images, SBOM  
- [ ] Kubernetes: deployments, HPA, configmaps, secrets, ingress  
- [ ] CI/CD: GitHub Actions/GitLab CI (tests, build, deploy)  
- [ ] IaC: Terraform (mínimo 1 cloud)

**Cloud (Muy alta)**
- [ ] AWS o GCP (elige 1 profundo, el otro “funcional”)  
  - [ ] IAM, networking, logging/monitoring  
  - [ ] Compute: Cloud Run/ECS/EKS  
  - [ ] Storage: S3/GCS, lifecycle, encryption  
  - [ ] Data: BigQuery/Redshift + pipelines  

**Seguridad/Privacidad (Muy alta en Europa)**
- [ ] GDPR: principios/obligaciones (minimización, finalidad, etc.)  
- [ ] Suiza nFADP (nuevo marco suizo)  
- [ ] EU AI Act: marco, categorías de riesgo, obligaciones clave  
- [ ] PII redaction: DLP (GCP DLP / AWS Macie o equivalente)  
- [ ] Policy & governance: retention, access logs, audit trails

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

### Nivel 2 (Para puestos competitivos)
- [ ] **Kubernetes**
- [ ] **Terraform**
- [ ] **MLflow**
- [ ] **LangGraph** (o LangChain + patrones sólidos)
- [ ] **Reranking + hybrid search** (OpenSearch/Elasticsearch)
- [ ] **Serving LLM** (vLLM o TGI)

### Nivel 3 (Diferenciadores top)
- [ ] **Evaluación LLM/RAG** (framework + métricas + datasets)
- [ ] **LLMOps** (monitoring seguridad/costo/calidad)
- [ ] **Data quality** (Great Expectations)
- [ ] **Security scanning** (Trivy/Snyk), SBOM, supply chain security
- [ ] **Multi-tenant SaaS patterns** (auth, cuotas, aislamiento, billing)

---

## Temario detallado por bloques (lo que debes dominar)

### A) Software Engineering (Python)
- Arquitectura: clean architecture, hexagonal, DDD-lite  
- Testing: unit/integration/contract tests, mocks, golden tests para prompts  
- APIs: versionado, pagination, idempotency keys  
- Resiliencia: retries/backoff, circuit breakers, bulkheads  
- Performance: profiling, async IO, colas, caching  
- Documentación: ADRs, runbooks, diagrams (C4)

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
