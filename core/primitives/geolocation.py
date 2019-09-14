'''
Geo Location primitive module
'''


class GeoLocation:
    '''
    Geo location primitive provide a solution for manage location data
    '''

    __latitude: float
    __longitude: float

    def __init__(self, latitude: float, longitude: float):
        self.__latitude = latitude
        self.__longitude = longitude

    @property
    def latitude(self) -> float:
        '''
        latitude of axe the location

        :return: float
        '''
        return self.__latitude

    @property
    def longitude(self) -> float:
        '''
        longitude of axe the location

        :return: float
        '''
        return self.__longitude
