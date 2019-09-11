'''
this module dont need be imported directly, actually the class
TemperatureMessage can be imported by:
from core.message import TemperatureMessage
'''
from typing import Text


class TemperatureMessage:
    '''
    DTO's Interface for the temperature data provided for the weather data
    services
    '''

    @property
    def service_name(self) -> Text:
        '''
        the service name that provide the temperature data

        :return: Text
        '''

    @property
    def value(self) -> float:
        '''
        temperature value in celsius degrees

        :return: float
        '''
