'''
weather service factory
'''
from typing import Text
from core.services import AbstractWeatherService
from infrastructure import weather_services as ws
from infrastructure import config
from infrastructure.exceptions import (
    WeatherServiceNotImplemented,
    WeatherServiceNotConfigured
)


class WeatherServiceFactory:
    '''
    Weather service factory method
    '''

    __SERVICE_TYPES = {
        'noaa': {
            'class_name': ws.NoaaWeatherService,
            'config_section': 'noaa-connection',
        },
        'weatherdotcom': {
            'class_name': ws.WeatherService,
            'config_section': 'weatherdotcom-connection',
        },
        'accuweather': {
            'class_name': ws.AccuWeatherService,
            'config_section': 'accuweather-connection'
        }
    }

    def make(self, service_implementation: Text) -> AbstractWeatherService:
        '''
        factory method that instatiate the service of a given type

        :param Text service_implementation
        '''
        config
        if service_implementation in self.__SERVICE_TYPES:
            service_config = self.__get_config(service_implementation)
            return self.__SERVICE_TYPES[service_implementation]['class_name'](service_config.get('base_url'))

        raise WeatherServiceNotImplemented(service_implementation)

    def __get_config(self, service_name: Text):
        service_config_section = self.__SERVICE_TYPES[service_name]['config_section']

        if service_config_section in config:
            return config[service_config_section]

        raise WeatherServiceNotConfigured(service_name)
