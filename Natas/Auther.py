from ast import pattern
import re
from typing import Callable

from git import Tree
import requests


def authPathOnServer(level: int):
    return f'/etc/natas_webpass/natas{level}'


def findAuth(level: int):
    with open("passwords") as f:
        psw = next((psw for psw in f.read().splitlines()
                    if psw.startswith("Level {:>2d}".format(level))), None)
    return (f'natas{level}', psw.split(":")[1].strip()) if psw else None


def target(level: int):
    return f'http://natas{level}.natas.labs.overthewire.org/'


def experiment_target(level: int):
    return f'http://natas{level}-experimenter.natas.labs.overthewire.org/'


def request(level: int, route: str = "", method: str = "POST", *,
            data=None, cookies=None, debug: bool = False, params: dict = None, experiment: bool = False,
            headers=None,
            allow_redirects=True,
            **kwargs):
    if debug:
        params = {**(params if params else {}), "debug": 1}
    url = (experiment_target(level) if experiment else target(level))+route
    return requests.request(method,
                            url,
                            data=data,
                            params=params,
                            auth=('natas0', 'natas0') if level == 0 else findAuth(
                                level),
                            cookies=cookies,
                            headers=headers,
                            allow_redirects=allow_redirects,
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


def getter(text: str, handle: Callable[[str], bool]):
    return next((line for line in text.splitlines() if handle(line)), None)


def passwordIsGetter(text: str, level: int):
    psw = getter(
        text, lambda line: f'The password for natas{level} is' in line)
    return (lambda: updateAuth(level, psw.split("is")[1].strip()[0:32])) if psw else None


def passwordLineGetter(text: str, level: int):
    pattern = re.compile(r"^(\w{32})$")
    psw = getter(text, lambda line: pattern.match(line) is not None)
    return (lambda: updateAuth(level, psw[0:32])) if psw else None


def passwordColonGetter(text: str, level: int):
    pattern = re.compile(r'Password: (\w{32})')
    psw = getter(text, lambda line: pattern.search(line) is not None)
    return (lambda: updateAuth(level, psw.split("Password:")[1].strip()[0:32])) if psw else None


def FOOSessionCookie(level: int):
    return {"PHPSESSID": f"LEVEL{level}RABBITFOO"}
