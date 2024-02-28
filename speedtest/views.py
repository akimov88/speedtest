import plotly.graph_objs as go
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from speedtest.models import Result
from speedtest.serializers import ResultSerializer


class SpeedTestViewSet(GenericViewSet, ListModelMixin):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
    filterset_fields = {'timestamp': ('gte', 'lte')}


class SpeedTestResultView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        qs = Result.objects.all()
        download_figure, upload_figure = go.Figure(), go.Figure()
        download_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in qs],
                y=[result.download_speed for result in qs],
            )
        )
        download_figure.update_layout(
            title='Download',
            xaxis_title='timestamp',
            yaxis_title='mb/s',
        )
        upload_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in qs],
                y=[result.upload_speed for result in qs]
            )
        )
        upload_figure.update_layout(
            title='Upload',
            xaxis_title='timestamp',
            yaxis_title='mb/s',
        )
        context['download'], context['upload'] = download_figure.to_html(), upload_figure.to_html()
        return render(request, context=context, template_name='result.html')
