from rest_framework import viewsets
from rest_framework import filters
from api.reading.models import Reading
from api.reading.serializers import ReadingSerializer

class ReadingViewSet(viewsets.ModelViewSet):
    queryset = Reading.objects.all().order_by('rec_at')
    serializer_class = ReadingSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['created_at']
