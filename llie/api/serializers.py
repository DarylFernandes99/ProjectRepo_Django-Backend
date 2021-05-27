import uuid
import base64
from ..models import Llie
from rest_framework import serializers
from django.core.files.base import ContentFile

#Converting base64 string format to image
class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        _format, str_img = data.split(';base64')
        decoded_file = base64.b64decode(str_img)
        fname = str(uuid.uuid4())[:10] + ".png"
        data = ContentFile(decoded_file, name=fname)
        return super().to_internal_value(data)

class LlieSerializers(serializers.ModelSerializer):
    image = Base64ImageField()
    class Meta():
        model = Llie
        fields = ('id', 'image', 'predicted', 'result')
