from rest_framework.routers import DefaultRouter
from Inventario.api.views import ProductosViewSet,TiendaViewset,PersonaViewset,TotalIngeViewset

router=DefaultRouter()
router.register('productos',ProductosViewSet,basename='producto')
router.register('tienda',TiendaViewset,basename='tienda')
router.register('persona',PersonaViewset,basename='persona')
router.register('empleado',TotalIngeViewset,basename='empleado')
urlpatterns = router.urls
