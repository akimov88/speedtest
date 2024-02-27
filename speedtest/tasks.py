from celery import shared_task

from speedtest.models import Ping, Download, Upload
from speedtest.service import network_speedtest


@shared_task()
def network_speedtest_task():
    speedtest_result = network_speedtest()
    if speedtest_result:
        Ping.objects.create(
            timestamp=speedtest_result.get('timestamp'),
            jitter=speedtest_result.get('ping').get('jitter'),
            latency=speedtest_result.get('ping').get('latency'),
            low=speedtest_result.get('ping').get('low'),
            high=speedtest_result.get('ping').get('high')
        )
        Download.objects.create(
            timestamp=speedtest_result.get('timestamp'),
            bandwidth=speedtest_result.get('download').get('bandwidth'),
            bytes=speedtest_result.get('download').get('bytes'),
            elapsed=speedtest_result.get('download').get('elapsed'),
            imq=speedtest_result.get('download').get('latency').get('iqm'),
            low=speedtest_result.get('download').get('latency').get('low'),
            high=speedtest_result.get('download').get('latency').get('high'),
            jitter=speedtest_result.get('download').get('latency').get('jitter')
        )
        Upload.objects.create(
            timestamp=speedtest_result.get('timestamp'),
            bandwidth=speedtest_result.get('upload').get('bandwidth'),
            bytes=speedtest_result.get('upload').get('bytes'),
            elapsed=speedtest_result.get('upload').get('elapsed'),
            imq=speedtest_result.get('upload').get('latency').get('iqm'),
            low=speedtest_result.get('upload').get('latency').get('low'),
            high=speedtest_result.get('upload').get('latency').get('high'),
            jitter=speedtest_result.get('upload').get('latency').get('jitter')
        )
