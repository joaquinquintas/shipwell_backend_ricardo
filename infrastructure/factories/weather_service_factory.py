'''
weather service factory
'''
from typing import Text
from core.services import AbstractWeatherService
from infrastructure import weather_services as ws


class WeatherServiceNotImplemented(Exception):
    '''
    exception type for the weather service not implemented
    '''


class WeatherServiceFactory:
    '''
    Weather service factory method
    '''

    __SERVICE_TYPES = {
        'noaa': ws.NoaaWeatherService,
        'weather.com': ws.WeatherService,
        'accuweather': ws.AccuWeatherService,
    }

    def make(self, service_implementation: Text) -> AbstractWeatherService:
        '''
        factory method that instatiate the service of a given type

        :param Text service_implementation
        '''
        if service_implementation in self.__SERVICE_TYPES:
            return self.__SERVICE_TYPES[service_implementation]()

        raise WeatherServiceNotImplemented(
            f'Service: {service_implementation} NOT implemented'
        )
