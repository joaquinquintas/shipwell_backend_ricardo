'''
find average temperature module
'''
from abc import ABCMeta, abstractmethod
from typing import Text, Set
from core.primitives import GeoLocation, TemperatureUnit


class FindAverageTemperatureMessage:
    '''
    DTO's interface for the average temperature Request
    '''
    __metaclass__ = ABCMeta

    @property
    @abstractmethod
    def location(self) -> GeoLocation:
        '''
        retrive the GeoLocation primitive of the requested location

        :return: GeoLocation
        '''

    @property
    @abstractmethod
    def services(self) -> Set[Text]:
        '''
        weather service set applied to the average temperature data

        :return: List[Text]
        '''

    @property
    @abstractmethod
    def conversion_unit(self) -> TemperatureUnit:
        '''
        spesify the temperature unit for AverageTemperature primitive

        :return: TemperatureUnit
        '''
