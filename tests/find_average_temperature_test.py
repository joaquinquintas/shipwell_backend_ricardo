from unittest import TestCase
import sys
import os

sys.path.insert(0, '/home/smoke/workspace/weather_mi/core')

from core.handlers import FindAverageTemperatureHandler
from core.services import AbstractWeatherService
from core.messages import (
    FindAverageTemperatureMessage,
    TemperatureMessage,
    AverageTemperatureMessage
)


class MockThreeWhereService(AbstractWeatherService):

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        return TemperatureMessage('three', 3.0)


class MockFourWhereService(AbstractWeatherService):

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        return TemperatureMessage('four', 4.0)


class MockFiveWhereService(AbstractWeatherService):

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        return TemperatureMessage('five', 5.0)


class TestFindAverageTemperature(TestCase):

    def find_average_temperature_test(self):
        handler = FindAverageTemperatureHandler([
            MockThreeWhereService(),
            MockFourWhereService(),
            MockFiveWhereService(),
        ])
        result = handler.handle(FindAverageTemperatureMessage(10121.121, -10121.121, []))
        self.assertIsInstance(result, AverageTemperatureMessage)
        self.assertEqual(4, result.average)
