from unittest import TestCase

from typing import Set, Text
from core.handlers import FindAverageTemperatureHandler
from core.services import AbstractWeatherService
from core.messages import FindAverageTemperatureMessage
from core.exceptions import NoneWeatherServicesProvided, NoneLocationProvided
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
        '''
        this last service retrive the result on fahrenheit temp unit, but the
        AverageTemperature primitive converts to a single unit begore to
        resolve the average:
        (5 celsius = 41 fahrenheit)
        '''
        return Temperature('five', 41, TemperatureUnit.make_fahrenheit())


class FindAverageTemperatureTest(FindAverageTemperatureMessage):

    __location: GeoLocation
    __services: Set[Text]
    __conversion_unit: Temperature

    def __init__(self, location: GeoLocation, services: Set[Text], conversion_unit: TemperatureUnit) -> None:
        self.__location = location
        self.__services = services
        self.__conversion_unit = conversion_unit

    @property
    def location(self) -> GeoLocation:
        return self.__location

    @property
    def services(self) -> Set[Text]:
        return self.__services

    @property
    def conversion_unit(self) -> TemperatureUnit:
        return self.__conversion_unit


class TestFindAverageTemperature(TestCase):

    def setUp(self):
        self.handler = FindAverageTemperatureHandler({
            'three': MockThreeWhereService(),
            'four': MockFourWhereService(),
            'five': MockFiveWhereService(),
        })

    def all_services_test(self):
        message = FindAverageTemperatureTest(
            GeoLocation(12.1213123, -12.1231231),
            {'five', 'four', 'three'},
            TemperatureUnit.make_celsius()
        )
        result = self.handler.handle(message)
        self.assertIsInstance(result, AverageTemperature)
        self.assertEqual(4, result.average.value)

    def some_services_test(self):
        message = FindAverageTemperatureTest(
            GeoLocation(12.1213123, -12.1231231),
            {'five', 'four'},
            TemperatureUnit.make_celsius()
        )
        result = self.handler.handle(message)
        self.assertIsInstance(result, AverageTemperature)
        self.assertEqual(4.5, result.average.value)

    def none_average_temperature_test(self):
        message = FindAverageTemperatureTest(
            GeoLocation(12.1213123, -12.1231231),
            {},
            TemperatureUnit.make_celsius()
        )
        self.assertRaises(NoneWeatherServicesProvided, self.handler.handle, (message))

    def none_location_test(self):
        message = FindAverageTemperatureTest(
            None,
            {'five', 'four', 'three'},
            TemperatureUnit.make_celsius()
        )
        self.assertRaises(NoneLocationProvided, self.handler.handle, (message))
