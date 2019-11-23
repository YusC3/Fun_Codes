"""
gameMake (v1.0) is intended to be a library of classes, useful for 
simple game creation with python. More classes will be added in time.
For further functionality and information see README.txt

"""

class Grid:
    """
    Grid class: A class that allows for a 9 X 9, text 'Grid' object creation.
    Numbers 1 through 9 are designated for each position on the grid.
    """
    def __init__(self):
        """
        Creates underlying data that automatically fills in grid positions.
        Also creates rows, columns and diag (or diagonal) attributes.
        """
        self._data = {1:1, 2:2, 3:3, 4:4, 5:5,
                  6:6, 7:7, 8:8, 9:9} # default data


    def _show(self):
        """
        Prints text grid to screen, with filled default data.
        """
        print(""" 
                {} | {} | {}
              --------------
                {} | {} | {}
              --------------
                {} | {} | {}
            """.format(self._data[1], self._data[2],
            self._data[3], self._data[4], self._data[5],
            self._data[6], self._data[7], self._data[8],
            self._data[9]))


class Player:
    """
    Player class: A class that allows for the creation of Player instances.
    Default slots are given (and intialized to None or 0). __dict__ is also a
    slot that allows for specific slots to be created for a Subclass 
    or specific instance of a Player object.
    """

    __slots__ = '_name', '_score', '__dict__'

    def __init__(self, name=None, score=0):
        """
        Parameters
        ----------
        name : TYPE, optional
            DESCRIPTION: Can enter a specific name. The default is None.
        score : TYPE, optional
            DESCRIPTION: Allows for player scores to be kept.
            The default is 0.

        Returns
        -------
        None.

        """
        self._name = name
        self._score = score


