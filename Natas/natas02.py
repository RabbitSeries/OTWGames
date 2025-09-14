import Auther

# print(Auther.request(2).text)
# print(Auther.request(2, "files").text)
# print(Auther.request(2, "files/users.txt").text)
psw = next((line
            for line in Auther.request(2, "files/users.txt").text.splitlines() if line.startswith("natas3:")), None)
if psw:
    Auther.updateAuth(3, psw.split(":")[1])
