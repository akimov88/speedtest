from django.shortcuts import render
from django.views.generic import View
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from speedtest.models import Result
from speedtest.serializers import ResultSerializer
from speedtest.services.graph import figures


class SpeedTestViewSet(GenericViewSet, ListModelMixin):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filterset_fields = {'timestamp': ('gte', 'lte')}


class SpeedTestResultView(View):
    def get(self, request, *args, **kwargs):
        qs = Result.objects.all()
        download, upload = figures(qs)
        return render(
            request,
            template_name='result.html',
            context={'download': download, 'upload': upload}
        )
