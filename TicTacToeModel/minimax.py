#!/bin/bash/python3.9


"""
This file contains the algorithm used to get the data in graph.py. Algorithms here consist 
of exploring all combination following some rules (p_s_turn), Minimax algorithm used to kn-
ow the best next move. Data structures here are graph and built-in list, dictionary used to
implement a variant of hash table.
"""

grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
FIRST_KEY = ''.join(''.join(grid[i]) for i in range(3))
graph = {}
opportunity = {}

# MINIMAX
# we are trying first to create a graph in an adjacency list way
def p_s_turn(player, graph, grid_key):
    """we are trying to create each possible configuration, after each possible move consi-
    dering that when we call this func for the fist time, player is X, because he always b-
    egins
    """
    if grid_key not in graph:
        graph[grid_key] = []
    for i in range(9):
        if grid_key[i] == ' ':
            temp_key = grid_key
            temp_key = list(temp_key)
            temp_key[i] = player
            temp_key = ''.join(temp_key)

            if temp_key not in graph[grid_key]:
                graph[grid_key].append(temp_key)
            if player == 'X':
                p_s_turn('O', graph, temp_key)
            elif player == 'O':
                p_s_turn('X', graph, temp_key)

def round_count(key):
    round_count = 0
    for l in key:
        if l in ('X', 'O'):
            round_count += 1
    return round_count

def _f_has_sone_won(key):
    if round_count(key) < 5:
        return ' '
    if key[0] == key[4] == key[8] != ' ':
        return key[0]
    if key[2] == key[4] == key[6] != ' ':
        return key[2]
    else:
        for i in range(3):
            if key[i] == key[i + 3] == key[i + 6] != ' ':
                return key[i]
            elif key[i*3] == key[i*3 + 1] == key[i*3 + 2] != ' ':
                return key[i*3]
        if round_count(key) == 9:
            return 'draw'
        return ' '

def f_has_sone_won(key, output='p'):
    """f stands for flattened,
    like the grid has been flattened to become 1*9 instead of 3*3
    """
    op = _f_has_sone_won(key)
    if output == 'p':
        return op
    elif output == 'b':
        if op in ('X', 'O'):
            return True
        else:
            return False


def find_next_traversal(turn, me, opportunity, graph, current_state):
    """ this function is about creating the reward graph of the minimax:
    for each level of the tree,
    if it is my turn, i will definitely maximize my score
    elif it is your, you may try to maximize your score, therefore minimize mine
    """
    if graph[current_state] == []:
        opponent = ['X', 'O']
        opponent.remove(me)
        opponent = opponent[0]

        p = (opponent, 'draw', me)
        s = (-10, 0, 100)
        winner = f_has_sone_won(current_state)
        score = s[p.index(winner)]
        opportunity[current_state] = score
        return score

    who_wins = f_has_sone_won(current_state)
    if who_wins  == me:
        opportunity[current_state] = 100
        return opportunity[current_state]
    elif who_wins != me and who_wins != ' ' and who_wins != 'draw':
        opportunity[current_state] = -10
        return opportunity[current_state]
    elif who_wins == 'draw':
        opportunity[current_state] = 0
        return opportunity[current_state]
    elif who_wins == ' ' and current_state not in opportunity:
        # search for its opportunity and recording it into opportunity dictionary
        recording = set()
        next_turn = ['X', 'O']
        next_turn.remove(turn)
        next_turn = next_turn[0]
        for next_case in graph[current_state]:
            recording.add(find_next_traversal(next_turn, me, opportunity, graph, next_case))

        # max if it is my turn
        if turn == me:
            opportunity[current_state] = max(recording)
            return opportunity[current_state]

        # min if it is my opponents
        elif turn != me:
            opportunity[current_state] = min(recording)
            return opportunity[current_state]

    # in case it has already been cached
    elif who_wins == ' ' and current_state in opportunity:
        return opportunity[current_state]
