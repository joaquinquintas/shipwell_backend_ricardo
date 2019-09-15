from typing import Dict
from core.primitives import AverageTemperature
from .dict_serializer import DictSerializer
from .temperature_serializer import TemperatureSerializer


class AverageTemperatureSerializer(DictSerializer):

    __temperature_serializer: TemperatureSerializer

    def __init__(self):
        self.__temperature_serializer = TemperatureSerializer()

    def to_dict(self, obj: AverageTemperature) -> Dict: 
        return {
            'average': self.__temperature_serializer.to_dict(obj.average),
            'service_data': [
                self.__temperature_serializer.to_dict(temperature)
                for temperature in obj.service_data
            ]
        }
