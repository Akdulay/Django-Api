from rest_framework.routers import DefaultRouter
from Inventario.api.views import ProductosViewSet,TiendaViewset,PersonaViewset

router=DefaultRouter()
router.register('productos',ProductosViewSet,basename='producto')
router.register('tienda',TiendaViewset,basename='tienda')
router.register('persona',PersonaViewset,basename='persona')
urlpatterns = router.urls
