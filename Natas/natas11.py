import base64
from json import JSONEncoder
import urllib.parse
import Auther
level11Cookies = urllib.parse.unquote(Auther.request(11).cookies.get("data"))
xor_encrypted = base64.decodebytes(level11Cookies.encode()).decode()
noshow = {
    "showpassword": "no",
    "bgcolor": "#ffffff"
}
# php json encode has no space
no_show_json = JSONEncoder().encode(noshow).replace(" ", "")
noshow.update({"showpassword": "yes"})
show_json = JSONEncoder().encode(noshow).replace(" ", "")


def bin_xor(b1: str, b2: str):
    return bytes(a ^ b for a, b in zip(b1.encode(), b2.encode()))


def xor_encrypt(raw: str, key: str):
    return "".join(bin_xor(c, key[i % len(key)]).decode() for i, c in enumerate(raw))


def shortest_loop(text: str):
    for loopLen in range(1, len(text)+1):
        s = text[0:loopLen]
        if all(sliced == s[:len(sliced)] for sliced in (text[i:i+len(s)] for i in range(0, len(text), len(s)))):
            return s


key = shortest_loop(xor_encrypt(no_show_json, xor_encrypted))

newCookie = {"data":
             urllib.parse.quote(base64.b64encode(xor_encrypt(show_json, key).encode()))}

Auther.passwordIsGetter(Auther.request(11, cookies=newCookie).text, 12)()
