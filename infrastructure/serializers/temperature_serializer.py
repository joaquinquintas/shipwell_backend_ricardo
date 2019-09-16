from typing import Dict
from .dict_serializer import  DictSerializer
from core.primitives import Temperature


class TemperatureSerializer(DictSerializer):

    def to_dict(self, obj: Temperature) -> Dict:
        value = f'{obj.value:.1f}'

        return {
            'provider_name': obj.provider_name,
            'value': float(value),
            'unit': obj.unit.unit_name,
        }
