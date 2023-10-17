import sys
import secrets
import hmac
import hashlib


class SecretKey:
    """"Represents cryptographically strong (secure) token"""

    def __init__(self, nbytes) -> None:
        self.nbytes = nbytes

    def generate_secret_key(self):
        return secrets.token_bytes(self.nbytes)


class Computer:
    """Represents an opponent"""

    def __init__(self, secret_key) -> None:
        self.secret_Key = secret_key
        self.moves = sys.argv[1:]
        self.move = None

    def make_move(self):
        self.move = secrets.choice(self.moves)
        return self.move

    def calculate_HMAC(self):
        move = self.make_move()
        return hmac.new(self.secret_Key, move.encode('utf-8'), hashlib.sha3_256).hexdigest()


class Table:
    pass


class GameRule:
    pass


if __name__ == '__main__':
    secret_key = SecretKey(nbytes=32).generate_secret_key()
    computer = Computer(secret_key)
    computer.make_move()
    print(computer.calculate_HMAC())

    # print("Argument List:", str(sys.argv[1:]))

    # print(secret_key.generate_secret_key())
