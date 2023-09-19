#!/bin/bash/python3.9

from GameException import GameException

class UnauthorizedMoveError(GameException):
    """
    This exception is raised when the chosen Avatar is not a valid one
    """
    pass
