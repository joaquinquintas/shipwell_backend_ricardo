'''
this module dont need be imported directly, actually the class
FindAverageTemperatureMessage can be imported by:
from core.message import FindAverageTemperatureMessage
'''
from typing import List, Text, Set


class FindAverageTemperatureMessage:
    '''
    DTO's for the average temperature Request
    '''

    __latitude: float
    __longitude: float
    __services: List[Text]


    def __init__(self, latitude: float, longitude: float, services: List[Text]) -> None:
        self.__latitude = latitude
        self.__longitude = longitude
        self.__services = services

    @property
    def latitude(self) -> float:
        '''
        latitude field of the location of interest

        :return: float
        '''
        return self.__latitude

    @property
    def longitude(self) -> float:
        '''
        longitude field of the location of interes

        :return: float
        '''
        return self.__longitude

    @property
    def services(self) -> Set[Text]:
        '''
        weather service set applied to the average temperature data

        :return: List[Text]
        '''
        return set(self.__services)
