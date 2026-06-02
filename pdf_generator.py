from reportlab.pdfgen import canvas


def generate_pdf(
        conclusions,
        trace):

    pdf = canvas.Canvas(
        "static/report.pdf"
    )

    pdf.drawString(
        100,
        800,
        "Explainable AI Report"
    )

    y = 760

    pdf.drawString(
        100,
        y,
        "Conclusions"
    )

    y -= 30

    for c in conclusions:

        pdf.drawString(
            120,
            y,
            c
        )

        y -= 20

    y -= 20

    pdf.drawString(
        100,
        y,
        "Trace"
    )

    y -= 20

    for step in trace:

        pdf.drawString(
            120,
            y,
            step
        )

        y -= 20

    pdf.save()