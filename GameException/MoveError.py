#!/bin/bash/python3.9

from GameException import GameException

class MoveError(GameException):
    """
    This exception is raised when an unauthorized action is attempted to be performed
    """
    pass
