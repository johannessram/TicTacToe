#!/bin/bash/python3.9

from random import choice
from TicTacToeModel.graph import graph
from TicTacToeModel.AiMediumNextMove import AiMediumNextMove
from GameException.PlayerError import PlayerError
from GameException.UnauthorizedMoveError import UnauthorizedMoveError


class TicTacToeModel():
    """
    This class contains all primary code for the functionalities of tic-tac-toe including making move, checking who has won, and play against AI.
    Our AI for this version is an algorithm based intelligence which knows opportunities for each possible move and chooses randomly one of next moves leading to the maximum possible score.
    It is not unbeatable due to its way of choosing the next move but this has been done on purpose.
    """
    def __init__(self):
        self.__grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.ai_model = AiMediumNextMove()

    def get_grid(self):
        return self.__grid

    def make_human_move(self, x, y, player):
        player = player.upper()
        if player not in ('X', 'O'):
            raise PlayerError('Player unkown')
        if self.__grid[x][y] != ' ':
            raise MoveError('Cannot override previous moves')
        self.__grid[x][y] = player

    # for testing purpose
    def __str__(self):
        return str(self.__grid)

    def make_ai_move(self, player, level='medium') -> dict:
        current_state = self.get_grid()
        # minimax is in another file
        coordinates = self.ai_model.next_move_coordinates(player, current_state)
        return coordinates
