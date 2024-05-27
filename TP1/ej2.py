#Implementar una función que calcule la suma de todos los
# números enteros comprendidos
#entre cero y un número entero positivo dado.

def suma_enteros(num):
    if num > 0 :
        return  num + suma_enteros(num-1)
    else:
        return 0

numero = int(input("Ingrese un número para calcular su suma: "))
resultado = suma_enteros(numero) 

print("La suma es de:", resultado)

