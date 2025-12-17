from django.contrib import admin
from django.contrib.gis.admin.options import GeoModelAdminMixin
from unfold.admin import ModelAdmin

from .inlines import BarrierHistoryInline
from .models import Barrier

@admin.register(Barrier)
class BarrierAdmin(GeoModelAdminMixin, ModelAdmin):
    inlines = [BarrierHistoryInline]
    readonly_fields = ['status']
