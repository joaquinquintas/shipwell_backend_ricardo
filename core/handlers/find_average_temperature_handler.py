'''
module of the find average temperature handler
'''
from typing import Dict, Text
from core.services import AbstractWeatherService
from core.messages import FindAverageTemperatureMessage
from core.primitives import AverageTemperature
from core.exceptions import NoneLocationProvided, NoneWeatherServicesProvided


class FindAverageTemperatureHandler:
    '''
    use case handler that implements the FindAverageTemperatureMessage
    '''

    __weather_services: Dict[Text, AbstractWeatherService]

    def __init__(self, weather_services):
        self.__weather_services = weather_services

    def handle(self, message: FindAverageTemperatureMessage) -> AverageTemperature:
        '''
        with the temperature message resolve the temperature data

        :param FindAverageTemperatureMessage message

        :return: AverageTemperatureMessage
        '''

        self.__check_message(message)

        service_data = [
            weather_service.get_temperature(message.location)
            for service_name, weather_service in self.__weather_services.items()
            if service_name in message.services
        ]

        return AverageTemperature(service_data, message.conversion_unit)

    def __check_message(self, message: FindAverageTemperatureMessage):
        if not message.location:
            raise NoneLocationProvided()

        if not message.services:
            raise NoneWeatherServicesProvided()
