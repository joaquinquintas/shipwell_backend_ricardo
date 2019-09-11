'''
weather service abastraction
'''
from abc import ABC, abstractmethod
from core.messages import TemperatureMessage


class AbstractWeatherService(ABC):
    '''
    Weather service interface
    '''

    @abstractmethod
    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        '''
        retrive the temperature data from the implementation of a weather
        service provider

        :param float latitude
        :param float longitude

        :return: TemperatureMessage
        '''
