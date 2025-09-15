import Auther
with Auther.request(22, params={"revelio": 1}, allow_redirects=False) as r:
    Auther.passwordColonGetter(r.text, 23)()
