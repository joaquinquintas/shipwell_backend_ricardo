'''
Temperature primitive module
'''
from __future__ import annotations
from typing import Text
from .temperature_unit import TemperatureUnit


class Temperature:
    '''
    Temperature premitive provide a solution for representing temperature
    values, units and data origin
    '''

    __service_name: Text
    __value: float
    __unit: TemperatureUnit

    def __init__(self, service_name: Text, value: float, unit: TemperatureUnit):
        self.__service_name = service_name
        self.__value = value
        self.__unit = unit

    @property
    def provider_name(self) -> Text:
        '''
        the service name that provide the temperature data

        :return: Text
        '''
        return self.__service_name

    @property
    def value(self) -> float:
        '''
        temperature value

        :return: float
        '''
        return self.__value

    @property
    def unit(self) -> TemperatureUnit:
        '''
        temperature unit

        :return: float
        '''
        return self.__unit

    def to_celsius(self) -> Temperature:
        '''
        converts the temperature object to a celcius representation

        :return: Temperature
        '''

        if self.__unit.is_fahrenheit:
            celsius_value = (self.__value - 32) * 5.0/9.0
            return Temperature(
                self.__service_name,
                celsius_value,
                TemperatureUnit.make_celsius()
            )

        return self

    def to_fahrenheit(self) -> Temperature:
        '''
        converts the temperature object to a fahrenheit representation

        :return: Temperature
        '''

        if self.__unit.is_celsius:
            fahrenheit_value = (self.__value * 1.8) + 32
            return Temperature(
                self.__service_name,
                fahrenheit_value,
                TemperatureUnit.make_fahrenheit()
            )

        return self
