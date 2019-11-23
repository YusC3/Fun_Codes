"""
Tic Tac Toe (v1.0) - 11/22/2019
Made with custom library gameMake.
"""

# Libraries used
from gameMake import Grid
from gameMake import Player


class _Board(Grid):
    """
    Creation of Tic Tac Toe Board for game play.
    """

    def __init__(self):
        """
        Initializes empty board with columns, rows, and diag attributes.
        """
        Grid.__init__(self)

    def _isPosEmpty(self, position:int):
        """
        Parameters
        ----------
        position : int
            DESCRIPTION: Takes a given board position as an int.

        Returns
        -------
        bool
            DESCRIPTION: Checks if a given position is still default data,
            if yes, this spot is empty.
        """

        if type(self._data[position]) == int:
            return True # position taken
        else:
            return False

    def _place(self, position:int, symbol:str):
        """
        Parameters
        ----------
        position : Same as description above ^^^
        symbol : str
            DESCRIPTION: Passes in a player's given symbol.

        Places a player's symbol on a given position.
        Note: OVERRIDES underlying data!
        """

        self._data[position] = symbol # place symbol


    def _check_vector(self, symbol:str, vector:dict):
        """
        Parameters
        ----------
        symbol : Same as description above ^^^
        vector : dict
            DESCRIPTION: Takes columns, rows, or diag attributes and checks
            each vector accordingly, looking to see if 3 symbols match.

        Returns
        -------
        all_same : bool
            DESCRIPTION: If all symbols are the same for a given vector,
            all_same is True, else False.
        """
        all_same = False
        i = 0
        while all_same == False and i < len(vector.keys()):
            if vector[i].count(symbol) == 3:
                all_same = True
            else:
                i += 1

        return all_same


    def _hasWon(self, symbol:str):
        """
        Parameters
        ----------
        symbol : Same as description above ^^^

        Returns
        -------
        answer : bool
            DESCRIPTION: If after checking all vectors, if 3
            of the given symbol match, answer is True, else False.
        """
        rows = {0: [self._data[1], self._data[2], self._data[3]],
                1: [self._data[4], self._data[5], self._data[6]],
                2: [self._data[7], self._data[8], self._data[9]]}
        columns = {0: [self._data[1], self._data[4], self._data[7]],
                   1: [self._data[2], self._data[5], self._data[8]],
                   2: [self._data[3], self._data[6], self._data[9]]}
        diag = {0: [self._data[1], self._data[5], self._data[9]],
                1: [self._data[3], self._data[5], self._data[7]]}
        answer = False
        if self._check_vector(symbol, columns) == True or\
           self._check_vector(symbol, rows) == True or\
           self._check_vector(symbol, diag) == True:
                              answer = True

        return answer



    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


class _TPlayer(Player):
    """
    Creates Player object for Tic Tac Toe game.
    """
    def __init__(self, symbol=None):
        """
        Initializes with an additional 'symbol' attribute.
        """
        Player.__init__(self)
        # SPECIFIC INSTANCE VARIABLES FOR TIC-TAC-TOE PLAYERS:
        self._symbol = symbol


    # - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
class TicTacToe:
    """
    Main Code for game play and functionality.
    """

    def __init__(self):
        """
        Creates 2 players and assigns a symbol to each.
        """
        self._player1 = _TPlayer()
        self._player2 = _TPlayer()
        self._players = [self._player1, self._player2]

        # Assign players names and symbols
        self._player1._name = "Player 1"
        self._player2._name = "Player 2"
        self._player1._symbol = "X"
        self._player2._symbol = "O"

        # ---------------

        # GREETING MESSAGE
        print("Game Start! \n")
        self._play()


    def _play(self):
        """
        Parameters
        ----------
        players : list
            DESCRIPTION: Takes in a list of players. Used as a
            switich for player turns.

        Returns
        -------
        win : bool
            DESCRIPTION: If a player wins, the code returns
            win as True, else False. To be used in the future
            for score keeping.
        """
        turn = 0
        board = _Board() # creation of board
        game_play = True
        win = False

        while game_play == True:
            if turn < 9: # 9 turns before board is full
                player = self._players[turn%2] # switch for turns
                placed = False
                print("- {}'s turn -".format(player._name))
                print("\n")
                print("Current board: ")
                board._show()
                print("\n")
                pos = input("Enter number position to place symbol: ")

                while placed == False:
                    if pos.isalpha() == True or pos.isnumeric() == False\
                        or pos =="" or pos.isspace() == True:
                        pos = input("Please enter your choice as a NUMBER: ")
                    elif (int(pos) in board._data.keys()) == False:
                        pos = input("Please choose from the given choices: ")
                    elif board._isPosEmpty(int(pos)) == False:
                        pos = input("Position already taken! Choose open position: ")
                    else:
                        pos = int(pos)
                        board._place(pos, player._symbol)
                        placed = True

                if turn >= 4:
                    if board._hasWon(player._symbol) == True:
                        win = True
                        game_play = False
                        print("\n")
                        print("{} has won!".format(player._name))
                        board._show()
                        return win

                turn += 1 # next player's turn
                print("\n")

            elif turn == 9 and win == False:
                print("Draw")
                board._show()
                game_play = False

        return win
