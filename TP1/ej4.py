#Implementar una función para calcular la potencia
# dado dos números enteros, el primero representa
# la base y segundo el exponente.

def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente == 1:
        return base
    else:
        return base * potencia(base, exponente - 1)
    
base = int(input("Ingrese la base:"))
exponente = int(input("Ingrese el exponente:"))
resultado = potencia(base, exponente)
print("El resultado es:", resultado)
     
