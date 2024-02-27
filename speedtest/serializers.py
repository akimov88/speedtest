from rest_framework.serializers import ModelSerializer

from speedtest.models import SpeedTest


class SpeedTestSerializer(ModelSerializer):
    class Meta:
        model = SpeedTest
        fields = ('timestamp', 'ping', 'download', 'upload')
