'''
service exception module
'''


class WeatherServiceNotConfigured(Exception):
    '''
    exception type for the weather service not implemented
    '''

    def __init__(self, service_implementation: str) -> None:
        super().__init__(f'Service: {service_implementation} NOT confiured properly')
