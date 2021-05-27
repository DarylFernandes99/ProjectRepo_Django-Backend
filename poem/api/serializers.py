from ..models import Poem
from rest_framework import serializers
from django.core.files.base import ContentFile

class PoemSerializers(serializers.ModelSerializer):
    class Meta():
        model = Poem
        fields = ('id', 'phrase', 'length', 'result')
