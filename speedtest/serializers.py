from rest_framework.serializers import ModelSerializer

from speedtest.models import Result


class ResultSerializer(ModelSerializer):
    class Meta:
        model = Result
        fields = ('timestamp',
                  'download_bandwidth',
                  'download_bytes',
                  'download_elapsed',
                  'upload_bandwidth',
                  'upload_bytes',
                  'upload_elapsed',
                  'ping_jitter',
                  'ping_latency',
                  'ping_high',
                  'ping_low')
