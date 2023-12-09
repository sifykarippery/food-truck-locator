from django.http import HttpResponse
from .models import TruckDetail
from django.db.models import F
#
from django.db.models.functions import ACos, Cos, Radians, Sin
from django.shortcuts import render

from .forms import TruckForm

def nearest_truck(lat,lng):
    locations = TruckDetail.objects.annotate(
        distance_miles=ACos(
            Cos(
                Radians(float(lat))
            ) * Cos(
                Radians(F('latitude'))
            ) * Cos(
                Radians(F('longitude')) - Radians(float(lng))
            ) + Sin(
                Radians(float(lat))
            ) * Sin(Radians(F('latitude')))
        ) * 3959
    ).order_by('distance_miles')[:5]
    return locations


def index(request):
    # if this is a POST request we need to process the form data
    try:
        if request.method == "POST":
            # create a form instance and populate it with data from the request:
            form = TruckForm(request.POST)
            # check whether it's valid:
            if form.is_valid():
                lat = request.POST['latitude']
                lng = request.POST['longitude']
                locations = nearest_truck(lat,lng)
                context = {
                    'food_trucks': locations
                }
                return render(request, 'index.html', context)

        else:
            form = TruckForm()
        return render(request, "index.html", {"form": form})
    except Exception as e:
        return e




