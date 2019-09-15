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
from typing import Text
from urllib import request, parse
import json
from core.services import AbstractWeatherService
from core.primitives import Temperature, TemperatureUnit, GeoLocation


class AccuWeatherService(AbstractWeatherService):
    '''
    accuweather service implementation
    '''

    __BASE_URL: Text

    def __init__(self, base_url: Text):
        self.__BASE_URL = base_url

    def get_temperature(self, location: GeoLocation) -> Temperature:
        values = {
            'latitude': location.latitude,
            'longitude': location.longitude,
        }
        url_params = parse.urlencode(values)
        url_endpoint = '%s/accuweather' % self.__BASE_URL

        with request.urlopen(f"{url_endpoint}?{url_params}") as response:
            data = json.load(response)
            return Temperature(
                'accuweather',
                float(data["simpleforecast"]["forecastday"][0]["current"]["celsius"]),
                TemperatureUnit.make_celsius() # TODO: reimplement after that the tests pass
            )
