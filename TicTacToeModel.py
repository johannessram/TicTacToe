class TicTacToeModel():
    """
    This class contains all primary code for the functionalities of tic-tac-toe including making move, checking who has won, and play against AI.
    Our AI for this version is an algorithm based intelligence which knows opportunities for each possible move and chooses randomly one of next moves leading to the maximum possible score.
    It is not unbeatable due to its way of choosing the next move but this has been done on purpose.
    """
    game_status = {'number_of_moves': 0}
    def __init__(self):
        self.__grid = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

    def make_human_move(self, x, y, player):
        if player not in ('X', 'O'):
            raise 'Player unkown'
        if self.__grid[x][y] != ' ':
            raise 'Cannot override previous moves'
        self.__grid[x][y] = player
        self.game_status['number_of_moves'] = self.game_status['number_of_moves'] + 1

    def __has_sone_won(self):
        if self.game_status['number_of_moves'] < 5:
            return ' '
        if self.__grid[0][0] == self.__grid[1][1] == self.__grid[2][2] != ' ':
            return self.__grid[0][0]
        elif self.__grid[0][2] == self.__grid[1][1] == self.__grid[2][0] != ' ':
            return self.__grid[0][2]
        else:
            for i in range(3):
                if self.__grid[i][0] == self.__grid[i][1] == self.__grid[i][2] != ' ':
                    return self.__grid[i][0]
                elif self.__grid[0][i] == self.__grid[1][i] == self.__grid[2][i] != ' ':
                    return self.__grid[0][i]
            if self.game_status['number_of_moves'] >= 9:
                return 'draw'
            return ' '

    # possible choices are p: player name or b: which means boolean output and the __has_sone_won becomes a predicate
    def has_sone_won(self, output='p'):
        op = self.__has_sone_won()
        if output == 'p':
            return op
        elif output == 'b':
            if op in ('X', 'O', 'draw'):
                return True
            else:
                return False

    # for testing purpose
    def __str__(self):
        return str(self.__grid)

    # redefine grid...
    # to avoid giving explicit right to rewrite the
    # def __redefine_state(self):
    #     self.__grid = self



    def make_ai_move(self, player):
        # minimax is in another file
        from graph import graph
        from random import choice

        if player == 'X':
            from graph import opportunity_X
            opportunity = opportunity_X
        elif player == 'O':
            from graph import opportunity_O
            opportunity = opportunity_O

        current_state = self.__grid
        def grid_to_key(disposition):
            return ''.join([''.join(sub_dis) for sub_dis in disposition])

        # choose the next move depending on the current 'state' of the game
        def choose_next(state):
            # further opportunity
            further_opp = []
            max_opp = set()
            [max_opp.add(opportunity[s]) for s in graph[state]]
            max_opp = max(max_opp)
            further_opp = [k for k in graph[state] if opportunity[k] == max_opp]
            return choice(further_opp)

        def tree_depth(further: dict, local_max):
            for st in further_opp:
                # create a new instance of tic_tac_toe model because only there exists an implementation of __has_sone_won
                pass





        def key_to_grid(key):
            for i in range(3):
                for j in range(3):
                    if self.__grid[i][j] != key[i*3 + j]:
                        return [i, j]

        key = grid_to_key(current_state)
        choice_key = choose_next(key)
        coordinates =  key_to_grid(choice_key)
        return coordinates