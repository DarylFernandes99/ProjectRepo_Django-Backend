from ..models import Colorize
from rest_framework import viewsets
from .serializers import ColorizeSerializers

class ColorizeViewSet(viewsets.ModelViewSet):
    serializer_class = ColorizeSerializers
    queryset = Colorize.objects.all()