#!/bin/bash/python3.9

"""This class is a console View for our tic-tac-toe game."""

import os
class MoveError(Exception):
    pass

class TicTacToeView():
    class Board():
        cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        # singleton
        instance = {'new': None}
        def __init__(self):
            if self.instance['new'] is not None:
                raise MoveError('Already an instance of Board working elsewhere...')
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
        
    def clear_screen(self):
        os.system('clear')

    class Pawn():
        def __new__(cls, player):
            if player not in ('X', 'O'):
                raise MoveError('Not allowed to invite a third player!')
            return str(player)

    def update_board(self, x, y, player: Pawn):
        if self.Board.cells[x][y] != ' ':
            raise MoveError('Cannot override whether oppenent\'s moves or yours')
        else:
            self.Board.cells[x][y] = player
            self.clear_screen()
            self.Board.instance['new'].show_board()

    def choose_avatar_prompt(self):
        print('Please choose your Avatar (X/O): ', end='')

    def error_message(self, error_msg=''):
        if error_msg != '':
            print(error_msg)
        else:
            print('Please verify your input')

    def congratulate(self, winner):
        if winner == 'I':
            print('*************SORRY*************')
            print(f'You lost!!')
        else:
            print('********CONGRATULATIONS********')
            print(f'{winner} won')
        print()
        print()
        print()
    
    def announce_a_draw(self):
        print('*********It\'s a draw**********')