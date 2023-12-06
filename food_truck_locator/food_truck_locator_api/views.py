from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from food_truck_locator_api.serializers import Truck_detailSerializer
from food_truck_locator_api.models import truck_detail


class Truck_detailViewSet(viewsets.ModelViewSet):
   queryset =  truck_detail.objects.all()
   serializer_class = Truck_detailSerializer


