from django.db import models


class TruckDetail(models.Model):
   truck_id = models.AutoField(primary_key=True, editable=False)
   name = models.CharField(max_length=100)
   location_description = models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   food_items=models.TextField()
   latitude =  models.FloatField()
   longitude = models.FloatField()

   class Meta:
        db_table = "trucks"
