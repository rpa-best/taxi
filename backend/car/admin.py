from django.contrib import admin
from unfold.admin import ModelAdmin
from barrier.inlines import BarrierHistoryInline
from .models import Car


@admin.register(Car)
class CarAdmin(ModelAdmin):
    inlines = [BarrierHistoryInline]
