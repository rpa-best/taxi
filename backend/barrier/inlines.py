from unfold.admin import TabularInline

from .models import BarrierHistory


class BarrierHistoryInline(TabularInline):
    model = BarrierHistory
    extra = 0
    tab = True

    def has_add_permission(self, *args, **kwargs):
        return False
    
    def has_change_permission(self, *args, **kwargs):
        return False
    
    def has_delete_permission(self, *args, **kwargs):
        return False
