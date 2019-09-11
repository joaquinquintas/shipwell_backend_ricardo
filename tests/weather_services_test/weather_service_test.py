from unittest import TestCase
import sys
import os

sys.path.insert(0, '/home/smoke/workspace/weather_mi/infrastructure')
sys.path.insert(0, '/home/smoke/workspace/weather_mi/core')

from core.messages import TemperatureMessage
from infrastructure.weather_services import WeatherService


class TestWeatherService(TestCase):

    def accu_weather_service_test(self):
        weather = WeatherService()
        result = weather.get_temperature(123123, 12312312)
        self.assertIsInstance(result, TemperatureMessage)
        self.assertEqual(result.value, 37)
