from src.table_letters import Table_letters
class Dni():
    
    def __init__(self, number):
        self.number = number
    
    def get_letter(self):
        
        if self.check_lenght_number() == True:
            position = self.number % len(Table_letters.keys)
            letter = Table_letters.table.get(position)
            return letter
        else:
            return self.check_lenght_number()
    
    def get_new_dni(self):
        new_dni = str(self.number) + self.get_letter()
        if len(new_dni) == Table_letters.lenght_dni:
            return new_dni
        else:
            return False
    
    def check_lenght_number(self):
        
        if len(str(self.number)) == Table_letters.lenght_number_dni:
            return True
        else:
            return False
        
if __name__ == "__main__":
    assert  Dni(41098501).get_letter() == 'P'