from ..models import Poem
from rest_framework import viewsets
from .serializers import PoemSerializers

class PoemViewSet(viewsets.ModelViewSet):
    serializer_class = PoemSerializers
    queryset = Poem.objects.all()