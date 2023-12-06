import csv
from datetime import datetime
from food_truck_locator_api.models import truck_detail # Replace 'myapp' with your actual app name

def import_truck_detail():
    with open('import_truck_details.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            truck_detail.objects.create(
            name =row['Applicant'],
            location_description =row['LocationDescription'],
            address = row['Address'],
            food_items = row['FoodItems'],
            latitude =  row['Latitude'],
            longitude = row['Longitude'],

            )

if __name__ == '__main__':
    import_truck_detail()