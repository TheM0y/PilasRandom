import random

class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.pila = []

    def insertar(self, elemento):
        if len(self.pila) < self.capacidad:
            self.pila.append(elemento)
            self.mostrar_estado(f"Insertar ({elemento})")
        else:
            print("\nLa pila está llena. No se puede insertar.")

    def eliminar(self, elemento):
        if self.pila:
            self.pila.pop()
            self.mostrar_estado(f"Eliminar ({elemento})")
        else:
            print("\nLa pila está vacía. No se puede eliminar.")

    def mostrar_estado(self, operacion):
        print(f"\nOperación: {operacion}")
        print("Estado de la pila:")
        for i in range(len(self.pila)-1, -1, -1):
            print(f"| {self.pila[i]} |")
        print("-----")
        print(f"TOPE = {len(self.pila)}")


# Crear una pila con capacidad para 8 elementos
pila = Pila(8)

# Operaciones disponibles
data = [
    ('insertar', 'X'), ('insertar', 'Y'), ('eliminar', 'Z'), 
    ('eliminar', 'T'), ('eliminar', 'U'), ('insertar', 'V'), 
    ('insertar', 'W'), ('eliminar', 'P'), ('insertar', 'R')
]

# Mezclar las operaciones de forma aleatoria
random.shuffle(data)

for operacion, elemento in data:
    if operacion == 'insertar':
        pila.insertar(elemento)
    elif operacion == 'eliminar':
        pila.eliminar(elemento)
