import uuid
from django.contrib.gis.db import models


class BarrierStatus(models.TextChoices):
    ON = "ON"
    OFF = "OFF"
    NOT_CONNECTION = "NOT_CONNECTION"


class Barrier(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    point = models.PointField(srid=4326)
    status = models.CharField(
        max_length=255, choices=BarrierStatus.choices, default=BarrierStatus.NOT_CONNECTION
    )
    phone = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name
    
    def call(self):
        return True
    

class BarrierHistory(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    barrier = models.ForeignKey(Barrier, on_delete=models.CASCADE)
    succuss = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey("car.Car", on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ["-created_at"]
