from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
from PIL import Image
from io import BytesIO
from .models import Movimiento, Cuenta
from django.templatetags.static import static

def generate_pdf(movimientos):
    cuenta = movimientos[0].cuenta 
    print(cuenta)
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=letter)
    #c.drawImage('./header.png', 100, 750, width=400, height=100)
    # other_img= Image.open(static('images/watermark.jpg'))
    # c.drawImage(other_img, 50, 50, width=200, height=200, mask='auto')
    
    c.setFont("Helvetica", 12)
    c.drawString(100, 700, "Movimientos:")

    y_position = 680
    for movimiento in movimientos:
        c.drawString(100, y_position, f"Fecha: {movimiento.fecha}, Monto: {movimiento.monto}, Tipo: {movimiento.tipo}")
        y_position -= 20

    c.save()
    return buffer.getvalue()
