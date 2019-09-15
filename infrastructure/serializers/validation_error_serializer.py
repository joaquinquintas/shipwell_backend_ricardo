'''
serializer module of error validations
'''
from typing import Dict
from django.core.exceptions import ValidationError
from .dict_serializer import DictSerializer


class ValidationErrorSerializer(DictSerializer):
    '''
    serialize an error validation
    '''

    def to_dict(self, obj: ValidationError) -> Dict:
        return {
            'messages': obj.messages
        }
