from fastapi import FastAPI
from app.api.routes import router
from app.api.pdf_routes import router as pdf_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI(
    title="VentureMind AI API",
    description="Production-ready Multi-Agent Startup Incubator API",
    version="1.0.0"
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {
        "message": "Welcome to VentureMind AI API 🚀"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "service": "VentureMind AI Backend"
    }


app.include_router(router, prefix="/api", tags=["API"])
app.include_router(pdf_router, prefix="/api", tags=["PDF"])