'''
Accuweather weather service module
'''
from core.services import AbstractWeatherService
from core.messages import TemperatureMessage


class AccuWeatherService(AbstractWeatherService):
    '''
    accuweather service implementation
    '''

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        # TODO: implements this
        pass
