# import ColorizeViewSet from '../colorize'
from colorize.api.views import ColorizeViewSet
from llie.api.views import LlieViewSet
from feedback.api.views import FeedbackViewSet
from poem.api.views import PoemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'colorize', ColorizeViewSet)
router.register(r'low-light', LlieViewSet)
router.register(r'feedback', FeedbackViewSet)
router.register(r'poem', PoemViewSet)

urlpatterns = router.urls