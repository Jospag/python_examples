from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


canvas = Canvas("hello.pdf", pagesize=(612.0, 729.0))

canvas.drawString(72, 72, "Hello World")
canvas.save()

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

canvas = Canvas("font-colors.pdf", pagesize=LETTER)
# Set font to Times New Roman with 12 point size
canvas.setFont("Times-Roman", 12)
# Draw blue text one inch from the left and ten
# inches from the bottom
canvas.setFillColor("blue")
canvas.drawString(1*inch, 10*inch, "Black text")
# Save the PDF file
canvas.save()

