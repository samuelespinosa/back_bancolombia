from rest_framework import generics,viewsets,status,views
from .models import * 
from .serializers import * 
from rest_framework.response import Response
from rest_framework.decorators import action
from .utils import generate_pdf,generate_base_64
from django.http import FileResponse
from django.template import loader
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

def pdf(request):
    movimientos = Movimiento.objects.filter(cuenta='5973518656').order_by('-fecha')
    template = loader.get_template("pdf_template.html")
    context = {'movimientos': movimientos,'logo':generate_base_64('header.png')}
    return HttpResponse(template.render(context, request))

class CuentasViewSet(viewsets.ModelViewSet):
    queryset= Cuenta.objects.all()
    serializer_class=CuentasSerializer
    
class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientosSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movimiento = serializer.save() 
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def lista_movimientos(self, request, pk=None):
        movimientos = Movimiento.objects.filter(cuenta=pk).order_by('-fecha')
        serializer = self.get_serializer(movimientos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get'])
    def obtener_pdf(self, request,pk=None):
        cuenta_obj = get_object_or_404(Cuenta, pk=pk)
        movimientos = Movimiento.objects.filter(cuenta=pk).order_by('-fecha')
        serializer = self.get_serializer(movimientos, many=True)
        pdf_response = generate_pdf(serializer.data,cuenta_obj)
        return pdf_response
