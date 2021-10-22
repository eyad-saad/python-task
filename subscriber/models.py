from django.db import models


class DeviceEntry(models.Model):
    device_id = models.CharField(max_length=50)
    temperature = models.IntegerField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    time = models.DateTimeField()

    class Meta:
        db_table = 'device_entry'
