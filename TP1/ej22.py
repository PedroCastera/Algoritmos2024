''''El problema de la mochila Jedi. Suponga que un Jedi está atrapado, pero muy cerca está su mochila que contiene muchos
objetos. Implementar una función recursiva llamada “usar la fuerza” que le permita al Jedi “con
ayuda de la fuerza” realizar las siguientes actividades:
a. sacar los objetos de la mochila de a uno a la vez hasta encontrar un sable de luz o que no
queden más objetos en la mochila;

b. determinar si la mochila contiene un sable de luz y cuantos objetos fueron necesarios sa-
car para encontrarlo;

c. Utilizar un vector para representar la mochila.'''

from random import randint, choice

info = {
    'existe_sable': False,
    'cant_objetos': 0
}

def cargar_mochila():
    mochila = []
    objetos = [
    "Sable de luz",
    "Comunicador",
    "Holocron",
    "Kit de primeros auxilios",
    "Comida y agua",
    "Moneda local", 
    "Antorchas y baterías",
    "Pasaporte galáctico"
    ]

    for i in range(5):
        mochila.append(choice(objetos))
    
    return mochila


def usar_la_fuerza(mochila, index=0):

    if index == len(mochila):
        return info 


    if mochila[index] == "Sable de luz":
        info["existe_sable"] = True
        return info
    
    info["cant_objetos"] += 1

    return usar_la_fuerza(mochila, index + 1)

mochila  = cargar_mochila()
resultados = usar_la_fuerza(mochila)
print("mochila", mochila)
print("resultados", resultados)

