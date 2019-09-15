'''
weather service abastraction
'''
from abc import ABC, abstractmethod
from core.primitives import Temperature, GeoLocation


class AbstractWeatherService(ABC):
    '''
    Weather service interface
    '''

    @abstractmethod
    def get_temperature(self, location: GeoLocation) -> Temperature:
        '''
        retrive the temperature data from the implementation of a weather
        service provider

        :param float latitude
        :param float longitude

        :return: TemperatureMessage
        '''
