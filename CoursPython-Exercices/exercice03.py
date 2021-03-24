def is_product_negative(a, b):
    # Votre code ici
    
    if (a < 0 or b < 0):
        result = True
    else:
        result = False
    return result

def run():
    assert is_product_negative(6, 7) == False
    assert is_product_negative(1, 0) == False
    assert is_product_negative(-1, 5) == True
    assert is_product_negative(1, -5) == True
    assert is_product_negative(-1, -5) == False
