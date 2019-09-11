'''
module of the find average temperature handler
'''
from typing import List
from core.services import WeatherService
from core.messages import (
    FindAverageTemperatureMessage,
    AverageTemperatureMessage
)


class FindAverageTemperatureHandler:
    '''
    use case handler that implements the FindAverageTemperatureMessage
    '''

    __weather_services: List[WeatherService]

    def __init__(self, weather_services):
        self.__weather_services = weather_services

    def handle(self, message: FindAverageTemperatureMessage) -> AverageTemperatureMessage:
        '''
        with the temperature message resolve the temperature data

        :param FindAverageTemperatureMessage message

        :return: AverageTemperatureMessage
        '''
        service_data = [
            weather_service.get_temperature(message.latitude, message.longitude)
            for weather_service in self.__weather_services
        ]

        return AverageTemperatureMessage(service_data)
