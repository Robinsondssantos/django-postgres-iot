from api.reading.models import Reading
from rest_framework import serializers

class ReadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reading
        fields = ('__all__')