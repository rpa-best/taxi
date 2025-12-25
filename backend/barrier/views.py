from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .serializers import BarrierFeatureSerializer, BarrierCallSerializer
from .models import Barrier


class BarrierFeatureView(ListAPIView):
    queryset = Barrier.objects.all()
    serializer_class = BarrierFeatureSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class BarrierCallView(CreateAPIView):
    queryset = Barrier.objects.all()
    serializer_class = BarrierCallSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    