'''
core exception module
'''
from core.primitives import TemperatureUnit


class ConversionUnitNotImplemented(Exception):
    '''
    raises when tring can not convert a TemperatureUnit
    '''

    def __init__(self,  temperature_unit: TemperatureUnit):
        super().__init__('Conversion unit %s not implemented' % temperature_unit.unit_name)
