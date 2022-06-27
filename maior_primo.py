def maior_primo(x):
    divisor = x
    primo = True
    while divisor > 2 and primo:
        divisor = divisor - 1
        resto = x % divisor
        if resto == 0:
            primo = False
            x = x - 1
    return x
    
        
