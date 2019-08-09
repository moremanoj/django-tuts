from io import BytesIO
from datetime import date
from .views import BookService
from django.http import HttpResponse
from django.template.loader import get_template

from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None

def getDisableDates():
    all_services = list(map(lambda x: f'{x.date()}', 
                            BookService.objects.values_list('selected_date', flat=True)))
    disable_dates = list(filter( lambda x: all_services.count(x) >= 20 , all_services))
    return disable_dates

def getServiceData(Id):
    result = {}
    datas = BookService.objects.filter(id=Id).values()
    print (datas[0])
    return datas[0]
