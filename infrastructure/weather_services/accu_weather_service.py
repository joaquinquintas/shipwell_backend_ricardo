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
from typing import Text
import json


class AccuWeatherService(AbstractWeatherService):
    '''
    accuweather service implementation
    '''

    __BASE_URL: Text

    def __init__(self, base_url: Text):
        self.__BASE_URL = base_url

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
