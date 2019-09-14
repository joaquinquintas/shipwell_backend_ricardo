'''
temperature unit module
'''
from __future__ import annotations
from typing import Set, Text


class TemperatureUnit:
    '''
    its a enum primitive to make posible comparate temperature units
    '''

    __CELSIUS = 'celsius'
    __FAHRENHEIT = 'fahrenheit'
    __unit_name: Text

    def __init__(self, unit_name) -> None:
        if unit_name in self.__avaiable_units:
            self.__unit_name = unit_name
            return None

        raise Exception('Unit name %s is not implemented' % unit_name)

    @classmethod
    def make_fahrenheit(cls):
        '''
        factory method to produce a fahrenheit unit
        '''
        return cls(cls.__FAHRENHEIT)

    @classmethod
    def make_celsius(cls):
        '''
        factory method to produce a fahrenheit unit
        '''
        return cls(cls.__CELSIUS)

    @property
    def __avaiable_units(self) -> Set[Text]:
        return {self.__CELSIUS, self.__FAHRENHEIT}

    @property
    def unit_name(self) -> Text:
        '''
        unit name

        :return: float
        '''
        return self.__unit_name

    @property
    def is_celsius(self) -> bool:
        '''
        check if the unit is the celsius unit
        '''
        return self.__unit_name == self.__CELSIUS

    @property
    def is_fahrenheit(self) -> bool:
        '''
        check if the unit is the fahrenheit unit
        '''
        return self.__unit_name == self.__FAHRENHEIT

    def __eq__(self, other: TemperatureUnit) -> bool:
        '''
        compare two temperature units
        '''
        return self.__unit_name == other.unit_name
