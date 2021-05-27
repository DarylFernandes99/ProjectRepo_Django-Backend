from . views import FeedbackViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FeedbackViewSet)

urlpatterns = router.urls