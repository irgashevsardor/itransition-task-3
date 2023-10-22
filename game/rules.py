"""The module provides implementation for the game rules to define a winner"""

import math
from typing import List


DRAW = "Draw"
USER = "You Won!"
COMPUTER = "Computer Won!"


class Rule:
    def __init__(self, options: List[str], user_option: str, computer_option: str) -> None:
        if not options:
            raise Exception
        self.options = options
        self.user_option = user_option
        self.computer_option = computer_option

    def __get_user_option_position_index(self):
        return self.options.index(self.user_option)

    def __get_computer_option_position_index(self):
        return self.options.index(self.computer_option)

    def __get_options_halflength(self):
        return math.floor(len(self.options) / 2)

    def define_winner(self):
        user_move = self.__get_user_option_position_index()
        computer_move = self.__get_computer_option_position_index()
        options_halflength = self.__get_options_halflength()

        if user_move == computer_move:
            return DRAW
        elif user_move in range(computer_move, computer_move + options_halflength):
            return USER
        return COMPUTER
