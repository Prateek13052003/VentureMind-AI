import os
import tempfile
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet


class PDFGenerator:

    @staticmethod
    def generate(report: str):
        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".pdf"
        )

        doc = SimpleDocTemplate(temp_file.name)
        styles = getSampleStyleSheet()

        story = []

        for line in report.split("\n"):
            story.append(Paragraph(line.replace("\t", "    "), styles["BodyText"]))

        doc.build(story)

        return temp_file.name