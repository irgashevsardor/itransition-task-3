"""The module provides implementation for a computer move in the game"""

import random
from key_generator import secure_token


class Move:
    """Represents a computer move"""

    def __init__(self, moves) -> None:
        self.moves = moves
        self.move = None
        self.__token = secure_token.SecureToken(32).generate()

    def __make_move(self):
        return random.choice(self.moves)

    def get_initial_token(self):
        return self.__token

    def get_move(self):
        return self.__make_move()
