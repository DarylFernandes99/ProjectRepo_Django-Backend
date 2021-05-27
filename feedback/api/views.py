from ..models import Feedback
from rest_framework import viewsets
from .serializers import FeedbackSerializers

class FeedbackViewSet(viewsets.ModelViewSet):
    serializer_class = FeedbackSerializers
    queryset = Feedback.objects.all()