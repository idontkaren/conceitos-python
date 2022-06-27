def maior_primo(x):
    divisor = x
    primo = True
    while divisor > 2 and primo:
        divisor = divisor - 1
        resto = divisor % divisor
        if resto == 0:
            primo = False
            x = x - 1
    return x
    


def test_maior_primo1():
    assert maior_primo(30) == 29

def test_maior_primo1():
    assert maior_primo(50) == 49
    
def test_maior_primo2():
    assert maior_primo(100) == 97
