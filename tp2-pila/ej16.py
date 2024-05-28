from TDA_Pila  import Pila, apilar, desapilar, pila_vacia, barrido, tamanio
from random import choice

'''Se tienen dos pilas con personajes de Star Wars, en una los del episodio V de “The empire
strikes back” y la otra los del episodio VII “The force awakens”. 
Desarrollar un algoritmo que permita obtener la intersección de ambas pilas, es decir los personajes que aparecen en am-
bos episodios.'''


def cargar_pila(personajes):
    pila = Pila()
    for i in range(5):
        apilar(pila, choice(personajes))
    return pila

def intersecciones(ep5, ep7):
    paux = Pila()
    pintersecciones = Pila()
    while not pila_vacia(ep5):
        x = desapilar(ep5)
        while not pila_vacia(ep7):
            y = desapilar(ep7)
            apilar(paux,y)
            if (x == y):
                apilar(pintersecciones, x)
        while not pila_vacia(paux):
            z = desapilar(paux)
            apilar(ep7, z)
    return pintersecciones          

personaje5 = [
    "Luke Skywalker",
    "Han Solo",
    "Leia Organa",
    "Darth Vader",
    "Yoda",
    "Lando Calrissian",
    "Chewbacca",
    "C-3PO",
    ]
personaje7 = [
    "Rey",
    "Finn",
    "Kylo Ren",
    "Poe Dameron",
    "Han Solo",
    "Leia Organa",
    "Luke Skywalker",
    "Chewbacca",
    ]
ep5 = cargar_pila(personaje5)
ep7 = cargar_pila(personaje7)

p_resultados = intersecciones(ep5, ep7)

if pila_vacia(p_resultados):
    print("No hay intershecciones")
else:
    print("Los personajes que se repitieron son: ") 
    barrido(p_resultados)
    print("Cantidad de repeticiones: ")
    print (tamanio(p_resultados))
