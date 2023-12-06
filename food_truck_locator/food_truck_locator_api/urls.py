from django.urls import include, path

from rest_framework import routers

from food_truck_locator_api.views import Truck_detailViewSet

router = routers.DefaultRouter()
router.register(r'people', Truck_detailViewSet)

urlpatterns = [
   path('', include(router.urls)),
]