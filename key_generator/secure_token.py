"""The module provides implementation to generate cryptographically secure random key"""

import secrets


class SecureToken:
    """Represents cryptographically strong (secure) token"""

    def __init__(self, nbytes) -> None:
        self.nbytes = nbytes

    def generate(self):
        return secrets.token_hex(self.nbytes)
