'''
$ curl http://localhost:8000/average_temperature/\?latitude\=12.23\&longitude\=-12.23\&services\[\]\=noaa\&services\[\]\=weatherdotcom\&services\[\]\=accuweather
'''

from django.test import TestCase, Client


class AverageTemperatureRequestTest(TestCase):

    def setUp(self):
        self.client = Client()

    def test_full_case(self):
        response = self.client.get('/average_temperature/', {
            'latitude': 12.23,
            'longitude': -12.23,
            'services[]': ['noaa', 'weatherdotcom', 'accuweather']
        })
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual('celsius', data['data']['average']['unit'])
        self.assertEqual(8.9, data['data']['average']['value'])

    def test_filtering_some_service(self):
        response = self.client.get('/average_temperature/', {
            'latitude': 12.23,
            'longitude': -12.23,
            'services[]': ['noaa', 'accuweather']
        })
        self.assertEqual(200, response.status_code)
        data = response.json()
        self.assertEqual('celsius', data['data']['average']['unit'])
        self.assertEqual(12, data['data']['average']['value'])

    def test_missing_latitude_validation(self):
        response = self.client.get('/average_temperature/', {
            'longitude': -12.23,
            'services[]': ['noaa', 'weatherdotcom', 'accuweather']
        })
        self.assertEqual(403, response.status_code)
        error = response.json()
        self.assertIn('must fill the field: latitude', error['error']['messages'])

    def test_missing_longitude_validation(self):
        response = self.client.get('/average_temperature/', {
            'latitude': 12.23,
            'services[]': ['noaa', 'weatherdotcom', 'accuweather']
        })
        self.assertEqual(403, response.status_code)
        error = response.json()
        self.assertIn('must fill the field: longitude', error['error']['messages'])

    def test_missing_services_validation(self):
        response = self.client.get('/average_temperature/', {
            'latitude': 12.23,
            'longitude': -12.23,
        })
        self.assertEqual(403, response.status_code)
        error = response.json()
        self.assertIn('must fill the field: services[]', error['error']['messages'])
