from src.Dni import Dni

"""CASES TEST DNI Objects
"""

def test_get_letter():
    assert  Dni(41098501).get_letter() == 'p'
    assert  Dni(34800381).get_letter() == 'R'
    assert  Dni(54293833).get_letter() == 'x'
    assert  Dni(60338893).get_letter() == 'A'

def test_dni_letter():
    assert Dni(41098501).get_new_dni() == '41098501P'
    assert Dni(34800381).get_new_dni() == '34800381R'
    assert Dni(54293833).get_new_dni() == '54293833X'
    assert Dni(60338893).get_new_dni() == '60338893A'

def test_check_lenght_dni():
    
    assert Dni(41098501).check_lenght_dni() == True
    assert Dni(4109850145).check_lenght_dni() == False
    assert Dni(41098501).check_lenght_dni() == True
    assert Dni(4109850).check_lenght_dni() == False
