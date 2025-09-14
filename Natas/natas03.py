import Auther

# print(Auther.request(3).text)
route = next((line
              for line in Auther.request(3, "robots.txt").text.splitlines() if line.startswith("Disallow:")), None)
if route:
    route = route.split(":")[1].strip()
    # print(Auther.request(3, route, "GET").text)
    Auther.updateAuth(
        4, Auther.request(3, route+"/users.txt", "GET").text.split(":")[1].strip())
