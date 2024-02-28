import logging

from celery import shared_task

from speedtest.models import Result
from speedtest.service import network_speedtest

logger = logging.Logger('speedtest.tasks')


@shared_task
def speedtest_task():
    result = network_speedtest()
    if result:
        try:
            Result.objects.create(
                timestamp=result.get('timestamp'),
                download_bandwidth=result.get('download').get('bandwidth'),
                download_bytes=result.get('download').get('bytes'),
                download_elapsed=result.get('download').get('elapsed'),
                upload_bandwidth=result.get('upload').get('bandwidth'),
                upload_bytes=result.get('upload').get('bytes'),
                upload_elapsed=result.get('upload').get('elapsed'),
                ping_jitter=result.get('ping').get('jitter'),
                ping_latency=result.get('ping').get('latency'),
                ping_high=result.get('ping').get('high'),
                ping_low=result.get('ping').get('low'),
            )
        except AttributeError as error:
            logger.error(msg=f'speedtest_task_error: {error}')
