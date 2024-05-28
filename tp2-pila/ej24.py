from random import choice
from TDA_Pila  import Pila, apilar, desapilar, pila_vacia, barrido, tamanio

'''Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales se dispone de
su nombre y la cantidad de películas de la saga en la que participó, implementar las funciones
necesarias para resolver las siguientes actividades:

a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando como posi-
ción uno la cima de la pila

b. determinar los personajes que participaron en más de 5 películas de la saga, además indi-
car la cantidad de películas en la que aparece;

c. determinar en cuantas películas participo la Viuda Negra (Black Widow);

d. mostrar todos los personajes cuyos nombre empiezan con C, D y G.
'''

def cargar_pila(personajes):
    pila = Pila()
    for i in range(0, len(personajes)):
        apilar(pila, personajes[i])
    return pila


def respuestas(p_personajes):
    pos = 1
    pos_rocket = 0
    pos_groot = 0
    pelicula_widow = 0
    p_ejb = Pila()
    p_letrac = Pila()
    p_letrad = Pila()
    p_letrag = Pila()
    while not pila_vacia(p_personajes):
        personaje = desapilar(p_personajes)
        #a
        if(personaje["name"] == "Rocket Raccoon"):
            pos_rocket = pos
        if(personaje["name"] == "Groot"):
            pos_groot = pos             


        #b
        if(personaje["movies"] > 5):
            apilar(p_ejb, personaje)

        #c 
        if(personaje["name"] == "Black Widow"):
            pelicula_widow = personaje["movies"] 

        #d
        if personaje["name"].startswith(('C')):
            apilar(p_letrac, personaje)
        if personaje["name"].startswith(('D')):
            apilar(p_letrad, personaje)
        if personaje["name"].startswith(('G')):
            apilar(p_letrag, personaje)
        pos +=1

    print("Ejercicio a:")
    print("Rocket Raccoon se enncuentra en la posiciòn", pos_rocket) 
    print("Groot se enncuentra en la posiciòn", pos_groot)

    print("Ejercicio b: ")
    print("Personajes que tienen más de 5 películas:")
    barrido(p_ejb)

    print("Ejercicio c: ")
    print("Black Widow tiene:",pelicula_widow, "peliculas")

    print("Ejercicio d")
    print("Personajes que empiezan con la letra c:")
    barrido(p_letrac)
    print("Personajes que empiezan con la letra d:")
    barrido(p_letrad)
    print("Personajes que empiezan con la letra g:")
    barrido(p_letrag)


personajes = [
    {"name": "Iron Man", "movies": 10},
    {"name": "Captain America", "movies": 11},
    {"name": "Thor", "movies": 9},
    {"name": "Black Widow", "movies": 9},
    {"name": "Hulk", "movies": 7},
    {"name": "Hawkeye", "movies": 6},
    {"name": "War Machine", "movies": 7},
    {"name": "Ant-Man", "movies": 4},
    {"name": "Spider-Man", "movies": 6},
    {"name": "Black Panther", "movies": 4},
    {"name": "Doctor Strange", "movies": 5},
    {"name": "Captain Marvel", "movies": 3},
    {"name": "Scarlet Witch", "movies": 6},
    {"name": "Vision", "movies": 4},
    {"name": "Falcon", "movies": 6},
    {"name": "Winter Soldier", "movies": 6},
    {"name": "Loki", "movies": 6},
    {"name": "Nick Fury", "movies": 11},
    {"name": "Phil Coulson", "movies": 5},
    {"name": "Star-Lord", "movies": 4},
    {"name": "Gamora", "movies": 4},
    {"name": "Drax", "movies": 4},
    {"name": "Rocket Raccoon", "movies": 5},
    {"name": "Groot", "movies": 5},
    {"name": "Nebula", "movies": 5},
    {"name": "Mantis", "movies": 3},
    {"name": "Yondu", "movies": 2},
    {"name": "Okoye", "movies": 3},
    {"name": "Shuri", "movies": 3},
    {"name": "Valkyrie", "movies": 3}
]

pila_cargada = cargar_pila(personajes)
barrido(pila_cargada)
respuestas(pila_cargada)


