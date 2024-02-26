from django.db import models


class AbstractNetworkSpeedtestModel(models.Model):
    timestamp = models.DateTimeField()
    jitter = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()

    class Meta:
        abstract = True


class Ping(AbstractNetworkSpeedtestModel):
    latency = models.FloatField()


class Download(AbstractNetworkSpeedtestModel):
    imq = models.FloatField()
    bandwidth = models.BigIntegerField()
    bytes = models.BigIntegerField()
    elapses = models.IntegerField()


class Upload(AbstractNetworkSpeedtestModel):
    imq = models.FloatField()
    bandwidth = models.BigIntegerField()
    bytes = models.BigIntegerField()
    elapses = models.IntegerField()
