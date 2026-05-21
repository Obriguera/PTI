# ADR-001 — Stack Tecnológico del Proyecto

**Fecha:** 2026-05-21
**Estado:** Aceptada
**Decisores:** Lagoria, Iriarte, Briguera, Juarez, Guerrero, Godoy
**Epic relacionado:** INFRA

---

## Contexto

El proyecto PTI requiere un stack completamente open source con costo < USD 200 usando tiers académicos. Necesitamos procesar imágenes satelitales y de dron, correr modelos de deep learning, servir una API REST y mostrar un mapa interactivo. El equipo tiene experiencia principalmente en Python; la infraestructura debe ser reproducible en distintas máquinas del equipo.

## Opciones consideradas

### Opción A — FastAPI + PostgreSQL/PostGIS + React + Docker (elegida)
- **Pro:** Ecosistema geoespacial Python maduro (Rasterio, GDAL, GeoPandas, GEE SDK). FastAPI tiene async nativo necesario para tareas Celery. PostGIS es el estándar para datos GIS. Amplia documentación en papers de agricultura de precisión.
- **Contra:** Requiere Docker y orquestación de varios servicios. Curva de aprendizaje para integrantes sin experiencia en contenedores.

### Opción B — Django + SQLite + Vue.js
- **Pro:** Menos servicios, más simple de arrancar localmente.
- **Contra:** SQLite sin soporte PostGIS nativo. Django es más pesado para una API pura REST/async.

### Opción C — Flask + MongoDB + Vanilla JS
- **Pro:** Setup mínimo.
- **Contra:** MongoDB tiene soporte geoespacial limitado comparado con PostGIS. Flask requiere más configuración manual para async y workers.

## Decisión

Elegimos **Opción A** porque maximiza la integración con el ecosistema geoespacial Python y es el stack más documentado en los papers de referencia del proyecto (Larrazabal et al. 2024, Sharma et al. 2024). Esta decisión es **difícil de revertir** una vez que el esquema de base de datos esté poblado con datos georreferenciados.

## Consecuencias

**Positivas:**
- Docker Compose permite onboarding rápido sin instalar dependencias locales.
- PostGIS + GeoAlchemy2 dan soporte nativo a geometrías georreferenciadas.
- Stack alineado con lo que usan los papers de referencia del dominio.

**Negativas / trade-offs:**
- docker-compose con 5+ servicios puede ser pesado en máquinas con < 8 GB RAM.
- El equipo deberá aprender Docker si no tiene experiencia previa.

**Acciones derivadas:**
- [x] Crear docker-compose.yml base (S1-02)
- [ ] Documentar requisitos mínimos de hardware en README (S1-02)

## Referencias
- Larrazabal et al. (2024). Site-Specific Prescription Maps for Sugarcane Weed Control. *Land*, 13(11).
- Sharma et al. (2024). Comparative performance of YOLO variants for weed detection. *Smart Ag Tech*, 9.
