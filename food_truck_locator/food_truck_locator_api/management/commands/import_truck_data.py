from django.core.management.base import BaseCommand

import csv
import re
from datetime import datetime
from food_truck_locator_api.models import TruckDetail 


class Command(BaseCommand):
    help = 'Import Trucks Data into Database'

    def handle(self, *args, **kwargs):

        TruckDetail.objects.all().delete()
        with open('food_truck_details.csv', 'r') as file:
            reader = csv.DictReader(file)
            # lat_regex=re.compile(r"^(\+|-)?(?:90(?:(?:\.0{1,6})?)|(?:[0-9]|[1-8][0-9])(?:(?:\.[0-9]{1,6})?))$")
            # long_regex=re.compile(r"^(\+|-)?(?:180(?:(?:\.0{1,6})?)|(?:[0-9]|[1-9][0-9]|1[0-7][0-9])(?:(?:\.[0-9]{1,6})?))$")
            for row in reader:
                lat=float(row['Latitude'])
                log=float(row['Longitude'])
                if ((lat >= -90 and lat <=90) and (log >=-180 and log <=180) and (lat != 0 and log != 0)):
                    TruckDetail.objects.create(
                    name =row['Applicant'],
                    location_description =row['LocationDescription'],
                    address = row['Address'],
                    food_items = row['FoodItems'],
                    latitude =  row['Latitude'],
                    longitude = row['Longitude']
                    )
                else:
                    pass
            
        self.stdout.write("Data Imported")

