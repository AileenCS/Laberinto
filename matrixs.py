#Algoritmo de ruta de mayor y menor costo en matrix 13x13

def encontrar_posicion(matrix, objetivo):
    for fila, fila_valores in enumerate(matrix):
        for columna, valor in enumerate(fila_valores):
            if valor == objetivo:
                return (fila, columna)
    return None


# Definimos la matriz con 'I' como 9 y 'F' como -9
matrix = [
    [-3, -3,  2, -3, 3, -2, -2, 1, 2, 0, 2, 0, 1],
    [2, 3, 9, -1, -1, 3, 2, 0, -3, -3, 2, 2, 1],
    [1, -3, -3, 2, 3, 1, 3, 3, 2, -1, -2, 3, 0],
    [0, 0, 3, 0, 3, -3, -2, -3, 0, 2, 2, 1, 1],
    [2, -1, -1, -3, 3, 3, 0, -3, 1, -2, 2, 0, 1], 
    [0, 3, -1, 1, -1, -2, 2, -2, 2, -1, -2, -3, 0],
    [3, 3, -3, -2, 3, -3, -1, -3, 3, -2, 2, -2, -1],
    [-2, -2, 1, 0, -1, 0, 3, 0, 0, -2, 2, -3, -1],
    [-3, 3, 0, -1, 0, 3, 0, 0, -2, 2, -3, -1, 0],
    [-3, 3, 0, -1, -3, 1, 2, -3, 2, -3, 0, 2, -2],
    [-3, -3, -3, 3, -2, 0, -2, -3, 1, 0, 1, -1, -2],
    [-1, 0, 1, 2, 1, 0, -9, 0, -3, 3, 3, 0, 3],
    [1, -3, 1, 0, 1, 2, 3, 1, -2, 3, 3, 0, 3]
]
# Ejemplo simplificado de matriz
# matrix = [
#     [9, 2, 3],
#     [4, 5, 6],
#     [7, 8, -9]
# ]


inicio = encontrar_posicion(matrix, 9)
fin = encontrar_posicion(matrix, -9)



def calcular_costos_y_rutas(matrix, inicio, fin):
    filas, columnas = len(matrix), len(matrix[0])
    
    # Inicializar matrices de costos
    costo_minimo = [[float('inf')] * columnas for _ in range(filas)]
    costo_maximo = [[float('-inf')] * columnas for _ in range(filas)]
    
    # Inicializar matrices de rutas
    ruta_minima = [[None] * columnas for _ in range(filas)]
    ruta_maxima = [[None] * columnas for _ in range(filas)]
    
    # Costos y rutas de la posición inicial
    costo_minimo[inicio[0]][inicio[1]] = matrix[inicio[0]][inicio[1]]
    costo_maximo[inicio[0]][inicio[1]] = matrix[inicio[0]][inicio[1]]
    
    ruta_minima[inicio[0]][inicio[1]] = [(inicio[0], inicio[1])]
    ruta_maxima[inicio[0]][inicio[1]] = [(inicio[0], inicio[1])]
    
    for x in range(filas):
        for y in range(columnas):
            if x > 0:
                if costo_minimo[x-1][y] + matrix[x][y] < costo_minimo[x][y]:
                    costo_minimo[x][y] = costo_minimo[x-1][y] + matrix[x][y]
                    ruta_minima[x][y] = ruta_minima[x-1][y] + [(x, y)]
                    
                if costo_maximo[x-1][y] + matrix[x][y] > costo_maximo[x][y]:
                    costo_maximo[x][y] = costo_maximo[x-1][y] + matrix[x][y]
                    ruta_maxima[x][y] = ruta_maxima[x-1][y] + [(x, y)]
                    
            if y > 0:
                if costo_minimo[x][y-1] + matrix[x][y] < costo_minimo[x][y]:
                    costo_minimo[x][y] = costo_minimo[x][y-1] + matrix[x][y]
                    ruta_minima[x][y] = ruta_minima[x][y-1] + [(x, y)]
                    
                if costo_maximo[x][y-1] + matrix[x][y] > costo_maximo[x][y]:
                    costo_maximo[x][y] = costo_maximo[x][y-1] + matrix[x][y]
                    ruta_maxima[x][y] = ruta_maxima[x][y-1] + [(x, y)]
    
    return costo_minimo[fin[0]][fin[1]], ruta_minima[fin[0]][fin[1]], costo_maximo[fin[0]][fin[1]], ruta_maxima[fin[0]][fin[1]]


# Ejecutar la simulación y calcular costos y rutas
try:
    costo_minimo, ruta_minima, costo_maximo, ruta_maxima = calcular_costos_y_rutas(matrix, inicio, fin)
    
    print(f"Costo mínimo: {costo_minimo}")
    print(f"Ruta mínima: {ruta_minima}")
    print(f"Costo máximo: {costo_maximo}")
    print(f"Ruta máxima: {ruta_maxima}")

except ValueError as e:
    print(e)
