'''
weather service module
'''
from core.services import AbstractWeatherService
from core.messages import TemperatureMessage


class WeatherService(AbstractWeatherService):
    '''
    noaa weather service implementation
    '''

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        # TODO: implement this service
        pass
