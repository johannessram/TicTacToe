#!/bin/bash/python3.9

"""
This file contains the definition of a Pawn 
"""

from GameException.PlayerError import PlayerError

class Pawn():
    def __new__(cls, player):
        if player not in ('X', 'O'):
            raise PlayerError('Not allowed to invite a third player!')
        return str(player)
