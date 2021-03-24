def get_category(age):
    # Votre code ici
    if age == 6 or age == 7:
        category="Poussin"
    elif age == 8 or age == 9:
        category="Pupille"
    elif age ==10 or age==11:
        category="Minime"
    elif age >= 12:
        category="Cadet"
    else:
        raise ValueError("mauvaise valeur")
    return category

def run():
    assert get_category(6) == "Poussin"
    assert get_category(7) == "Poussin"
    assert get_category(8) == "Pupille"
    assert get_category(9) == "Pupille"
    assert get_category(10) == "Minime"
    assert get_category(11) == "Minime"
    assert get_category(12) == "Cadet"
    assert get_category(99) == "Cadet"
    
    try:
        get_category(1)
        raise AssertionError()
    except ValueError:
        pass
