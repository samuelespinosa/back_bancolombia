#
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import *
#
# router = DefaultRouter()
# router.register(r'cuentas', CuentasViewSet)
# router.register(r'movimientos', MovimientosViewSet)
#
# # The API URLs are now determined automatically by the router.
# # Additionally, we include the views that don't require ViewSets manually.
#
# urlpatterns = [
#     path(r'api/',include(router.urls)),
#     path('api/movimientos/<int:pk>/lista_movimientos/', MovimientosViewSet.as_view({'get': 'lista_movimientos'})),
#     path('api/movimientos/<int:pk>/obtner_pdf/', MovimientosViewSet.as_view({'get': 'obtner_pdf'})),
#     path('pdf/',views.pdf , name="pdf"),
# ]
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import CuentasViewSet, MovimientosViewSet

router = DefaultRouter()
router.register(r'cuentas', CuentasViewSet)
router.register(r'movimientos', MovimientosViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/movimientos/<int:pk>/lista_movimientos/', MovimientosViewSet.as_view({'get': 'lista_movimientos'})),
    path('api/movimientos/<int:pk>/obtener_pdf/', MovimientosViewSet.as_view({'get': 'obtener_pdf'})),
]
