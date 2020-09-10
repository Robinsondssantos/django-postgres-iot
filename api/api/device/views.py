from rest_framework import viewsets
from rest_framework import filters
from api.device.models import Device
from api.device.serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('created_at')
    serializer_class = DeviceSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['description']
