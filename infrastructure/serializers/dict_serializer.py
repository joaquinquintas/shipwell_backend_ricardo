'''
base dict serializer module
'''
from typing import Dict, Any
from abc import ABCMeta, abstractmethod


class DictSerializer:
    '''
    interface to convert any type of object to dict
    '''

    __metaclass__ = ABCMeta

    @abstractmethod
    def to_dict(self, obj: Any) -> Dict:
        return
