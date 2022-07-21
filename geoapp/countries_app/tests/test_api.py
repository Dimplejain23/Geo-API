import json
import requests
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from countries_app.models import Countries
from countries_app.serializers import CountrySerializer

# initialize the APIClient app
client = Client()

class GeoApiTest(TestCase):

    def setUp(self):
        self.name = 'dummy'
        self.update_payload = {"iso_a3":"TT"}
        self.payload = {"admin":"test","iso_a3":"TT","geometry":"Polygon ((93.46169130199361064 36.22999858415099084, 93.75444245735633331 33.3024870305237215, 102.97610385128223243 33.59523818588644417, 101.21959691910586798 37.54737878328326417, 102.89889259016469225 53.6935343678431849, 93.46169130199361064 36.22999858415099084))"}
        self.search_string = 'ch'
        self.geom = self.payload['geometry']
        self.dummy_data = Countries.objects.create(admin="dummy",iso_a3="TU",geometry='Point (73.56 21.27)')

    def test_add_country(self):
        response = client.post(
            reverse('create-country'),
            data=json.dumps(self.payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    
    def get_all_countries(self):
        response = client.get(reverse('get-all-countries'))
        countries = Countries.objects.all()
        serializer = CountrySerializer(countries, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_country(self):
        response = client.put(
            reverse('update-country', kwargs={'name': self.name}),
            data=json.dumps(self.update_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_country(self):
        response = client.delete(
            reverse('delete-country', kwargs={'name': self.name}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_search_country(self):
        response = requests.get('http://localhost:8000/api/search/ch/')
        self.assertEqual(len(response.json()),10)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_spatial_query_geom(self):
        response = requests.get(f'http://localhost:8000/api/sgeomquery/{self.geom}/')
        self.assertEqual(len(response.json()),3)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_spatial_query_country(self):
        response = requests.get(f'http://localhost:8000/api/squerybycountry/India/')
        self.assertEqual(len(response.json()),8)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
