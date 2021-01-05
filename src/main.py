from Dni import Dni

def execute_program_dni():
    
    number_dni = int(input('Escribe el número del DNI para saber que letra tiene:'))
    
    print('*'*50)
    
    dni_object = Dni(number_dni)

    print(f'La letra de este número de DNI es: {dni_object.get_letter()} \n')
    print(f'Este es el DNI con la letra: {dni_object.get_new_dni()} \n')
    
    print('*'*50)
    
    program_reload = input('Quieres saber la letra de otro DNI? 1.Si 2.No')
    
    if program_reload == '1':
        reload_program(True)
    else:
        reload_program(False)
        print('Gracias por usar nuestro programa')
    
    
def reload_program(active=False):
    
    while active == True:
        
        execute_program_dni()

if __name__ == "__main__":
    
    execute_program_dni()