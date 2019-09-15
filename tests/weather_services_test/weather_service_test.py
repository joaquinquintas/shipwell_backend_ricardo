from unittest import TestCase

from core.primitives import Temperature, GeoLocation
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestWeatherService(TestCase):

    def setUp(self):
        factory = WeatherServiceFactory()
        self.weather: AbstractWeatherService = factory.make('weatherdotcom')

    def guideline_case_test(self):
        result = self.weather.get_temperature(GeoLocation(12.123123, -12.12312312))
        self.assertIsInstance(result, Temperature)
        self.assertEqual(result.value, 37)
        self.assertTrue(result.unit.is_fahrenheit)
        self.assertEqual(result.provider_name, 'weatherdotcom')

    def to_celsius_test(self):
        result = self.weather.get_temperature(GeoLocation(12.123123, -12.12312312))
        self.assertIsInstance(result, Temperature)
        self.assertEqual(result.to_celsius().value, 2.7777777777777777)


    def none_location_error_test(self):
        self.assertRaises(TypeError, self.weather.get_temperature)
