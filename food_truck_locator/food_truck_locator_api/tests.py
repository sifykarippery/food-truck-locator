from django.test import SimpleTestCase,TestCase
from django.urls import reverse
from .models import TruckDetail
from .forms import TruckForm

class HomepageTests(SimpleTestCase):
    def test_home_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

class TruckModelTestCase(TestCase):
    def setUp(self):
        TruckDetail.objects.create(
                    name ='Test Object',
                    location_description = 'Test LocationDescription',
                    address = 'Test Address',
                    food_items = 'Test FoodItems',
                    latitude =  36.778259,
                    longitude = -119.417931
                    )

    def test_model_str_method(self):
        obj = TruckDetail.objects.get(name='Test Object')
        self.assertEqual(str(obj.address), 'Test Address')

class TruckViewTestCase(TestCase):
    def test_view_returns_200(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)


class TruckFormTestCase(TestCase):
    def test_valid_form(self):
        # Test a valid form submission
        form_data = {'latitude': '36.778259', 'longitude': '-112.417931'}

        form = TruckForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        # Test an invalid form submission
        form_data = {'latitude': '', 'longitude':''}
        form = TruckForm(data=form_data)
        self.assertFalse(form.is_valid())