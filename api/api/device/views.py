from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import filters
from api.device.models import Device
from api.device.serializers import DeviceSerializer


class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all().order_by('created_at')
    serializer_class = DeviceSerializer
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['description']

    # @method_decorator(cache_page(60*24*365)) # one year
    # def dispatch(self, request, *args, **kwargs):
    #     return super().dispatch(request, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        # The user is always owner of device that will be created
        request.data['account_id'] = request.user.id
        return super(DeviceViewSet, self).create(request, args, kwargs)


    def list(self, request, *args, **kwargs):
        # Return all devices of user
        queryset = Device.objects.filter(account_id=request.user.id).all().order_by('created_at')

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

