import os
from fastapi import APIRouter
from fastapi.responses import FileResponse

from backend.app.pdf.pdf_generator import PDFGenerator

router = APIRouter()


@router.post("/download-pdf")
def download_pdf(report: dict):

    pdf_path = PDFGenerator.generate(
        report["investor_pitch"]
    )

    return FileResponse(
        pdf_path,
        media_type="application/pdf",
        filename="VentureMind_Report.pdf"
    )