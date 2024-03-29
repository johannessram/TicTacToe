#!/bin/bash/python3.9

from time import sleep
from TicTacToeModel import TicTacToeModel
from TicTacToeView import TicTacToeView
from GameException import GameException
from GameException.CellError import CellError
from GameException.PlayerError import PlayerError
from CheckGameConclusion import CheckGameConclusion

NEXT_MOVE = +1
NOT_TERMINATED_ACTION = +0
TIME_TO_SIMULATE_HUMAN_THINKING = 2

class TicTacToeController():
    """
    This is the Controller side of our MVC-based implementation of our game.
    It contains the single class and methods linking TicTacToeView and TicTacToeModel.
    """
    game_status = {'number_of_moves': 0, 'num_of_players': 0, 'X': None, 'O': None}

    def __init__(self):
        self.model = TicTacToeModel()
        self.view = TicTacToeView()
        self.view.board = self.view.board_instance
        self.letter_coordinates = ('A', 'B', 'C')
        self.players = ('X', 'O')

        self.game_status['X'] = self.make_human_move
        self.game_status['O'] = self.make_human_move

    def start(self, message=''):
        self.view.clear_screen()
        self.view.board.show_board()
        self.choose_mode()

        while not CheckGameConclusion.game_ends(self, boolean_output=True):
            number_of_moves = self.game_status['number_of_moves']
            number_of_moves %= len(self.players)
            current_player = self.players[number_of_moves]
            current_player_move = self.game_status[current_player]
            self.view.display(f'It\'s {current_player}\'s turn')
            self.game_status['number_of_moves'] += current_player_move(current_player)
        
        self.announce_the_end()

    def parse_coordinates(self, yx: str):
        try:
            REAJUST_INDEX = - 1
            column = yx[0].upper()
            column = self.letter_coordinates.index(column)
            line = int(yx[1:]) + REAJUST_INDEX

            if line > 3:
                raise CellError('Bad cell coordinates!!')
            return {'x': line, 'y': column}
        except ValueError:
            raise CellError('Bad cell coordinates!!')

    def choose_mode(self, message=''):
        SINGLE_INDEX = 0
        if message != '':
            self.view.error_message(error_msg=message)
        game_mode = self.view.prompt('Choose the number of players (1/2)\t')
        self.game_status['num_of_players'] = game_mode
        if game_mode == '2':
            self.view.display('Player 1 is X, Player 2 is O')
            return None
        if game_mode == '1':
            self.view.display('You chose to play against ai')
            avatar = self.choose_avatar()
            temporary_players_list = list(self.players)
            temporary_players_list.remove(avatar)
            ai_avatar = temporary_players_list[SINGLE_INDEX]
            self.game_status['ai'] = ai_avatar
            self.game_status[ai_avatar] = self.make_ai_move
            return
        else:
            self.choose_mode('Choose between 1 and 2!!')
            return

    def choose_avatar(self):
        avatar = self.view.choose_avatar_prompt()
        try:
            avatar = avatar.upper()
            avatar = self.view.Pawn(avatar)
            return avatar
        except PlayerError:
            self.view.clear_screen()
            self.view.board.show_board()
            self.view.error_message(error_msg='Enter a valid avatar: X or O')
            return self.choose_avatar()

    def make_move(self, x, y, player):
        pawn = self.view.Pawn(player)
        try:
            self.model.make_human_move(x, y, pawn)
            self.view.update_board(x, y, pawn)
            return NEXT_MOVE
        except GameException:
            self.view.clear_screen()
            self.view.board.show_board()
            self.view.error_message(error_msg='Bad coordinates, please enter valid ones')
            return NOT_TERMINATED_ACTION

    def make_human_move(self, player):
        coordinates = self.view.prompt('Enter an empty cell coordinates, for example A1, B3, ... :\t')
        try:
            coordinates = self.parse_coordinates(coordinates)
        except CellError:
            self.view.error_message('Invalid cell coordinates')
            return self.make_human_move(player)
        return self.make_move(**coordinates, player=player)

    def make_ai_move(self, player):
        coordinates = self.model.make_ai_move(player)
        sleep(TIME_TO_SIMULATE_HUMAN_THINKING)
        self.view.display('It\'s your turn')

        return self.make_move(**coordinates, player=player)

    def announce_the_end(self):
        winner = CheckGameConclusion.game_ends(self, boolean_output=False)
        ai = self.game_status.get('ai')

        if winner == 'draw':
            self.view.announce_a_draw()
        elif not ai:
            self.view.announce_the_end(winner)
        elif winner == ai:
            self.view.announce_the_end(winner='I')
        else:
            self.view.announce_the_end(winner='You')
