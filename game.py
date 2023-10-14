import sys
import secrets


class SecretKey:
    """"Represents cryptographically strong (secure) random secret token"""

    def __init__(self, nbytes):
        self.nbytes = nbytes

    def generate_secret_key(self):
        return secrets.token_hex(self.nbytes)


class Table:
    pass


class GameRule:
    pass


class HMAC:
    pass


if __name__ == '__main__':
    print("Argument List:", str(sys.argv))
    secret_key = SecretKey(nbytes=32)
    print(secret_key.generate_secret_key())
