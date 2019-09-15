from unittest import TestCase

from core.primitives import Temperature, GeoLocation
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestNoaaWeatherService(TestCase):

    def setUp(self):
        factory = WeatherServiceFactory()
        self.noaa: AbstractWeatherService = factory.make('noaa')

    def guideline_case_test(self):
        result: Temperature = self.noaa.get_temperature(GeoLocation(12.123123, 12.12312312))
        self.assertIsInstance(result, Temperature)
        self.assertEqual(result.value, 12)
        self.assertTrue(result.unit.is_celsius)
        self.assertEqual(result.provider_name, 'noaa')

    def none_location_error_test(self):
        self.assertRaises(TypeError, self.noaa.get_temperature)
