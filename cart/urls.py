from rest_framework.routers import DefaultRouter
from .views import CartItemViewSet

router = DefaultRouter()
router.register('items', CartItemViewSet)

urlpatterns = router.urls
