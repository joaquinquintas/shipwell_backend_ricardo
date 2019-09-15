from django.http.request import QueryDict, HttpRequest
from django.core.exceptions import ValidationError


def validate_required(fieldname, querydict: QueryDict):
    '''
    validates that a field is present in the request
    '''
    if fieldname not in querydict:
        raise ValidationError(f'must fill the field: {fieldname}')

def validate_list_not_empty(fieldname, querydict: QueryDict):

    if not querydict.getlist(fieldname):
        raise ValidationError(f'must pass some option on filter: {fieldname}')


def validate_coordinate(fieldname, value):
    '''
    validatates that de field is a float
    '''

    try:
        float(value)
    except ValueError:
        raise ValidationError(f'field {fieldname} -> {value} is not a decimal number')


def validate_latitude(request: HttpRequest):
    '''
    validates a latidude field
    '''
    validate_required('latitude', request.GET)
    validate_coordinate('latitude', request.GET['latitude'])


def validate_longitude(request: HttpRequest):
    '''
    validates a longitude field
    '''
    validate_required('longitude', request.GET)
    validate_coordinate('longitude', request.GET['longitude'])


def validate_services(request: HttpRequest):
    '''
    validates a services filter field
    '''
    validate_required('services[]', request.GET)
    validate_list_not_empty('services[]', request.GET)
