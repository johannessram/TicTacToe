#!/bin/bash/python3.9

from GameException import GameException

class PlayerError(GameException):
    """
    This exception is raised when an unauthorized action is attempted to be performed
    """
    pass
