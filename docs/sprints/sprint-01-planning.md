# Sprint 1 — Planning

**Período:** 21 May – 4 Jun 2026
**Goal:** El equipo puede trabajar — entorno Docker funcional, repo estructurado y dataset baseline identificado.
**Capacidad estimada:** 6 personas × ~10 hs = ~60 hs | ~37 story points

---

## Equipos

| Equipo | Integrantes | Foco |
|---|---|---|
| IA | Briguera, Juarez, Guerrero | `ml/`, `data/`, modelos |
| Full-stack | Godoy, Iriarte, Lagoria | `backend/`, `frontend/`, `infra/` |

> Cualquier integrante puede tomar tareas del backlog de otro equipo para ayudar a cumplir el sprint goal.

---

## Backlog del Sprint

| ID | Tarea | Equipo | Pts | Responsable | Estado |
|---|---|---|---|---|---|
| S1-01 | Crear estructura de carpetas del repo | Full-stack | 2 | Lagoria | ✅ Done |
| S1-02 | docker-compose.yml base (FastAPI, PostgreSQL+PostGIS, Redis, Celery, MLflow) | Full-stack | 5 | Lagoria/Iriarte | ✅ Done |
| S1-03 | .env.example documentado | Full-stack | 2 | Lagoria | ✅ Done |
| S1-04 | GitHub Actions CI básico (lint ruff + pytest) | Full-stack | 3 | Lagoria | ✅ Done |
| S1-05 | Setup GitHub Projects: milestones, labels, vistas Backlog/Sprint/Done | Full-stack | 2 | Lagoria | 🔲 To Do |
| S1-06 | Skeleton FastAPI con health endpoint | Full-stack | 3 | Lagoria/Iriarte | ✅ Done |
| S1-07 | Investigar y seleccionar dataset público de malezas (DeepWeeds, CottonWeedDet3, WeedNet) | IA | 3 | Guerrero | 🔲 To Do |
| S1-08 | Script de descarga y organización del dataset en formato YOLO | IA | 5 | Guerrero/Juarez | 🔲 To Do |
| S1-09 | Setup CVAT en Docker para etiquetado | IA | 3 | Briguera | 🔲 To Do |
| S1-10 | Setup MLflow tracking server | IA | 3 | Briguera | ✅ Done (incluido en compose) |
| S1-11 | ADR-001: Justificación del stack tecnológico | Full-stack | 2 | Lagoria | ✅ Done |
| S1-12 | ADR-002: Justificación de YOLOv8 vs alternativas (Detectron2, RT-DETR) | IA | 2 | Juarez | 🔲 To Do |
| S1-13 | Scaffold React + Leaflet con Vite | Full-stack | 3 | Godoy | 🔲 To Do |

**Total:** 37 pts | **Completado en planning:** 20 pts

---

## Definition of Done

- Código en branch del módulo correspondiente (`infra/`, `ml/`, `api/`, `frontend/`)
- PR creado y aprobado por al menos 1 integrante distinto al autor
- Test básico asociado (si el cambio agrega código nuevo)
- Documentación actualizada (Wiki o ADR si hay decisión de diseño)

---

## Notas de planning

- El dataset de entrenamiento final vendrá del INTA Famaillá (contacto en gestión activa). Mientras tanto el equipo IA usa dataset público como baseline — decisión válida académicamente.
- La integración con Google Earth Engine requiere cuenta académica aprobada. Guerrero inicia el trámite esta semana.
- Se usa Python 3.12 en Docker (3.14 está en alpha). Se revisará upgrade cuando salga versión estable — ver ADR-001.
- Las carpetas `Backend/` y `Frontend/` (mayúsculas) existentes son legacy; se migra todo a `backend/` y `frontend/` (minúsculas) según estructura del README.

---

## Retrospectiva
*(Completar el 4 de Jun 2026)*

**¿Qué salió bien?**

**¿Qué mejorar?**

**Acciones concretas para Sprint 2:**
