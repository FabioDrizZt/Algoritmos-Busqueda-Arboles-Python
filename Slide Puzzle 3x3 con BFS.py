from collections import deque

# Definición del estado inicial del problema
# 0 representa el espacio en blanco
estado_inicial = [[1, 6, 2], [7, 4, 3], [5, 8, 0]]

# Definición del estado objetivo (puzzle resuelto)
estado_objetivo = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

# Definición de las operaciones posibles (mover el espacio en blanco)


def acciones(estado):
    acciones_posibles = []
    for i in range(3):
        for j in range(3):
            if estado[i][j] == 0:
                if i > 0:
                    acciones_posibles.append(("Arriba", i, j))
                if i < 2:
                    acciones_posibles.append(("Abajo", i, j))
                if j > 0:
                    acciones_posibles.append(("Izquierda", i, j))
                if j < 2:
                    acciones_posibles.append(("Derecha", i, j))
    return acciones_posibles

# Función para aplicar una acción y obtener un nuevo estado


def aplicar_accion(estado, accion):
    accion_nombre, i, j = accion
    nuevo_estado = [list(fila) for fila in estado]
    if accion_nombre == "Arriba":
        nuevo_estado[i][j], nuevo_estado[i -
                                         1][j] = nuevo_estado[i - 1][j], nuevo_estado[i][j]
    elif accion_nombre == "Abajo":
        nuevo_estado[i][j], nuevo_estado[i +
                                         1][j] = nuevo_estado[i + 1][j], nuevo_estado[i][j]
    elif accion_nombre == "Izquierda":
        nuevo_estado[i][j], nuevo_estado[i][j -
                                            1] = nuevo_estado[i][j - 1], nuevo_estado[i][j]
    elif accion_nombre == "Derecha":
        nuevo_estado[i][j], nuevo_estado[i][j +
                                            1] = nuevo_estado[i][j + 1], nuevo_estado[i][j]
    return nuevo_estado

# Implementación de la búsqueda en árboles (BFS)


def busqueda_arboles(problema):
    # Nodo inicial con estado y ruta
    cola = deque([(problema.estado_inicial, [])])
    visitados = set()  # Conjunto de estados visitados

    while cola:
        estado_actual, ruta = cola.popleft()
        if estado_actual == problema.estado_objetivo:
            return ruta  # Se ha encontrado la solución
        # Convertir la matriz en una tupla hashable
        visitados.add(tuple(map(tuple, estado_actual)))

        for accion in problema.acciones(estado_actual):
            nuevo_estado = problema.aplicar_accion(estado_actual, accion)
            if tuple(map(tuple, nuevo_estado)) not in visitados:
                nueva_ruta = ruta + [accion[0]]
                cola.append((nuevo_estado, nueva_ruta))

    return None  # Fallo, no se encontró una solución

# Clase para representar el problema


class ProblemaSlidePuzzle:
    def __init__(self, estado_inicial, estado_objetivo):
        self.estado_inicial = estado_inicial
        self.estado_objetivo = estado_objetivo

    def acciones(self, estado):
        return acciones(estado)

    def aplicar_accion(self, estado, accion):
        return aplicar_accion(estado, accion)


# Crear el problema y resolverlo
problema = ProblemaSlidePuzzle(estado_inicial, estado_objetivo)
solucion = busqueda_arboles(problema)

if solucion:
    print("Solución encontrada:")
    print(solucion)
else:
    print("No se encontró una solución.")
