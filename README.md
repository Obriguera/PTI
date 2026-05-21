# PTI — Plataforma de Detección de Malezas en Caña de Azúcar

**Proyecto Tecnológico Integrador | Ingeniería en Informática | Universidad Blas Pascal**

Plataforma open source de agricultura de precisión para la detección automática de malezas en cultivos de caña de azúcar (Tucumán, Argentina) mediante imágenes RGB de dron, deep learning y datos satelitales abiertos.

---

## Equipo

| Integrante | Rol |
|---|---|
| Briguera, Octavio | ML Engineer / Integración |
| Juarez, Carlos Nahuel | ML Engineer / QA |
| Godoy Cabrera, Santiago Abel | Frontend / Visualización |
| Guerrero, Lautaro | ML Engineer / Datos |
| Iriarte Chamorro, Jorge Manuel | Backend / DevOps |
| Lagoria, Ricardo Augusto | Backend / DevOps |

**Docente tutor:** Gencarelli, Oscar Luis
**Institución:** Universidad Blas Pascal — Córdoba, Argentina
**Versión:** 1.0 | Mayo 2026

---

## Descripción

El sistema procesa imágenes de vuelo RGB mediante OpenDroneMap, detecta malezas con modelos YOLOv8/v11 entrenados con datos locales, calcula índices de vegetación visibles (ExG, VARI, GLI, MGRVI) y enriquece el análisis con datos de Sentinel-2 (GEE), humedad de suelo (SMAP L4) y pronóstico meteorológico (Open-Meteo / NASA POWER).

La salida es un JSON georreferenciado por parcela con un mapa de prescripción variable de herbicidas, validado agronómicamente por técnicos del INTA Famaillá.

**Resultado esperado:** reducción del 20–35 % en el consumo de herbicidas por campaña.
**Infraestructura:** 100 % open source | costo < USD 200 usando tiers académicos gratuitos.

---

## Pipeline

```
Vuelo RGB
    |
    v
OpenDroneMap --> GeoTIFF ortomosaico + DSM/DTM
    |
    v
Preprocesamiento (OpenCV + Rasterio) --> tiles 1024x1024 px
    |
    v
YOLOv8/v11 (detección) + DeepLabV3+ (segmentación) + ResNet-18 (estadio fenológico)
    |
    v
Índices de vegetación (ExG, VARI, GLI, MGRVI)
    |
    v
Enriquecimiento APIs (Sentinel-2 / SMAP L4 / Open-Meteo / NASA POWER)
    |
    v
Motor de reglas YAML --> prescripción variable por parcela
    |
    v
API REST (FastAPI) + Dashboard web (Leaflet) + exportación GeoJSON / PDF
```

---

## Stack tecnológico

| Capa | Tecnología | Licencia |
|---|---|---|
| Fotogrametría | OpenDroneMap | AGPL-3.0 |
| Detección | YOLOv8/v11 (Ultralytics) | AGPL-3.0 |
| Segmentación | DeepLabV3+ / U-Net (SMP) | MIT |
| Geoprocesamiento | Rasterio, GDAL, GeoPandas | BSD/MIT |
| Teledetección | Google Earth Engine + Sentinel-2 | Académico |
| Clima / Suelo | Open-Meteo, NASA POWER, SMAP L4 | CC BY 4.0 |
| Backend | FastAPI + Celery + Redis | MIT/BSD |
| Base de datos | PostgreSQL 15 + PostGIS 3.4 | PostgreSQL |
| Frontend | React + Leaflet.js | MIT |
| MLOps | MLflow + CVAT | Apache 2.0 |
| Infraestructura | Docker Compose + GitHub Actions | Apache 2.0 |

---

## Estructura del repositorio

