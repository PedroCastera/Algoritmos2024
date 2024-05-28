class nodoPila(object):
    '''clase nodo pila'''

    infi, sig = None, None


class Pila(object):
    '''clase pila'''

    def __init__(self):
        '''crear una pila vacia'''

        self.cima = None
        self.tamanio = 0


def apilar(pila, dato):
    '''apila un dato en la cima'''
    nodo = nodoPila()
    nodo.info = dato
    nodo.sig = pila.cima
    pila.cima = nodo
    pila.tamanio += 1

def desapilar(pila):
    '''desapila el elemento de la cima y te lod evuelve'''
    x = pila.cima.info
    pila.cima = pila.cima.sig
    pila.tamanio -= 1
    return x

def pila_vacia(pila):
    '''devuelve true si la pila esta vacia'''
    return pila.cima is None

def en_cima(pila):
    '''devuelve el valor almacenado en la cima de la pila'''
    if pila.cima is not None:
        return pila.cima.info
    else:
        return None
    
def tamanio(pila):
    '''devuelve el numero de elementos en la pila'''
    return pila.tamanio 

def barrido(pila):
    '''muestra el contenido de una pila sin perder datos'''
    paux = Pila()
    while(not pila_vacia(pila)):
        dato = desapilar(pila)
        print(dato)
        apilar(paux, dato)

    while(not pila_vacia(paux)):
        dato = desapilar(paux)
        apilar(pila,dato)

