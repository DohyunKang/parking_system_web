from django.db import models

class ParkingLot(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    capacity = models.IntegerField()
    available_spots = models.IntegerField()

    def __str__(self):
        return self.name