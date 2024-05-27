#Implementar una función para calcular 
#el producto de dos números enteros dados.

def producto(num1, num2): 
    if num1 > 0 or num2 > 0:
        return num1 * num2
    else:
        return 1

num1 = int(input("Ingrese el primer nùmero entero:"))
num2 = int(input("Ingrese el segundo nùmero entrero:"))

resultado = producto(num1, num2)
print("El resultado es:", resultado)