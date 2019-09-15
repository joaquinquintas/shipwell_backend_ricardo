from unittest import TestCase

from core.primitives import Temperature, GeoLocation
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestNoaaWeatherService(TestCase):

    def accu_weather_service_test(self):
        factory = WeatherServiceFactory()
        noaa: AbstractWeatherService = factory.make('noaa')
        result = noaa.get_temperature(GeoLocation(12.123123, 12.12312312))
        self.assertIsInstance(result, Temperature)
        self.assertEqual(result.value, 12)
