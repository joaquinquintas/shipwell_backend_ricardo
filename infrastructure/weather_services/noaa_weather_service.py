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
from typing import Text
import json


class NoaaWeatherService(AbstractWeatherService):
    '''
    noaa weather service implementation
    '''

    __BASE_URL: Text

    def __init__(self, base_url: Text):
        self.__BASE_URL = base_url

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
