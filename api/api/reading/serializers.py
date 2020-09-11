from rest_framework import serializers
from api.reading.models import Reading
from api.device.serializers import DeviceSerializer

class ReadingSerializer(serializers.ModelSerializer):

    device = DeviceSerializer()

    class Meta:
        model = Reading
        fields = ('__all__')
