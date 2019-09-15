'''
core exception module
'''

class NoneLocationProvided(Exception):
    '''
    raises when a no GeoLocation is provided on a operation
    '''

    def __init__(self):
        super().__init__('None location provided, Need use GeoLocation object')
