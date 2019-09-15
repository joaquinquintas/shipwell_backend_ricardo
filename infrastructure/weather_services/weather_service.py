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
from typing import Text
from urllib import request, parse
import json
from core.services import AbstractWeatherService
from core.primitives import Temperature, TemperatureUnit, GeoLocation


class WeatherService(AbstractWeatherService):
    '''
    noaa weather service implementation
    '''
    __BASE_URL: Text

    def __init__(self, base_url: Text):
        self.__BASE_URL = base_url

    def get_temperature(self, location: GeoLocation) -> Temperature:
        values = {
            'lat': location.latitude,
            'lon': location.longitude,
        }
        payload = json.dumps(values).encode('ascii')
        url_endpoint = '%s/weatherdotcom' % self.__BASE_URL
        weather_request = request.Request(url_endpoint, payload)
        weather_request.add_header('Content-Type', 'application/json')

        with request.urlopen(weather_request) as response:
            data = json.load(response)
            return Temperature(
                'weatherdotcom',
                float(data['query']['results']['channel']['condition']['temp']),
                TemperatureUnit.make_fahrenheit()
            )
