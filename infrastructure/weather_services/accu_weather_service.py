'''
Accuweather weather service module
HERE is the response format
{
    "simpleforecast": {
        "forecastday": [
            {
                "conditions": "Partly Cloudy",
                "current": {
                    "celsius": "12",
                    "fahrenheit": "55"
                },
                "high": {
                    "celsius": "20",
                    "fahrenheit": "68"
                },
                "icon": "partlycloudy",
                "icon_url": "http://icons-ak.wxug.com/i/c/k/partlycloudy.gif",
                "low": {
                    "celsius": "10",
                    "fahrenheit": "50"
                },
                "period": 1,
                "pop": 0,
                "qpf_allday": {
                    "in": 0.0,
                    "mm": 0.0
                },
                "skyicon": "mostlysunny"
            }
        ]
    }
}
'''
from core.services import AbstractWeatherService
from core.messages import TemperatureMessage
from urllib import request, parse
import json


class AccuWeatherService(AbstractWeatherService):
    '''
    accuweather service implementation
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
            'latitude': latitude,
            'longitude': longitude,
        }
        url_params = parse.urlencode(values)
        url_endpoint = '%s/accuweather' % self.__BASE_URL

        with request.urlopen(f"{url_endpoint}?{url_params}") as response:
            data = json.load(response)
            return TemperatureMessage(
                'accu',
                float(data["simpleforecast"]["forecastday"][0]["current"]["celsius"])
            )
