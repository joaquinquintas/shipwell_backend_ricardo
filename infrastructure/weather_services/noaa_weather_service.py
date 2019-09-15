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
from typing import Text
from urllib import request, parse
import json
from core.services import AbstractWeatherService
from core.primitives import Temperature, TemperatureUnit, GeoLocation


class NoaaWeatherService(AbstractWeatherService):
    '''
    noaa weather service implementation
    '''

    __BASE_URL: Text

    def __init__(self, base_url: Text):
        self.__BASE_URL = base_url

    def get_temperature(self, location: GeoLocation) -> Temperature:
        values = {
            'latlon': f"{location.latitude},{location.longitude}"
        }
        url_params = parse.urlencode(values)
        url_endpoint = '%s/noaa' % self.__BASE_URL

        with request.urlopen(f"{url_endpoint}?{url_params}") as response:
            data = json.load(response)
            return Temperature(
                'noaa',
                float(data["today"]["current"]["celsius"]),
                TemperatureUnit.make_celsius() # TODO: change this implementation after pass the tests
            )
