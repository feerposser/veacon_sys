from django.contrib import admin

from .models import AlertModel


class AlertAdmin(admin.ModelAdmin):
      readonly_fields = ('date', 'hour')


admin.site.register(AlertModel, AlertAdmin)

