class Nodo:

    def __init__(self, data):
        self.dato = data
        self.izquierda = None
        self.derecha = None

class Arbol_binario:

    def __init__(self):
        self.head = None

    def insertar(self, data):
        nuevo = Nodo(data)

        if self.head is not None:
            if data < self.head.dato:
                if self.head.izquierda is None:
                    self.head.izquierda = nuevo
                else:
                    self.head.izquierda.insertar(data)
            elif data > self.head.dato:
                if self.head.derecha is None:
                    self.head.derecha = nuevo
                else:
                    self.head.derecha.insertar(data)
        else:
            self.head = nuevo

    def Peso_arbol(self):
        return self.contar_nodos(self.head)

    def contar_nodos(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self.contar_nodos(nodo.izquierda) + self.contar_nodos(nodo.derecha)

    def Altura_arbol(self):
        return self.altura(self.head)

    def altura(self, nodo):
        if nodo is None:
            return 0
        else:
            izq_altura = self.altura(nodo.izquierda)
            der_altura = self.altura(nodo.derecha)
            return 1 + max(izq_altura, der_altura)

    def imprimir_arbol(self):
        self.inorden(self.head)

    def inorden(self, nodo):
        if nodo:
            self.inorden(nodo.izquierda)
            print(nodo.dato, end=' ')
            self.inorden(nodo.derecha)

arbol = Arbol_binario()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(2)
arbol.insertar(4)
arbol.insertar(6)
arbol.insertar(8)

print("Peso del árbol:", arbol.Peso_arbol())
print("Altura del árbol:", arbol.Altura_arbol())
print("Árbol inorden:")
arbol.imprimir_arbol()


#Implemetación arboles binarios con Big three
from bigtree import Node


tree = Node("A")


tree.add_node("A/B")
tree.add_node("A/E")


tree.add_node("A/B/C", {"color": "red"})
tree.add_node("A/B/D", {"color": "blue"})


tree.add_node("A/E/F", {"color": "green"})
tree.add_node("A/E/G", {"color": "yellow"})


tree.add_node("A/E/G/H", {"color": "orange"})
tree.add_node("A/E/G/I", {"color":"purple"})

#Códigos ya establecidos anteriormente, solo copie y pegue de mi computadora, por esa razón no hay muchos cambios resgitrados