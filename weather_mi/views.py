'''
django main view for the weather average data
'''
from typing import List
from django.conf import settings
from django.core.exceptions import ValidationError
from django.http.request import HttpRequest
from django.http.response import JsonResponse
from core.messages import FindAverageTemperatureMessage
from core.handlers import FindAverageTemperatureHandler
from core.primitives import AverageTemperature
from .request_adapters import FindAverageTemperatureRequest
from . import validators
from infrastructure.factories import WeatherServiceFactory
from infrastructure.serializers import AverageTemperatureSerializer, ValidationErrorSerializer


def validate_request(request: HttpRequest) -> List:
    errors = []
    rules = [
        validators.validate_latitude,
        validators.validate_longitude,
        validators.validate_services
    ]

    for rule in rules:
        try:
            rule(request)
        except ValidationError as error:
            errors.append(error)

    return errors


def index(request: HttpRequest) -> JsonResponse:
    '''
    resive a HttpRequest object with latitude, longitude, and weather services
    used to retrive the temperature information of a location of interest

    :param: HttpRequest request

    :return: JsonResponse
    '''
    service_factory = WeatherServiceFactory()
    services = {
        service_name: service_factory.make(service_name)
        for service_name in settings.LOAD_WEATHER_SERVICES
    }
    serializer = AverageTemperatureSerializer()
    error_serializer = ValidationErrorSerializer()
    errors = validate_request(request)

    if errors:
        return JsonResponse(
            {'error': error_serializer.to_dict(ValidationError(errors)) },
            status=403
        )

    message = FindAverageTemperatureRequest(request)
    handler = FindAverageTemperatureHandler(services)
    average: AverageTemperature = handler.handle(message)

    return JsonResponse({
        "data": serializer.to_dict(average)
    })
