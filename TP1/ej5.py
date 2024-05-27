#Desarrollar una funciòn que permita, 
#convertir un número romano en un número decimal

#diccionario
rom_dec = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def romano_a_decimal(rom, i=0):
    if not rom:
        return 0
    
    if i == len(rom):
        return 0
    
    current_value = rom_dec[rom[i]]
    next_value = 0
    #validacion para saber si estamos en el ultimo ciclo
    if i != len(rom)-1:
        next_value = rom_dec[rom[i+1]]

    if current_value > next_value:
        return current_value + romano_a_decimal(rom, i+1)
    else:
        return - current_value + romano_a_decimal(rom, i+1)
    


num = romano_a_decimal('MCD')
print(num)
