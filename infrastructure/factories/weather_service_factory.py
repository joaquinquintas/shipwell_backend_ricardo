'''
weather service factory
'''
from typing import Text
from core.services import AbstractWeatherService
from infrastructure import weather_services as ws
from infrastructure import config


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
        'weatherdotcom': ws.WeatherService,
        'accuweather': ws.AccuWeatherService,
    }

    def make(self, service_implementation: Text) -> AbstractWeatherService:
        '''
        factory method that instatiate the service of a given type

        :param Text service_implementation
        '''
        config
        if service_implementation in self.__SERVICE_TYPES:
            service_config = self.__get_config(service_implementation)
            return self.__SERVICE_TYPES[service_implementation](service_config.get('base_url'))

        raise WeatherServiceNotImplemented(
            f'Service: {service_implementation} NOT implemented'
        )

    def __get_config(self, service_name: Text):
        service_config_section = '%s-connection' % service_name

        if service_config_section in config:
            return config[service_config_section]

        raise Exception('Weather service not configured')
