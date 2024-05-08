from rest_framework import generics,permissions,views,status, viewsets
from .models import * 
from .serializers import * 
from rest_framework.response import Response
#from rest_framework.decorators import action


class CuentaViewSet(viewsets.ModelViewSet):
    queryset= Cuenta.objects.all()
    serializer_class=CuentaSerializer
    
    def list(self, request, *args, **kwargs):
        queryset = self.queryset 
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

