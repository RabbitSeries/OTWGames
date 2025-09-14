import Auther

# curl
# You can also do this by adding link <a href="http://natas4.natas.labs.overthewire.org">Click me</a> into https://natas5.natas.labs.overthewire.org's unauthorized page
Auther.passwordIsGetter(Auther.request(4, headers={
    "Referer": "http://natas5.natas.labs.overthewire.org/"}).text, 5)()
