import re

import requests


def authPathOnServer(level: int):
    return f'/etc/natas_webpass/natas{level}'


def findAuth(level: int):
    with open("passwords") as f:
        psw = next((psw for psw in f.read().splitlines()
                    if psw.startswith("Level {:>2d}".format(level))), None)
    return (f'natas{level}', psw.split(":")[1].strip()) if psw else None


def request(level: int, route: str = "", method: str = "POST", /, *, data=None, **kwargs):
    return requests.request(method, f'http://natas{level}.natas.labs.overthewire.org/{route}', data=data, auth=('natas0', 'natas0') if level == 0 else findAuth(level),
                            **kwargs
                            )


def updateAuth(updateLevel: int, psw: str):
    if re.compile(r"^\w{32}$").match(psw) is None:
        return
    print(f"Updating level{updateLevel}'s password to {psw}")
    pattern = re.compile(r"^Level\s+(\d+): (\w{32})$")
    with open("passwords") as f:
        auths = {int(m[1]): m[2] for psw in f.read().splitlines()
                 if (m := pattern.match(psw))}
    auths.update({updateLevel: psw})
    authList = sorted([(k, v) for k, v in auths.items()])
    with open("passwords", "w") as f:
        f.writelines(['Level {:>2d}: {}\n'.format(level, psw)
                     for level, psw in authList])


def passwordIsGetter(text: str, level: int):
    psw = next((line for line in text.splitlines()
               if f'The password for natas{level} is' in line), None)
    return (lambda: updateAuth(level, psw.split("is")[1].strip()[0:32]))if psw else None


def passwordLineGetter(text: str, level: int):
    pattern = re.compile(r"^(\w{32})$")
    psw = next((m[1]
                for m in [pattern.match(line) for line in text.splitlines()] if m), None)
    return (lambda: updateAuth(level, psw))if psw else None
