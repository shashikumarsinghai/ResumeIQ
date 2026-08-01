from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(score, matched_skills, missing_skills, jobs):
    pdf_file = "Resume_Report.pdf"

    doc = SimpleDocTemplate(pdf_file)
    styles = getSampleStyleSheet()
    elements = []

    elements.append(Paragraph("<b>ResumeIQ Report</b>", styles['Title']))
    elements.append(Paragraph(f"<b>Resume Score:</b> {score}/100", styles['Normal']))

    elements.append(Paragraph("<b>Matched Skills:</b>", styles['Heading2']))
    for skill in matched_skills:
        elements.append(Paragraph(f"- {skill}", styles['Normal']))

    elements.append(Paragraph("<b>Missing Skills:</b>", styles['Heading2']))
    for skill in missing_skills:
        elements.append(Paragraph(f"- {skill}", styles['Normal']))

    elements.append(Paragraph("<b>Recommended Jobs:</b>", styles['Heading2']))
    for job in jobs:
        elements.append(Paragraph(f"- {job}", styles['Normal']))

    doc.build(elements)

    return pdf_file