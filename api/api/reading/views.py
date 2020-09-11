from rest_framework import status
from rest_framework.response import Response

from rest_framework import viewsets
from rest_framework import filters
from api.reading.models import Reading
from api.device.models import Device
from api.reading.serializers import ReadingSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by('-created_at')
    serializer_class = ReadingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['created_at']

    def create(self, request, *args, **kwargs):
        # The request needs send the mac parameter
        # with the mac a search will be done
        # if mac exists, than the device exists
        # and now can create de register
        mac = self.request.query_params.get('mac', None)

        if mac:
            device = Device.objects.get(mac=mac)

            if device:
                request.data['device_id'] = str(device.id)

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
