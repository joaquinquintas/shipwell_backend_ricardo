'''
core exeption module
'''

class NoneWeatherServiceDataRetrived(Exception):
    '''
    can not make a average if not has temperature data
    '''
    def __init__(self):
        super().__init__('None weather service data retrived')
