class Nodo():
    def __init__(self,valor,izq=None,der=None):
        self.valor = valor
        self.izq = izq
        self.der = der


a1 = Nodo (25, Nodo (10), Nodo (50, Nodo (40)))

a2 = Nodo(15,Nodo(6, Nodo(4, Nodo(2), Nodo(3))),Nodo(50,Nodo(25),Nodo(104)))

print (a2.der.izq.valor)




#print a1.valor

def in_orden(arbol):
    if arbol == None:
        return []
    return in_orden(arbol.izq) + [arbol.valor] + in_orden(arbol.der)



print (in_orden(a2))
