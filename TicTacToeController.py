#!/bin/bash/python3.9


from TicTacToeModel import TicTacToeModel
from TicTacToeView import TicTacToeView
from time import sleep
# add a 1 second timer to simulate the thinking time

class TicTacToeController():
    """
    This is the Controller side of our MVC-based implementation of our game.
    It contains the single class and methods linking TicTacToeView and TicTacToeModel.
    """
    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeView()
        self.view.board = self.view.Board()
        self.letter_coordinates = ('A', 'B', 'C')
        self.players = ('X', 'O')

    def translate_coordinates(self, yx: str):
        y = yx[0].upper()
        y = self.letter_coordinates.index(y)
        x = int(yx[1]) - 1
        x = str(x)
        y = str(y)
        return f'{x} {y}'

    def start(self, message=''):
        self.view.clear_screen()
        self.view.board.show_board()
        if message != '':
            self.view.error_message(error_msg=message)
        game_mode = input('Choose the number of players (1/2)')
        if game_mode == '1':
            self.game_mode = self.one_player
        elif game_mode == '2':
            self.game_mode = self.multi_player
        else:
            self.start('Choose between 1 and 2!!')
        
        self.game_mode()
    
    def multi_player(self):
        print('Player 1 is X, Player 2 is O')

        i = 0
        while not self.model.has_sone_won(output='b'):
            pawn = self.view.Pawn(self.players[i % 2])
            print(f'It\'s {pawn}\'s turn')
            coordinates = input('Enter an empty cell coordinates, for example A1, B3, ... :\t')
            try:
                coordinates = self.translate_coordinates(coordinates)
                coordinates = coordinates.split()
                x, y = list(map(int, coordinates))
                self.model.make_human_move(x, y, pawn)
                self.view.update_board(x, y, pawn)
                i += 1
            except:
                self.view.clear_screen()
                self.view.board.show_board()
                self.view.error_message()

        winner = self.model.has_sone_won(output='p')
        if winner in self.players:
            self.view.congratulate(winner)
        if winner == 'draw':
            self.view.announce_a_draw()

    def choose_avatar(self):
        self.view.choose_avatar_prompt()
        a = input()
        try:
            self.avatar = self.view.Pawn(a)
        except:
            self.view.clear_screen()
            self.view.board.show_board()
            self.view.error_message()
            self.choose_avatar()

    # to be coded
    def one_player(self):
        print('You chose to play against ai')
        self.choose_avatar()
        user = self.avatar
        ai = ['X', 'O']
        ai.remove(user)
        ai = ai[0]

        i = 0
        while not self.model.has_sone_won(output='b'):
            pawn = self.view.Pawn(self.players[i % 2])
            if pawn == user:
                print(f'It\'s your turn')
                coordinates = input('Enter an empty cell coordinates, for example A1, B3, ... :\t')
                try:
                    coordinates = self.translate_coordinates(coordinates)
                    coordinates = coordinates.split()
                    x, y = list(map(int, coordinates))
                    self.model.make_human_move(x, y, pawn)
                    self.view.update_board(x, y, pawn)
                    i += 1
                except:
                    self.view.clear_screen()
                    self.view.board.show_board()
                    self.view.error_message()
            elif pawn == ai:
                    sleep(1)
                    x, y = self.model.make_ai_move(ai)
                    self.model.make_human_move(x, y, pawn)
                    self.view.update_board(x, y, pawn)
                    i += 1

        winner = self.model.has_sone_won()
        if winner == user:
            self.view.congratulate('You')
        elif winner == ai:
            self.view.congratulate('I')
        elif winner == 'draw':
            self.view.announce_a_draw()