import binascii
import Auther
# import base64
# base64.encodebytes() -> this will add a newline according to MIME standard? data should be broken into lines of appropriate length
# base64.b64encode() -> this uses binascii.b2a_base64( bytes , newline=False)


def base64decode(s: str):
    return binascii.a2b_base64(s.encode()).decode()


def base64encode(s: str):
    return binascii.b2a_base64(s.encode(), newline=False).decode()


def bin2hex(s: str):
    return s.encode().hex()


def hex2bin(s: str):
    return bytes.fromhex(s).decode()


secret = "3d3d516343746d4d6d6c315669563362"

decoded = base64decode(bytes.fromhex(secret)[::-1].decode())

assert bin2hex(base64encode(decoded)[::-1]) == secret
Auther.passwordIsGetter(
    Auther.request(8, data={"submit": "", "secret": decoded}).text, 9)()
