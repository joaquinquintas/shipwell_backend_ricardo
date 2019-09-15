'''
request adapter module
'''
from typing import Set, Text
from django.http.request import HttpRequest
from django.conf import settings
from core.messages import FindAverageTemperatureMessage
from core.primitives import GeoLocation, TemperatureUnit

class FindAverageTemperatureRequest(FindAverageTemperatureMessage):
    '''
    adapts the HttpRequest object to the FindAverageTemperatureMessage
    abstraction
    '''

    __request: HttpRequest
    __conversion_unit: TemperatureUnit

    def __init__(self, request: HttpRequest):
        self.__request = request
        self.__conversion_unit = None

    @property
    def location(self) -> GeoLocation:
        latitude = float(self.__request.GET.get('latitude', ''))
        longitude = float(self.__request.GET.get('longitude', ''))
        return GeoLocation(latitude, longitude)

    @property
    def services(self) -> Set[Text]:
        return {service_name for service_name in self.__request.GET.getlist('services[]', [])}

    @property
    def conversion_unit(self) -> TemperatureUnit:
        if self.__conversion_unit:
            return self.__conversion_unit

        if settings.AVERAGE_CONVERSION_UNIT == 'C':
            self.__conversion_unit = TemperatureUnit.make_celsius()

        if settings.AVERAGE_CONVERSION_UNIT == 'F':
            self.__conversion_unit = TemperatureUnit.make_fahrenheit()

        if not self.__conversion_unit:
            import pdb; pdb.set_trace()
            raise Exception('Conversion unit not configured !!')

        return self.__conversion_unit
