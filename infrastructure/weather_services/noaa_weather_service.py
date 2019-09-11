'''
noaa weather service module
{
    "today": {
        "current": {
            "celsius": "12",
            "fahrenheit": "55"
        },
        "high": {
            "celsius": "20",
            "fahrenheit": "68"
        },
        "low": {
            "celsius": "10",
            "fahrenheit": "50"
        }
    }
}
'''
from core.services import AbstractWeatherService
from core.messages import TemperatureMessage
from urllib import request, parse
import json


class NoaaWeatherService(AbstractWeatherService):
    '''
    noaa weather service implementation
    '''

    __BASE_URL: str

    def __init__(self):
        # la idea seria traer la configuracion de settings.WHEATER_SERVICES
        # pero al mismo tiempo tengo que contrar un modo de que lo tome la
        # bateria de pruebas, lo ideal para resolver este problema es poder
        # contar con un mecanismo de inyeccion de dependencias automatico y
        # python los tiene pero no me alcanza el tiempo para implementarlo
        self.__BASE_URL = 'http://127.0.0.1:5000'

    def get_temperature(self, latitude: float, longitude: float) -> TemperatureMessage:
        values = {
            'latlon': f"{latitude},{longitude}"
        }
        url_params = parse.urlencode(values)
        url_endpoint = '%s/noaa' % self.__BASE_URL

        with request.urlopen(f"{url_endpoint}?{url_params}") as response:
            data = json.load(response)
            return TemperatureMessage(
                'noaa',
                float(data["today"]["current"]["celsius"])
            )
