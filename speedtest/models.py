from django.db import models


class Result(models.Model):
    timestamp = models.DateTimeField('временная метка')
    download_bandwidth = models.PositiveBigIntegerField('пропускная способность при загрузке')
    download_bytes = models.PositiveBigIntegerField('загружено байт')
    download_elapsed = models.PositiveBigIntegerField('время затраченное на загрузку')

    upload_bandwidth = models.PositiveBigIntegerField('пропускная способность при выгрузке')
    upload_bytes = models.PositiveBigIntegerField('выгружено байт')
    upload_elapsed = models.PositiveBigIntegerField('время затраченное на выгрузку')

    ping_jitter = models.FloatField('jitter')
    ping_latency = models.FloatField('latency')
    ping_high = models.FloatField('high')
    ping_low = models.FloatField('low')

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
