import logging

from celery import shared_task

from speedtest.models import Ping, Download, Upload, SpeedTest
from speedtest.service import network_speedtest

logger = logging.Logger('speedtest.tasks')


@shared_task()
def network_speedtest_task():
    speedtest_result = network_speedtest()
    if speedtest_result:
        try:
            ping = Ping.objects.create(
                timestamp=speedtest_result.get('timestamp'),
                jitter=speedtest_result.get('ping').get('jitter'),
                latency=speedtest_result.get('ping').get('latency'),
                low=speedtest_result.get('ping').get('low'),
                high=speedtest_result.get('ping').get('high')
            )
            download = Download.objects.create(
                timestamp=speedtest_result.get('timestamp'),
                bandwidth=speedtest_result.get('download').get('bandwidth'),
                bytes=speedtest_result.get('download').get('bytes'),
                elapsed=speedtest_result.get('download').get('elapsed'),
                iqm=speedtest_result.get('download').get('latency').get('iqm'),
                low=speedtest_result.get('download').get('latency').get('low'),
                high=speedtest_result.get('download').get('latency').get('high'),
                jitter=speedtest_result.get('download').get('latency').get('jitter')
            )
            upload = Upload.objects.create(
                timestamp=speedtest_result.get('timestamp'),
                bandwidth=speedtest_result.get('upload').get('bandwidth'),
                bytes=speedtest_result.get('upload').get('bytes'),
                elapsed=speedtest_result.get('upload').get('elapsed'),
                iqm=speedtest_result.get('upload').get('latency').get('iqm'),
                low=speedtest_result.get('upload').get('latency').get('low'),
                high=speedtest_result.get('upload').get('latency').get('high'),
                jitter=speedtest_result.get('upload').get('latency').get('jitter')
            )
            SpeedTest.objects.create(
                timestamp=speedtest_result.get('timestamp'),
                ping=ping,
                download=download,
                upload=upload
            )
        except AttributeError as error:
            logger.error(msg=f'network_speedtest_task_error: {error}')
