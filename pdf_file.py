from reportlab.lib.pagesizes import LETTER
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas


# canvas = Canvas("hello.pdf", pagesize=(612.0, 729.0))
#
# canvas.drawString(72, 72, "Hello World")
# canvas.save()

canvas = Canvas("font-example.pdf", pagesize=LETTER)
canvas.setFont("Times-Roman", 18)
canvas.drawString(1 * inch, 10 * inch, "Times New Roman (18 pt)")
canvas.save()

