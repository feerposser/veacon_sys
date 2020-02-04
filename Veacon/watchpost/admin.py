from django.contrib import admin

from .models import WatchpostModel


class WatchpostAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'last_update',)  # 'rssi_max', 'rssi_min',
    list_display = ('id', '__str__')


admin.site.register(WatchpostModel, WatchpostAdmin)
