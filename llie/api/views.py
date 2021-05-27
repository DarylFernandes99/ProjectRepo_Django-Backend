from ..models import Llie
from rest_framework import viewsets
from .serializers import LlieSerializers

class LlieViewSet(viewsets.ModelViewSet):
    serializer_class = LlieSerializers
    queryset = Llie.objects.all()