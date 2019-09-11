'''
weather service module
{
    "query": {
        "count": 1,
        "created": "2017-09-21T17:00:22Z",
        "lang": "en-US",
        "results": {
            "channel": {
                "astronomy": {
                    "sunrise": "8:42 am",
                    "sunset": "9:6 pm"
                },
                "atmosphere": {
                    "humidity": "80",
                    "pressure": "1014.0",
                    "rising": "0",
                    "visibility": "16.1"
                },
                "condition": {
                    "code": "33",
                    "date": "Thu, 21 Sep 2017 08:00 AM AKDT",
                    "temp": "37",
                    "text": "Mostly Clear"
                },
                "description": "Current Weather",
                "item": {
                    "guid": {
                        "isPermaLink": "false"
                    },
                    "lat": "64.499474",
                    "long": "-165.405792",
                    "pubDate": "Thu, 21 Sep 2017 08:00 AM AKDT",
                    "title": "Conditions for Nome, AK, US at 08:00 AM AKDT"
                    "temperature": "F"
                }
            }
        }
    }
}
'''
from django.conf import settings
from core.services import AbstractWeatherService
from core.messages import TemperatureMessage
from urllib import request, parse
import json


class WeatherService(AbstractWeatherService):
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
            'lat': latitude,
            'lon': longitude,
        }
        payload = json.dumps(values).encode('ascii')
        url_endpoint = '%s/weatherdotcom' % self.__BASE_URL
        weather_request = request.Request(url_endpoint, payload)
        weather_request.add_header('Content-Type', 'application/json')
        with request.urlopen(weather_request) as response:
            data = json.load(response)
            return TemperatureMessage(
                'weather.com',
                float(data['query']['results']['channel']['condition']['temp'])
            )
