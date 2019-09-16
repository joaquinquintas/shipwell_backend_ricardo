'''
core exception module
'''

class ConversionUnitNotImplemented(Exception):
    '''
    raises when tring can not convert a TemperatureUnit
    '''

    def __init__(self, unit_name: str):
        super().__init__('Conversion unit %s not implemented' % unit_name)
