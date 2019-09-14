from unittest import TestCase
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(base_dir, 'infrastructure'))
sys.path.insert(0, os.path.join(base_dir, 'core'))

from core.messages import TemperatureMessage
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestAccuWeatherService(TestCase):

    def accu_weather_service_test(self):
        factory = WeatherServiceFactory()
        accu: AbstractWeatherService = factory.make('accuweather')
        result = accu.get_temperature(123123, 12312312)
        self.assertIsInstance(result, TemperatureMessage)
        self.assertEqual(result.value, 12)
