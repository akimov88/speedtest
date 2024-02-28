from django.contrib import admin

from speedtest.models import Result


@admin.register(Result)
class SpeedTestAdmin(admin.ModelAdmin):
    list_display = (
        'timestamp',
        'download_bandwidth',
        'download_bytes',
        'download_elapsed',
        'upload_bandwidth',
        'upload_bytes',
        'upload_elapsed',
        'ping_jitter',
        'ping_latency',
        'ping_high',
        'ping_low',
    )
    list_filter = ('timestamp',)
