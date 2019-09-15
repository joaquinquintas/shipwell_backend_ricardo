'''
module of the find average temperature handler
'''
from typing import List
from core.services import AbstractWeatherService
from core.messages import FindAverageTemperatureMessage
from core.primitives import AverageTemperature


class FindAverageTemperatureHandler:
    '''
    use case handler that implements the FindAverageTemperatureMessage
    '''

    __weather_services: List[AbstractWeatherService]

    def __init__(self, weather_services):
        self.__weather_services = weather_services

    def handle(self, message: FindAverageTemperatureMessage) -> AverageTemperature:
        '''
        with the temperature message resolve the temperature data

        :param FindAverageTemperatureMessage message

        :return: AverageTemperatureMessage
        '''
        service_data = [
            weather_service.get_temperature(message.location)
            for weather_service in self.__weather_services
        ]

        return AverageTemperature(service_data, message.conversion_unit)
