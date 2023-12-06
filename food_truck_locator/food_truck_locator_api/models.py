from django.db import models

class truck_detail(models.Model):
   truck_id = models.AutoField(primary_key=True, editable=False)
   name = models.CharField(max_length=100)
   location_description = models.CharField(max_length=100)
   address=models.CharField(max_length=100)
   food_items=models.TextField()
   latitude =  models.CharField('Latitude', max_length=20, null=True, blank=True)
   longitude = models.CharField('Latitude', max_length=20, null=True, blank=True)
# Create your models here.
