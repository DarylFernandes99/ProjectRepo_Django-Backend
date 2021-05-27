from . views import LlieViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'low-light', LlieViewSet)

urlpatterns = router.urls