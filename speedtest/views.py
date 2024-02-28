from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import ListModelMixin

from speedtest.serializers import SpeedTestSerializer
from speedtest.models import SpeedTest


class SpeedTestViewSet(GenericViewSet, ListModelMixin):
    queryset = SpeedTest.objects.all()
    serializer_class = SpeedTestSerializer
    filterset_fields = {'timestamp': ('gte', 'lte')}


class SpeedTestResultView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        result = SpeedTest.objects.get(timestamp=request.GET.get('timestamp'))
        context['result'] = {
            'timestamp': result.timestamp.isoformat(),
            'ping': {
                'jitter': result.ping.jitter,
                'low': result.ping.low,
                'high': result.ping.high,
                'latency': result.ping.latency,
            },
            'download': {
                'jitter': result.download.jitter,
                'low': result.download.low,
                'high': result.download.high,
                'iqm': result.download.iqm,
                'bandwidth': result.download.bandwidth,
                'bytes': result.download.bytes,
                'elapsed': result.download.elapsed,
            },
            'upload': {
                'jitter': result.upload.jitter,
                'low': result.upload.low,
                'high': result.upload.high,
                'iqm': result.upload.iqm,
                'bandwidth': result.upload.bandwidth,
                'bytes': result.upload.bytes,
                'elapsed': result.upload.elapsed,
            },
        }
        return render(request, context=context, template_name='speedtest_result.html')
