from unittest import TestCase

from core.primitives import Temperature, GeoLocation
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestAccuWeatherService(TestCase):

    def accu_weather_service_test(self):
        factory = WeatherServiceFactory()
        accu: AbstractWeatherService = factory.make('accuweather')
        result = accu.get_temperature(GeoLocation(12.123123, 12312312))
        self.assertIsInstance(result, Temperature)
        self.assertEqual(result.value, 12)
