from fractions import Fraction
import sys
import os

# Agrega la carpeta algebra_lineal al path de Python
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import validaciones as val

def print_matrix(A):
    for fila in A:
        print([str(x) for x in fila])
    print()

def mostrar_solucion(A, num_vars):
    # Funcion para detectar si tiene unica, infinitas o sin solucion
    A = []

def gauss_jordan(A):
    n = len(A)       # número de filas
    m = len(A[0])

    print("\nMatriz inicial:")
    print_matrix(A)

    for i in range(n):
        # Pivote
        # Si el pivote es 0, buscar una fila mas abajo con valor distinto de 0
        if A[i][i] == 0:
            # Va de i+1 (siguiente fila) hasta n (ultima fila) 
            for k in range(i+1, n):
                if A[k][i] != 0:
                    A[i], A[k] = A[k], A[i]  # intercambio de filas
                    print(f"\n\nIntercambio fila {i+1} con fila {k+1}\n")
                    print_matrix(A)
                    break
        # Convertir pivote en 1
        pivote = A[i][i]
        if pivote != 1:
            # Toma la fila i, y divide cada elemento [x] entre el pivote
            # La fila A[i] va a ser igual a una nueva lista
            # en la cual el elemento x se divide entre el pivote y esta operacion
            # se hace para cada elemento x en la fila A[i]
            A[i] = [x / pivote for x in A[i]]
            print(f"\n\nNormalizamos fila {i+1} (dividimos por {pivote})\n")
            print_matrix(A)
        
        # Hacer ceros en la misma columna (arriba y abajo)
        # Donde j representa el numero de filas
        for j in range(n):
            # Si j no es igual al pivote
            if j != i:
                # Obtener el elemento en la fila j y columna i
                elemento = A[j][i]
                # Si aun no es 0
                if elemento != 0:
                    # Creamos el multiplicador que al sumarlo nos haga el elemento 0
                    # Es decir su opuesto
                    mult = elemento * (-1)
                    # Zip nos permite iterar dos listas del mismo tamaño al mismo tiempo
                    # En este caso, la operacion que hacemos es:
                    # Multiplicar el elemento de la fila i (donde esta el pivote) por el multiplicador
                    # Y sumarlo a la fila j (donde esta el elemento que queremos hacer 0)
                    # Con el zip decimos que x es cada elemento de la fila j
                    # Y y es cada elemento de la fila i
                    A[j] = [x + mult * y for x, y in zip(A[j], A[i])]
                    print(f"\n\nFila {j+1} = Fila {j+1} - ({elemento})*Fila {i+1}\n")
                    print_matrix(A)
    return A

def ingresar_matriz():
    print("\n-- Definir Matriz --")
    n = val.validar_entero_positivo("\nNúmero de filas (ecuaciones): ")
    m = val.validar_entero_positivo("Número de columnas (variables): ")

    A = []
    print("\n\n-- Ingreso de Datos --")
    for i in range(n):
        fila = []
        print(f"\n\nIngrese los {m} coeficientes y el término independiente para la fila {i+1}:\n")
        for j in range(m + 1):
            valor = val.validar_numero(f"  Elemento [{i+1},{j+1}]: ")
            fila.append(valor)
        A.append(fila)

    return A

print("--- METODO DE GAUSS-JORDAN ---\n")


A = ingresar_matriz()

resultado = gauss_jordan(A)
print("Matriz final (identidad | soluciones)")
print_matrix(resultado)

print("Soluciones:")
for i in range(len(resultado)):
    print(f"x{i+1} = {resultado[i][-1]}")