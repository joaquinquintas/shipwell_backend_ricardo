'''
infrastructure exceptions package
'''
from .weather_service_not_implemented import WeatherServiceNotImplemented
from .weather_service_not_configured import WeatherServiceNotConfigured


__all__ = [
    'WeatherServiceNotImplemented',
    'WeatherServiceNotConfigured',
]
