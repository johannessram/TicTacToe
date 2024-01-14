#!/bin/bash/python3.9

"""
This file contains the code that computes the next move of the AI of level Medium.
Medium level tic-tac-toe player means the player knows the rules about the possible moves, and knows how to prevent the oppoonent from winning.
"""

from random import choice
from time import sleep
from TicTacToeModel.graph import graph, opportunity_O, opportunity_X

DRAW_OPPORTUNITY = 0

class AiMediumNextMove():
    def next_move_coordinates(self, player, current_state):
        if player == 'X':
            self.opportunity = opportunity_X
        elif player == 'O':
            self.opportunity = opportunity_O

        key = self.grid_to_key(current_state)
        key_new_state = self.choose_next_configuration(key)
        coordinates = self.key_to_grid(key_new_state, current_state)
        return coordinates

    def grid_to_key(self, disposition):
        return ''.join([''.join(sub_dis) for sub_dis in disposition])

    # choose the next move depending on the current 'state' of the game
    def choose_next_configuration(self, state):
        immediate_win = self.immediate_win(state)
        if immediate_win:
            return immediate_win

        further_opportunities = []
        max_opportunities = set()
        [max_opportunities.add(self.opportunity[conf]) for conf in graph[state]]
        # add 0 to max to show that in the case we reach a leaf, meaning opportunity set is empty
        max_opportunities.add(DRAW_OPPORTUNITY)
        max_opportunities = max(max_opportunities)
        further_opportunities = [k for k in graph[state] if self.opportunity[k] == max_opportunities]
        return choice(further_opportunities)

    def immediate_win(self, state):
        winning_child = None
        children = set(graph[state])
        for child in children:
            grandchildren = graph[child]
            for grandchild in grandchildren:
                if grandchild not in self.opportunity and self.opportunity[child] == 100 :
                    winning_child = child
                    return winning_child


    def key_to_grid(self, key_new_state, current_state):
        for i in range(3):
            for j in range(3):
                if current_state[i][j] != key_new_state[i*3 + j]:
                    coordinates = {'x': i, 'y': j}
                    return coordinates
