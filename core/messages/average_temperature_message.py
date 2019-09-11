'''
this module dont need be imported directly, actually the class
AverageTemperatureMessage can be imported by:
from core.message import AverageTemperatureMessage
'''
from statistics import mean
from typing import List
from . import TemperatureMessage


class AverageTemperatureMessage:
    '''
    Final message with the average temperature data
    '''

    __service_data: List[TemperatureMessage]

    def __init__(self, service_data: List[TemperatureMessage]) -> None:
        self.__service_data = service_data

    @property
    def average(self) -> float:
        '''
        final average temperature value

        :return: float
        '''
        return mean([temperature_message for temperature_message in self.__service_data])

    @property
    def service_data(self) -> List[TemperatureMessage]:
        '''
        service result data of TemperatureMessage's responded from the diferent
        weather service providers

        :return: List[TemperatureMessage]
        '''
        return self.__service_data
