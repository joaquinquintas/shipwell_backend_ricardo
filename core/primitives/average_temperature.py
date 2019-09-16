'''
this module dont need be imported directly, actually the class
AverageTemperatureMessage can be imported by:
from core.message import AverageTemperatureMessage
'''
from statistics import mean
from typing import List
from core.primitives import Temperature, TemperatureUnit
from core.exceptions import (
    NoneWeatherServiceDataRetrived,
    ConversionUnitNotImplemented
)


class AverageTemperature:
    '''
    Final message with the average temperature data
    '''

    __service_data: List[Temperature]
    __conversion_unit: TemperatureUnit

    def __init__(self, service_data: List[Temperature], conversion_unit: TemperatureUnit) -> None:

        if not service_data:
            raise NoneWeatherServiceDataRetrived()

        self.__service_data = service_data
        self.__conversion_unit = conversion_unit

    def __converted_data(self):
        '''
        no need that the original data retrived from services change, only
        convert to a common unit for achive the average
        '''

        for temperature in self.__service_data:
            converted = False

            if self.__conversion_unit.is_celsius:
                yield temperature.to_celsius()
                converted = True

            if self.__conversion_unit.is_fahrenheit:
                yield temperature.to_fahrenheit()
                converted = True

            if not converted:
                raise ConversionUnitNotImplemented(self.__conversion_unit.unit_name)

    @property
    def average(self) -> Temperature:
        '''
        final average temperature value

        :return: Temperature
        '''
        average = mean([temperature.value for temperature in self.__converted_data()])
        return Temperature(
            'weather_mi',
            average,
            self.__conversion_unit
        )

    @property
    def service_data(self) -> List[Temperature]:
        '''
        service result data of Temperature's responded from the diferent
        weather service providers

        :return: List[Temperature]
        '''
        return self.__service_data
