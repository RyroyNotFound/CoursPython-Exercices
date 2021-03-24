def factorial(number):
    # Votre code ici
    
    if number == 0:
        return 1
    else:
        F = 1
        for k in range(2,number+1):
            F = F * k
        return F

def run():
    assert factorial(1) == 1
    assert factorial(2) == 2
    assert factorial(3) == 6
    assert factorial(4) == 24
    assert factorial(8) == 40320
    assert factorial(-8) == -40320