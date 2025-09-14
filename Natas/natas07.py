import Auther
Auther.passwordLineGetter(Auther.request(
    7, params={"page": f"{Auther.authPathOnServer(8)}"}).text, 8)()
