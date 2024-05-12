from rest_framework import generics,viewsets,status,views
from .models import * 
from .serializers import * 
from rest_framework.response import Response
from rest_framework.decorators import action
from .utils import generate_pdf
from django.http import FileResponse

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
        movimientos = Movimiento.objects.filter(cuenta=pk)
        pdf_bytes = generate_pdf(movimientos)
        response = FileResponse(pdf_bytes, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="extractos.pdf"'
        return response
