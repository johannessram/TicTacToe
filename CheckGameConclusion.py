#!/bin/bash/python3.9

from abc import ABC
# from TicTacToeController import TicTacToeController

class CheckGameConclusion(ABC):
    """
    This file contains the checker of whether the play ends or not. And if it ends, it checks who has won.
    """
    
    @staticmethod
    def __check_diagonal_adjacency(grid):
        if grid[0][0] == grid[1][1] == grid[2][2] != ' ':
            return grid[0][0]
        if grid[0][2] == grid[1][1] == grid[2][0] != ' ':
            return grid[0][2]

    @staticmethod
    def __check_othogonal_adjacency(grid):
        for i in range(3):
            if grid[i][0] == grid[i][1] == grid[i][2] != ' ':
                return grid[i][0]
            elif grid[0][i] == grid[1][i] == grid[2][i] != ' ':
                return grid[0][i]

    @staticmethod
    def winner(game):
        ONE_PLAYER_MOVE = 3
        ANOTHER_PLAYER_MOVE = 2
        MAXIMUM_AVAILABLE_CELL = 9
        if game.game_status['number_of_moves'] < (ONE_PLAYER_MOVE + ANOTHER_PLAYER_MOVE):
            return None
        grid = game.model.get_grid()
        if game.game_status['number_of_moves'] > MAXIMUM_AVAILABLE_CELL:
            return 'draw'
        return CheckGameConclusion.__check_diagonal_adjacency(grid) or CheckGameConclusion.__check_othogonal_adjacency(grid)

    @staticmethod
    def game_ends(game, boolean_output=False) -> bool:
        winner = CheckGameConclusion.winner(game)
        if boolean_output:
            return not not winner
        return winner
