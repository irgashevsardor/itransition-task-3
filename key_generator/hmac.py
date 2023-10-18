"""The module provides implementation to generate HMAC based on cryptographically secure key with digest SHA3-256"""

import hmac
import hashlib


class HMAC:
    """"Represents secure token based HMAC"""

    def __init__(self, secure_key, move) -> None:
        self.key = bytes.fromhex(secure_key)
        self.msg = move

    def generate(self):
        return hmac.new(self.key, self.msg.encode('utf-8'), hashlib.sha3_256).hexdigest()
