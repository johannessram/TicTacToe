#!/bin/bash/python3.9

"""
This file contains the code that computes the next move of the AI of level Medium.
Medium level tic-tac-toe player means the player knows the rules about the possible moves, and knows how to prevent the oppoonent from winning.
"""

from random import choice
from TicTacToeModel.graph import graph

class AiMediumNextMove():
    def next_move_coordinates(self, player, current_state):
        if player == 'X':
            from TicTacToeModel.graph import opportunity_X
            self.opportunity = opportunity_X
        elif player == 'O':
            from TicTacToeModel.graph import opportunity_O
            self.opportunity = opportunity_O

        key = self.grid_to_key(current_state)
        choice_key = self.choose_next_configuration(key)
        coordinates = self.key_to_grid(choice_key, current_state)
        return coordinates

    def grid_to_key(self, disposition):
        return ''.join([''.join(sub_dis) for sub_dis in disposition])

    # choose the next move depending on the current 'state' of the game
    def choose_next_configuration(self, state):
        further_opportunities = []
        max_opportunities = set()
        [max_opportunities.add(self.opportunity[conf]) for conf in graph[state]]
        max_opportunities = max(max_opportunities)
        further_opportunities = [k for k in graph[state] if self.opportunity[k] == max_opportunities]
        return choice(further_opportunities)

    def key_to_grid(self, key, current_state):
        for i in range(3):
            for j in range(3):
                if current_state[i][j] != key[i*3 + j]:
                    coordinates = {'x': i, 'y': j}
                    return coordinates
