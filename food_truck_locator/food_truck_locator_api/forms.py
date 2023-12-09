from django import forms
from django.core.validators import ValidationError


class TruckForm(forms.Form):
    latitude = forms.FloatField(label="Latitude")
    longitude = forms.FloatField(label="Longitude")

    def clean_latitude(self):
        latitude = self.cleaned_data['latitude']
        if latitude >= -90 and latitude<=90:
            return latitude
        raise ValidationError("Invalid Latitude")
    def clean_longitude(self):
        longitude = self.cleaned_data['longitude']
        if longitude >= -180 and longitude<=180:
            return longitude
        raise ValidationError("Invalid longitude")
