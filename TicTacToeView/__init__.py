#!/bin/bash/python3.9

"""This class is a console View for our tic-tac-toe game."""

import os
from TicTacToeView.Board import Board
from TicTacToeView.Pawn import Pawn
from GameException.UnauthorizedMoveError import UnauthorizedMoveError

class TicTacToeView():
    Board = Board
    Pawn = Pawn
    def clear_screen(self):
        os.system('clear')

    def update_board(self, x=3, y=3, player:Pawn=''):
        if self.Board.cells[x][y] != ' ':
            raise UnauthorizedMoveError('Cannot override whether oppenent\'s moves or yours')
        else:
            self.Board.cells[x][y] = player
            self.clear_screen()
            self.Board.instance['new'].show_board()

    def choose_avatar_prompt(self):
        return input('Please choose your Avatar (X/O): ')

    def error_message(self, error_msg=''):
        if error_msg != '':
            print(error_msg)
        else:
            print('Please verify your input')

    def congratulate(self, winner):
        if winner == 'I':
            print('*************SORRY*************')
            print('You lost!!')
        else:
            print('********CONGRATULATIONS********')
            print(f'{winner} won')
        print()
        print()
        print()

    def display(self, message):
        print(message)

    def prompt(self, message=''):
        return input(message)

    def announce_a_draw(self):
        self.Board().clear()
        print('*********It\'s a draw**********')

    def announce_the_end(self, winner):
        PLAYERS_LIST = (Pawn('X'), Pawn('O'))
        if winner in PLAYERS_LIST:
            self.congratulate(winner)
        if winner == 'draw':
            self.announce_a_draw()

