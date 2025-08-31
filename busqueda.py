# Programa 1: Busqueda en matriz bidimensional

def buscar_valor(matriz, valor):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == valor:
                return i, j  # Retorna la posicion si encuentra el valor
    return None  # Si no lo encuentra


# Matriz 3x3
matriz = [
    [4, 8, 15],
    [16, 23, 42],
    [1, 2, 3]
]

valor_buscado = 23

posicion = buscar_valor(matriz, valor_buscado)

print("Matriz:")
for fila in matriz:
    print(fila)

if posicion:
    print(f"\n Valor {valor_buscado} encontrado en la posición: fila {posicion[0]}, columna {posicion[1]}")
else:
    print(f"\n Valor {valor_buscado} no encontrado en la matriz")
