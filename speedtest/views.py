from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin

from speedtest.serializers import SpeedTestSerializer
from speedtest.models import SpeedTest


class SpeedTestViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    queryset = SpeedTest.objects.all()
    serializer_class = SpeedTestSerializer
    filterset_fields = {'timestamp': ('gte', 'lte')}
