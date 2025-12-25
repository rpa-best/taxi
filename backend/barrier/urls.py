from django.urls import path

from .views import BarrierFeatureView, BarrierCallView

urlpatterns = [
    # path('', BarrierFeatureView.as_view(), name='barrier-features'),
    path('call/', BarrierCallView.as_view(), name='barrier-call'),
]
