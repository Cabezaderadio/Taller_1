class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.hijos = []

class ArbolEnlazado:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor, padre=None):
        nuevo_nodo = Nodo(valor)

        if padre is None:
            if self.raiz is None:
                self.raiz = nuevo_nodo
            else:
                print("Error: El árbol ya tiene una raíz.")
        else:
            padre.hijos.append(nuevo_nodo)

    def peso_arbol(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        peso = 1
        for hijo in nodo.hijos:
            peso += self.peso_arbol(hijo)
        return peso

    def orden_arbol(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        for hijo in nodo.hijos:
            self.orden_arbol(hijo)
            print(hijo.valor, end=' ')
        if nodo == self.raiz:
            print()

    def altura_arbol(self, nodo=None):
        if nodo is None:
            nodo = self.raiz
        if not nodo.hijos:
            return 1
        alturas_hijos = [self.altura_arbol(hijo) for hijo in nodo.hijos]
        return 1 + max(alturas_hijos)

arbol = ArbolEnlazado()

while True:
    opcion = input("Ingrese un nodo (o 'fin' para terminar): ")
    if opcion.lower() == 'fin':
        break
    arbol.insertar(opcion)

print("Peso del árbol:", arbol.peso_arbol())
print("Orden del árbol:")
arbol.orden_arbol()
print("Altura del árbol:", arbol.altura_arbol())


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