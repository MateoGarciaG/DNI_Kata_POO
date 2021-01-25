from src.table_letters import Table_letters
class Dni():
    
    def __init__(self, number):
        self.number = number
    
    def getLetter(self):
        
        if self.checkLenghtNumber() == True:
            position = self.number % len(Table_letters.keys)
            letter = Table_letters.table.get(position)
            return letter
        else:
            return self.check_lenght_number()
    
    def getNewDni(self):
        new_dni = str(self.number) + self.getLetter()
        if len(new_dni) == Table_letters.lenghtDni:
            return new_dni
        else:
            return False
    
    def checkLenghtNumber(self):
        
        if len(str(self.number)) == Table_letters.lenghtNumberDni:
            return True
        else:
            return False
