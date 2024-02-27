from django.contrib import admin

from speedtest.models import Ping, Download, Upload


@admin.register(Ping)
class PingAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'jitter', 'low', 'high', 'latency')
    list_filter = ('timestamp',)


@admin.register(Download)
class DownloadAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'bandwidth', 'bytes', 'elapsed', 'imq', 'low', 'high', 'jitter')
    list_filter = ('timestamp',)


@admin.register(Upload)
class UploadAdmin(admin.ModelAdmin):
    list_display = ('timestamp', 'bandwidth', 'bytes', 'elapsed', 'imq', 'low', 'high', 'jitter')
    list_filter = ('timestamp',)
