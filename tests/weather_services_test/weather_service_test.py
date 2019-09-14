from unittest import TestCase
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(base_dir, 'core'))
sys.path.insert(0, os.path.join(base_dir, 'infrastructure'))

from core.messages import TemperatureMessage
from core.services import AbstractWeatherService
from infrastructure.factories import WeatherServiceFactory


class TestWeatherService(TestCase):

    def accu_weather_service_test(self):
        factory = WeatherServiceFactory()
        weather: AbstractWeatherService = factory.make('weatherdotcom')
        result = weather.get_temperature(123123, 12312312)
        self.assertIsInstance(result, TemperatureMessage)
        self.assertEqual(result.value, 37)
