import Auther


session_cookie = Auther.FOOSessionCookie(21)


def registerSession():
    # data can be sent via POST
    # with Auther.request(21, method="POST", debug=True, experiment=True, data={"submit": "1", "admin": 1}, cookies=session_cookie) as r:
    # params can be sent via GET
    with Auther.request(21, method="GET", debug=True, experiment=True, params={"submit": "1", "admin": 1}, cookies=session_cookie) as r:
        return r.text
    return ""


if __name__ == "__main__":
    registerSession()

    with Auther.request(21, cookies=session_cookie) as r:
        Auther.passwordColonGetter(r.text, 22)()
