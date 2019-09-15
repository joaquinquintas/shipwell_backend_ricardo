'''
This package provide an abstraction layer for the messages (DTO) that the
domain layer of the core needs to achive the Use Case operations
'''
from .find_average_temperature_message import FindAverageTemperatureMessage


__all__ = [
    'FindAverageTemperatureMessage',
]
