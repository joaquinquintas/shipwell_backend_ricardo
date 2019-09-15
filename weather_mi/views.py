'''
django main view for the weather average data
'''
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from infrastructure.factories import WeatherServiceFactory
from core.messages import FindAverageTemperatureMessage, AverageTemperatureMessage
from core.handlers import FindAverageTemperatureHandler


def index(request: HttpRequest) -> JsonResponse:
    '''
    resive a HttpRequest object with latitude, longitude, and weather services
    used to retrive the temperature information of a location of interest

    :param: HttpRequest request

    :return: JsonResponse
    '''
    service_factory = WeatherServiceFactory()

    latitude = float(request.GET.get('latitude', ''))
    longitude = float(request.GET.get('longitude', ''))
    services = [
        service_factory.make(service_name)
        for service_name in request.GET.getlist('services[]', [])
    ]
    message = FindAverageTemperatureMessage(latitude, longitude, services)
    handler = FindAverageTemperatureHandler(services)
    average: AverageTemperatureMessage = handler.handle(message)

    return JsonResponse({
        "data": average.average
    })
