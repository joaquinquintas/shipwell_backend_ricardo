'''
django main view for the weather average data
'''
from django.http.request import HttpRequest
from django.http.response import HttpResponse


def index(request: HttpRequest) -> HttpResponse:
    '''
    resive a HttpRequest object with latitude, longitude, and weather services
    used to retrive the temperature information of a location of interest

    :param: HttpRequest request

    :return: HttpResponse
    '''
    latitude = request.GET.get('latitude', '')
    longitude = request.GET.get('longitude', '')
    services = ', '.join(request.GET.getlist('services[]', []))
    message = f'{latitude}/{longitude} from {services}'
    return HttpResponse(message)
