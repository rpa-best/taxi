from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from rest_framework import serializers
from rest_framework.exceptions import NotFound
from car.models import Car
from .models import Barrier, BarrierHistory


class BarrierFeatureSerializer(GeoFeatureModelSerializer):

    class Meta:
        model = Barrier
        fields = "__all__"
        geo_field = 'point'


class BarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Barrier
        fields = ['uuid', 'name', 'status']


class BarrierCallSerializer(serializers.Serializer):
    car = serializers.PrimaryKeyRelatedField(queryset=Car.objects.all(), write_only=True)
    lng = serializers.FloatField(write_only=True)
    lat = serializers.FloatField(write_only=True)
    barrier = BarrierSerializer(read_only=True)
    success = serializers.BooleanField(read_only=True)

    def create(self, validated_data):
        point = Point(validated_data['lng'], validated_data['lat'])
        barrier = Barrier.objects.filter(
            point__distance_lt=(point, D(km=2))
        ).annotate(distance=Distance("point", point)).order_by("distance").first()

        if barrier:
            success = barrier.call()
            history = BarrierHistory.objects.create(
                barrier=barrier, 
                car=validated_data['car']
            )
            history.succuss = success
            history.save()
            return {"barrier": barrier, "success": success}
        raise NotFound("Barrier not found")
