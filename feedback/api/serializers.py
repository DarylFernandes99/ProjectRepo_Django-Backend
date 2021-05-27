from ..models import Feedback
from rest_framework import serializers
from django.core.files.base import ContentFile

class FeedbackSerializers(serializers.ModelSerializer):
    class Meta():
        model = Feedback
        fields = ('id', 'email', 'subject', 'message')
