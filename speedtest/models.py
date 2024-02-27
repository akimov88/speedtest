from django.db import models


class AbstractNetworkTestModel(models.Model):
    timestamp = models.DateTimeField()
    jitter = models.FloatField()
    low = models.FloatField()
    high = models.FloatField()

    class Meta:
        abstract = True


class AbstractSpeedtestModel(models.Model):
    iqm = models.FloatField()
    bandwidth = models.BigIntegerField()
    bytes = models.BigIntegerField()
    elapsed = models.IntegerField()

    class Meta:
        abstract = True


class Ping(AbstractNetworkTestModel):
    latency = models.FloatField()


class Download(AbstractNetworkTestModel, AbstractSpeedtestModel):
    pass


class Upload(AbstractNetworkTestModel, AbstractSpeedtestModel):
    pass
