from rest_framework import generics,viewsets,status
from .models import * 
from .serializers import * 
from rest_framework.response import Response
from rest_framework.decorators import action

class CuentasViewSet(viewsets.ModelViewSet):
    queryset= Cuenta.objects.all()
    serializer_class=CuentasSerializer
    
class MovimientosViewSet(viewsets.ModelViewSet):
    queryset = Movimiento.objects.all()
    serializer_class = MovimientosSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.create(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    @action(detail=True, methods=['get'])
    def lista_movimientos_por_cuenta(self, request, pk):
        movimientos = Movimiento.objects.filter(cuenta=pk)
        serializer = self.get_serializer(movimientos, many=True)
        return Response(serializer.data)
