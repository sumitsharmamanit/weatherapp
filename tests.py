from django.test import TestCase, Client
from django.urls import reverse
from .models import City


class WeatherAppTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.city = City.objects.create(name='London')

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')
        self.assertContains(response, self.city.name)

    def test_add_city_view(self):
        response = self.client.post(reverse('index'), {'name': 'New York'})
        self.assertEqual(response.status_code, 302)  # Redirect after POST
        new_city = City.objects.get(name='New York')
        self.assertIsNotNone(new_city)

    def test_weather_data_display(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'London')

    def test_add_city_view_missing_name(self):
        response = self.client.post(reverse('index'), {})
        self.assertEqual(response.status_code, 400)  # Expect 400 for missing cit

    def test_add_city_view_existing_city(self):
        response = self.client.post(reverse('index'), {'name': 'London'})
        self.assertEqual(response.status_code, 400)  # Expect 400 for existing city

    def test_invalid_city_name(self):
        response = self.client.post(reverse('index'), {'name': 'InvalidCityName'})
        self.assertEqual(response.status_code, 400)  # Expect 400 for invalid city name

    def tearDown(self):
        self.city.delete()
