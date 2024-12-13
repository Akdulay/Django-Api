from rest_framework.routers import DefaultRouter
from Inventario.api.views import ProductosViewSet,TiendaViewset,PersonaViewset,TotalIngeViewset,CargoViewset

router=DefaultRouter()
router.register('producto',ProductosViewSet,basename='producto')
router.register('tienda',TiendaViewset,basename='tienda')
router.register('persona',PersonaViewset,basename='persona')
router.register('empleado',TotalIngeViewset,basename='empleado')
router.register('cargo',CargoViewset,basename='cargo')
urlpatterns = router.urls
