from django.db import models


class Result(models.Model):
    timestamp = models.DateTimeField('Дата')
    download_bandwidth = models.PositiveBigIntegerField('Пропускная способность загрузки')
    download_bytes = models.PositiveBigIntegerField('Загружено байт')
    download_elapsed = models.PositiveBigIntegerField('Время загрузки')

    upload_bandwidth = models.PositiveBigIntegerField('Пропускная способность выгрузки')
    upload_bytes = models.PositiveBigIntegerField('Выгружено байт')
    upload_elapsed = models.PositiveBigIntegerField('Время выгрузки')

    ping_jitter = models.FloatField('Jitter ping')
    ping_latency = models.FloatField('Latency ping')
    ping_high = models.FloatField('High ping')
    ping_low = models.FloatField('Low ping')

    @property
    def download_speed(self):
        return self.download_bytes / 1024 / 1024 / (self.download_elapsed / 1000) * 8

    @property
    def upload_speed(self):
        return self.upload_bytes / 1024 / 1024 / (self.upload_elapsed / 1000) * 8

    class Meta:
        verbose_name = 'Результат'
        verbose_name_plural = 'Результаты'
