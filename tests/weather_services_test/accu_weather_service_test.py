from unittest import TestCase
import sys
import os

base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.insert(0, os.path.join(base_dir, 'infrastructure'))
sys.path.insert(0, os.path.join(base_dir, 'core'))

from core.messages import TemperatureMessage
from infrastructure.weather_services import AccuWeatherService


class TestAccuWeatherService(TestCase):

    def accu_weather_service_test(self):
        accu = AccuWeatherService()
        result = accu.get_temperature(123123, 12312312)
        self.assertIsInstance(result, TemperatureMessage)
        self.assertEqual(result.value, 12)
