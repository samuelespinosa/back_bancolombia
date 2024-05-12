from io import BytesIO
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse
from html import escape
import base64
from django.contrib.staticfiles import finders

def generate_pdf(movimientos,cuenta=None):
    template = get_template('pdf_template.html')
    context = {'pagesize':'A4','cuenta':cuenta,'movimientos':movimientos,'logo':generate_base_64('header.jpg')}
    html  = template.render(context)
    result = BytesIO() 

    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))

def generate_base_64(path):
    with open(finders.find(path), 'rb') as image_file:
        image_data = image_file.read()
    img = base64.b64encode(image_data).decode('utf-8')
    return img;
