from fastapi import APIRouter
from backend.app.services.groq_service import GroqService
from backend.app.services.startup_service import StartupService
from backend.app.schemas.startup import StartupRequest

router = APIRouter()


@router.get("/test")
def test_api():
    return {
        "message": "API Routes Working Successfully 🚀"
    }


@router.get("/test-groq")
def test_groq():
    groq = GroqService()

    response = groq.generate_response(
        "Say only: Groq connection successful."
    )

    return {
        "response": response
    }


@router.post("/generate-startup")
def generate_startup(request: StartupRequest):

    startup_service = StartupService()

    result = startup_service.generate_startup_report(
        startup_domain=request.startup_domain,
        problem_statement=request.problem_statement
    )

    return result