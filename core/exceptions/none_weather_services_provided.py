'''
core exception module
'''


class NoneWeatherServicesProvided(Exception):
    '''
    raises when trying to retrive average and none service list are provided
    '''

    def __init__(self):
        super().__init__('None services names was provided')
