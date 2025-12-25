from rest_framework_gis.serializers import GeoFeatureModelSerializer
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import D
from django.contrib.gis.db.models.functions import Distance
from rest_framework import serializers
from rest_framework.exceptions import NotFound, ValidationError
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
    lng = serializers.FloatField(write_only=True)
    lat = serializers.FloatField(write_only=True)
    barrier = BarrierSerializer(read_only=True)
    success = serializers.BooleanField(read_only=True)

    def validate(self, attrs):
        point = Point(attrs['lng'], attrs['lat'])
        barrier = Barrier.objects.filter(
            point__distance_lt=(point, D(km=0.6))
        ).annotate(distance=Distance("point", point)).order_by("distance").first()
        
        if not barrier:
            raise NotFound("Barrier not found")
        
        attrs['barrier'] = barrier

        if barrier and self.context['request'].user not in barrier.users.all():
            raise ValidationError("You are not allowed to call this barrier")
        return attrs

    def create(self, validated_data):
        barrier: Barrier = validated_data.get('barrier')
        success = barrier.call()
        history = BarrierHistory.objects.create(
            barrier=barrier, 
            car=validated_data['car']
        )
        history.succuss = success
        history.save()
        return {"barrier": barrier, "success": success}
