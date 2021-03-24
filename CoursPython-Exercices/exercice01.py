a = 1
b = 2

# Votre code ici
c = a
a = b
b = c


def run():
    assert a == 2
    assert b == 1
