#!/bin/bash/python3.9

import os
from GameException.UnauthorizedMoveError import UnauthorizedMoveError

class Board():
    """
    Board class of the View side
    """
    cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    # singleton
    instance = {'new': None}
    def __init__(self):
        if self.instance['new'] is not None:
            raise UnauthorizedMoveError('Already an instance of Board working elsewhere...')
        self.instance['new'] = self

    def show_board(self):
        print()
        print('\tTIC TAC TOE GAME')
        print()
        print('\t    A   B   C')
        print()
        print(f'\t1   {self.cells[0][0]} | {self.cells[0][1]} | {self.cells[0][2]} ')
        print('\t   ---+---+---')
        print(f'\t2   {self.cells[1][0]} | {self.cells[1][1]} | {self.cells[1][2]} ')              
        print('\t   ---+---+---')
        print(f'\t3   {self.cells[2][0]} | {self.cells[2][1]} | {self.cells[2][2]} ')
        print()

    def clear(self):
        os.system('clear')
        self.instance['new'] = None
        self.__init__()
