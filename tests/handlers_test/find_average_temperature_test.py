from unittest import TestCase

from typing import Set, Text
from core.handlers import FindAverageTemperatureHandler
from core.services import AbstractWeatherService
from core.messages import FindAverageTemperatureMessage
from core.primitives import (
    Temperature,
    AverageTemperature,
    GeoLocation,
    TemperatureUnit
)


class MockThreeWhereService(AbstractWeatherService):

    def get_temperature(self, location: GeoLocation) -> Temperature:
        return Temperature('three', 3, TemperatureUnit.make_celsius())


class MockFourWhereService(AbstractWeatherService):

    def get_temperature(self, location: GeoLocation) -> Temperature:
        return Temperature('four', 4, TemperatureUnit.make_celsius())


class MockFiveWhereService(AbstractWeatherService):

    def get_temperature(self, location: GeoLocation) -> Temperature:
        return Temperature('five', 5, TemperatureUnit.make_celsius())


class FindAverageTemperatureTest(FindAverageTemperatureMessage):

    @property
    def location(self) -> GeoLocation:
        return GeoLocation(12.123112, -13.123123)

    @property
    def services(self) -> Set[Text]:
        return {}

    @property
    def conversion_unit(self) -> TemperatureUnit:
        return TemperatureUnit.make_celsius()


class TestFindAverageTemperature(TestCase):

    def find_average_temperature_test(self):
        handler = FindAverageTemperatureHandler([
            MockThreeWhereService(),
            MockFourWhereService(),
            MockFiveWhereService(),
        ])
        result = handler.handle(FindAverageTemperatureTest())
        self.assertIsInstance(result, AverageTemperature)
        self.assertEqual(4, result.average.value)
