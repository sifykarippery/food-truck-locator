from rest_framework import serializers
from food_truck_locator_api.models import TruckDetail

class Truck_detailSerializer(serializers.ModelSerializer):
   class Meta:
       model = TruckDetail
       fields = ('truck_id','name','location_description','address','food_items','latitude','longitude')