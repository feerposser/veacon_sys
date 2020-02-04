from django.contrib import admin

from .models import GatewayBeaconModel


class GatewayBeaconAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)


admin.site.register(GatewayBeaconModel, GatewayBeaconAdmin)
