from django.contrib import admin

from .models import WatchpostModel


class WatchpostAdmin(admin.ModelAdmin):
    readonly_fields = ('id', 'last_update',)  # 'rssi_far', 'rssi_near',
    list_display = ('id', '__str__')


admin.site.register(WatchpostModel, WatchpostAdmin)
