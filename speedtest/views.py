import plotly.graph_objs as go
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from speedtest.models import SpeedTest
from speedtest.serializers import SpeedTestSerializer


class SpeedTestViewSet(GenericViewSet, ListModelMixin):
    queryset = SpeedTest.objects.all()
    serializer_class = SpeedTestSerializer
    filterset_fields = {'timestamp': ('gte', 'lte')}


class SpeedTestResultView(TemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        timestamp_qs = SpeedTest.objects.all()
        download_figure, upload_figure = go.Figure(), go.Figure()
        download_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.download.high for result in timestamp_qs],
                name='high'
            )
        )
        download_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.download.low for result in timestamp_qs],
                name='low'
            )
        )
        download_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.download.jitter for result in timestamp_qs],
                name='jitter'
            )
        )
        download_figure.update_layout(
            title='Download',
            xaxis_title='timestamp',
            yaxis_title='mb/s',
        )
        upload_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.upload.high for result in timestamp_qs],
                name='high'
            )
        )
        upload_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.upload.low for result in timestamp_qs],
                name='low'
            )
        )
        upload_figure.add_trace(
            go.Scatter(
                x=[result.timestamp for result in timestamp_qs],
                y=[result.upload.jitter for result in timestamp_qs],
                name='jitter'
            )
        )
        upload_figure.update_layout(
            title='Upload',
            xaxis_title='timestamp',
            yaxis_title='mb/s',
        )
        context['download'], context['upload'] = download_figure.to_html(), upload_figure.to_html()
        return render(request, context=context, template_name='speedtest_result.html')


# class SpeedTestResultDetailView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         context = self.get_context_data()
#         result = SpeedTest.objects.get(timestamp=request.GET.get('timestamp'))
#         # context['result'] = {
#         #     'timestamp': result.timestamp.isoformat(),
#         #     'ping': {
#         #         'jitter': result.ping.jitter,
#         #         'low': result.ping.low,
#         #         'high': result.ping.high,
#         #         'latency': result.ping.latency,
#         #     },
#         #     'download': {
#         #         'jitter': result.download.jitter,
#         #         'low': result.download.low,
#         #         'high': result.download.high,
#         #         'iqm': result.download.iqm,
#         #         'bandwidth': result.download.bandwidth,
#         #         'bytes': result.download.bytes,
#         #         'elapsed': result.download.elapsed,
#         #     },
#         #     'upload': {
#         #         'jitter': result.upload.jitter,
#         #         'low': result.upload.low,
#         #         'high': result.upload.high,
#         #         'iqm': result.upload.iqm,
#         #         'bandwidth': result.upload.bandwidth,
#         #         'bytes': result.upload.bytes,
#         #         'elapsed': result.upload.elapsed,
#         #     },
#         # }
#         download = px.line(
#             title='download',
#             labels={'x': 'sec', 'y': 'mb/s'},
#             x=[result.download.timestamp - timedelta(seconds=result.download.elapsed/1000), result.download.timestamp],
#             y=[result.download.low, result.download.high]
#         ).to_html()
#         upload = px.line(
#             title='upload',
#             labels={'x': 'sec', 'y': 'mb/s'},
#             x=[result.upload.timestamp - timedelta(seconds=result.upload.elapsed/1000), result.upload.timestamp],
#             y=[result.upload.low, result.upload.high]
#         ).to_html()
#         context['download'], context['upload'] = download, upload
#         return render(request, context=context, template_name='speedtest_result_detail.html')
