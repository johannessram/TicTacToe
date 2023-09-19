#!/bin/bash/python3.9

from GameException import GameException

class CellError(GameException):
    """
    This exception is raised when the cell coordinates are not empty, not in the grid, or are erroneous
    """
    pass
