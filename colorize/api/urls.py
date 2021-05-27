from .views import ColorizeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'colorize', ColorizeViewSet)

urlpatterns = router.urls