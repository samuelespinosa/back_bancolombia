
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'cuentas', CuentasViewSet)
router.register(r'movimientos', MovimientosViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the views that don't require ViewSets manually.

urlpatterns = [
    path(r'api/',include(router.urls))
]
