from fastapi import FastAPI

app = FastAPI(
    title="PTI — Detección de Malezas en Caña de Azúcar",
    version="0.1.0",
    docs_url="/docs",
    redoc_url="/redoc",
)


@app.get("/health", tags=["Sistema"])
def health():
    return {"status": "ok", "version": "0.1.0"}
