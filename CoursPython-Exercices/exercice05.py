def is_number_correct(number):
    # Votre code ici
    
    if number >=10 and number <=20:
        result = (True,0)
    elif number <10 :
        ecart= number + 10
        result = (False,ecart)
    else:
        ecart= 20 - number
        result = (False,ecart)
    return result

def run():
    assert is_number_correct(0) == (False, 10)
    assert is_number_correct(10) == (True, 0)
    assert is_number_correct(20) == (True, 0)
    assert is_number_correct(21) == (False, -1)
    assert is_number_correct(50) == (False, -30)
    assert is_number_correct(15) == (True, 0)
