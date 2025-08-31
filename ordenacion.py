# Programa 2: Ordenacion de una fila en la matriz

def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n - i - 1):
            if fila[j] > fila[j + 1]:
                fila[j], fila[j + 1] = fila[j + 1], fila[j]


# Matriz 3x3
matriz = [
    [9, 2, 7],
    [5, 1, 3],
    [8, 6, 4]
]

print("Matriz original:")
for fila in matriz:
    print(fila)

fila_a_ordenar = 2

# Ordenar la fila seleccionada
bubble_sort(matriz[fila_a_ordenar])

print("\nMatriz después de ordenar la fila", fila_a_ordenar, ":")
for fila in matriz:
    print(fila)
