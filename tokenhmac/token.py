import base64
import binascii
import hashlib
from hmac import HMAC, compare_digest
from typing import Callable, Union


class TokenError(Exception):
    pass


class TokenHMAC:
    def __init__(self, key: Union[bytes, str], algorithm: Callable = hashlib.sha256):
        if isinstance(key, str):
            self.key = key.encode("utf-8")

        self.algorithm = algorithm

    def encode(self, payload: bytes) -> bytes:
        return b".".join(
            [
                base64.urlsafe_b64encode(payload),
                base64.urlsafe_b64encode(HMAC(self.key, payload, self.algorithm).digest()),  # type: ignore
            ]
        )

    def decode(self, token: bytes) -> bytes:
        try:
            payload, signature = token.split(b".")
        except ValueError:
            raise TokenError("Invalid token")

        try:
            payload: bytes = base64.urlsafe_b64decode(payload)  # type: ignore
        except (TypeError, binascii.Error):
            raise TokenError("Invalid token")

        try:
            signature: bytes = base64.urlsafe_b64decode(signature)  # type: ignore
        except (TypeError, binascii.Error):
            raise TokenError("Invalid token")

        if not compare_digest(signature, HMAC(self.key, payload, self.algorithm).digest()):  # type: ignore
            raise TokenError("Invalid token")

        return payload
