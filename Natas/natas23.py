import Auther
with Auther.request(23, data={"passwd": "20iloveyou"}) as r:
    Auther.passwordColonGetter(r.text, 24)()
