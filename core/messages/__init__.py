'''
This package provide an abstraction layer for the messages (DTO) that the
domain layer of the core needs to achive the Use Case operations
'''
from .find_average_temperature_message import FindAverageTemperatureMessage
from .average_temperature_message import AverageTemperatureMessage
from .temperature_message import TemperatureMessage

__all__ = [
        'FindAverageTemperatureMessage',
        'AverageTemperatureMessage',
        'TemperatureMessage',
]
