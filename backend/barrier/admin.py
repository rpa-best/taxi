from django.contrib import admin
from django.contrib.gis.admin.options import GeoModelAdminMixin
from unfold.admin import ModelAdmin
from backend.widgets import GeoWidget

from .inlines import BarrierHistoryInline
from .models import Barrier

@admin.register(Barrier)
class BarrierAdmin(GeoModelAdminMixin, ModelAdmin):
    inlines = [BarrierHistoryInline]
    gis_widget = GeoWidget

    readonly_fields = ("latitude", "longitude", 'status')

    fieldsets = (
        (None, {
            "fields": ("name", "status", "phone")
        }),
        ("Location", {
            "fields": ("point", "latitude", "longitude")
        }),
    )

    def latitude(self, obj: Barrier):
        return obj.point.y if obj.point else None

    def longitude(self, obj: Barrier):
        return obj.point.x if obj.point else None

    latitude.short_description = "Latitude"
    longitude.short_description = "Longitude"
