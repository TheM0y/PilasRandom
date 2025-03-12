import random
import time

def mostrar_pila(pila, tope):
    print("\nEstado actual de la pila:")
    for i in range(len(pila) - 1, -1, -1):
        print(f"[{pila[i]}]" if i == tope - 1 else f" {pila[i]} ")
    print(f"TOPE -> {tope}" if tope > 0 else "PILA VACÍA")

def main():
    CAPACIDAD_MAXIMA = 8
    pila = []
    tope = 0
    
    for _ in range(15):  # Realizar 15 operaciones aleatorias
        operacion = random.choice(["push", "pop"])
        
        if operacion == "push" and tope < CAPACIDAD_MAXIMA:
            elemento = random.randint(1, 99)  # Números aleatorios entre 1 y 99
            pila.append(elemento)
            tope += 1
            print(f"\nPUSH: Se agregó {elemento}")
        elif operacion == "pop" and tope > 0:
            elemento = pila.pop()
            tope -= 1
            print(f"\nPOP: Se eliminó {elemento}")
        
        mostrar_pila(pila, tope)
        time.sleep(1)  # Pequeña pausa para visualizar cambios
    
    print(f"\nLa pila finalizó con {tope} elementos.")

if __name__ == "__main__":
    main()
