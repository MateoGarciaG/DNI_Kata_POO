from src.Dni import Dni

"""CASES TEST DNI Objects
"""

def test_getLetter():
    assert  Dni(41098501).getLetter() == 'P'
    assert  Dni(34800381).getLetter() == 'R'
    assert  Dni(54293833).getLetter() == 'X'
    assert  Dni(60338893).getLetter() == 'A'

def test_dniLetter():
    assert Dni(41098501).getNewDni() == '41098501P'
    assert Dni(34800381).getNewDni() == '34800381R'
    assert Dni(54293833).getNewDni() == '54293833X'
    assert Dni(60338893).getNewDni() == '60338893A'

def test_checkLenghtNumber():
    
    assert Dni(41098501).checkLenghtNumber() == True
    assert Dni(4109850145).checkLenghtNumber() == False
    assert Dni(41098501).checkLenghtNumber() == True
    assert Dni(4109850).checkLenghtNumber() == False
