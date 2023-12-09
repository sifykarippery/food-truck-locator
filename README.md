# food-truck-locator
The Problem : World Needs More Food Trucks!


## Run Migrations

Please run migrations after activating environments
Make sure pyenv and pipenv installed 



```
pipenv shell          # this will activate virtual env
pipenv install        # Install dependencies

cd food_truck_locator
python manage.py migrate        # Run the migrations

python manage.py import_truck_data   # to import the sample CSV data

```