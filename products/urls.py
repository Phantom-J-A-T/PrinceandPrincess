from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet, ProductDetailViewSet

router = DefaultRouter()
router.register('categories', CategoryViewSet)
router.register('', ProductViewSet)
router.register('details', ProductDetailViewSet)

urlpatterns = router.urls
