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
    template_name = 'speedtest_result.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['result'] = SpeedTest.objects.get(timestamp=kwargs.get('timestamp'))
        return context
