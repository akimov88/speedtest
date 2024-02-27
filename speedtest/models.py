from django.db import models

from speedtest.base.base_models import AbstractNetworkTestModel, AbstractSpeedtestModel


class Ping(AbstractNetworkTestModel):
    latency = models.FloatField()


class Download(AbstractNetworkTestModel, AbstractSpeedtestModel):
    pass


class Upload(AbstractNetworkTestModel, AbstractSpeedtestModel):
    pass


class SpeedTest(models.Model):
    timestamp = models.DateTimeField()
    ping = models.ForeignKey(Ping, on_delete=models.CASCADE)
    download = models.ForeignKey(Download, on_delete=models.CASCADE)
    upload = models.ForeignKey(Upload, on_delete=models.CASCADE)