```
PTI/
├── data/                   # Scripts de descarga y preprocesamiento de datos
│   ├── labeling/           # Configuración CVAT y scripts de etiquetado
│   └── raw/                # (ignorado por .gitignore — datos locales)
├── ml/                     # Entrenamiento, evaluación y exportación de modelos
│   ├── train/
│   ├── eval/
│   └── models/             # Pesos exportados (.onnx, .pt)
├── geo/                    # Procesamiento ODM, índices de vegetación, GEE
│   ├── odm/
│   ├── indices/
│   └── satellite/
├── backend/                # FastAPI + Celery + motor de reglas
│   ├── api/
│   ├── rules/              # Reglas agronómicas en YAML
│   └── workers/
├── frontend/               # Dashboard React + Leaflet
├── infra/                  # Docker Compose, variables de entorno, CI/CD
│   ├── docker-compose.yml
│   └── .github/workflows/
├── tests/                  # Suite pytest — cobertura objetivo >= 70 %
├── docs/                   # Documentación técnica y agronómica
└── README.md
```

---

## Inicio rápido

### Requisitos previos

- Docker >= 24.0 y Docker Compose >= 2.20
- Git
- (Opcional para entrenamiento) GPU con CUDA 11.8+ o acceso a Google Colab

### Instalación

```bash
# 1. Clonar el repositorio
git clone https://github.com/Obriguera/PTI.git
cd PTI

# 2. Copiar y configurar variables de entorno
cp infra/.env.example infra/.env
# Editar infra/.env con las credenciales de GEE y demás APIs

# 3. Levantar todos los servicios
docker compose -f infra/docker-compose.yml up --build

# 4. Acceder al dashboard
# http://localhost:3000

# 5. Acceder a la documentación de la API
# http://localhost:8000/docs
```

### Ejecutar los tests

```bash
docker compose -f infra/docker-compose.yml exec backend pytest tests/ -v --cov
```

---

## Fases del proyecto

| Fase | Período | Hito principal |
|---|---|---|
| F1 | Meses 1-2 | Entorno Docker funcional + dataset baseline 200 imgs |
| F2 | Meses 3-5 | Demo E2E con 2 especies — pipeline completo de punta a punta |
| F3 | Meses 6-8 | mAP@0.5 >= 0,75 sobre dataset local (>= 800 imgs) |
| F4 | Meses 9-10 | Dashboard + API documentada + validación agronómica INTA |
| F5 | Mes 11 | Cobertura tests >= 70 % + documentación + defensa |

---

## Especies objetivo (EEAOC, Avance 2023)

| Especie | Nombre común | Frecuencia en Tucumán |
|---|---|---|
| Cynodon dactylon | Gramilla | 49 % |
| Tithonia tubaeformis | Pasto cubano | 64 % (emergente) |
| Sorghum halepense | Sorgo de Alepo | ~30 % |
| Sicyos polyacanthus | Tupúlo | ~35 % |
| Cyperus rotundus | Cebollín | 23 % |

---

## Convenciones de trabajo

- **Ramas:** `main` protegida. Feature branches con prefijo de módulo:
  `ml/`, `geo/`, `api/`, `frontend/`, `infra/`
- **Pull requests:** revisión obligatoria de al menos un integrante distinto al autor
- **Tests:** ningún merge a `main` sin al menos un test que pase en CI
- **Commits:** mensajes en inglés, formato `tipo(scope): descripción`
  — ejemplo: `feat(ml): add YOLOv8 training pipeline`
- **Reducción de alcance:** vertical (menos especies o menos imágenes),
  nunca horizontal (no se saltean etapas del pipeline)

---

## Contribuir

Este es un proyecto académico cerrado. El código se publica bajo licencia AGPL-3.0 para permitir la replicación por otras instituciones del NOA. Si sos investigador o técnico del INTA/EEAOC y querés colaborar, abrí un issue o contactá al equipo.

---

## Licencia

AGPL-3.0 — ver [LICENSE](LICENSE) para el texto completo.

---

## Referencias clave

- IPAAT (2024). Reporte final de zafra 2024.
- EEAOC / Revista Avance (2023). Relevamiento de malezas en caña de azúcar en Tucumán.
- Jocher et al. (2023). YOLOv8 — Ultralytics.
- Larrazabal et al. (2024). Site-Specific Prescription Maps for Sugarcane Weed Control. Land, 13(11).
- Sharma et al. (2024). Comparative performance of YOLO variants for weed detection. Smart Ag Tech, 9.
