# Definición de un grafo como un diccionario de listas de adyacencia
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H', 'I'],
    'E': ['J', 'K'],
    'F': ['L', 'M'],
    'G': ['N', 'O'],
    'H': [],
    'I': [],
    'J': [],
    'K': [],
    'L': [],
    'M': [],
    'N': [],
    'O': [],
}


def busqueda_en_profundidad(graph, start, goal):
    # Inicializar una pila para seguir la ruta
    stack = [start]
    # Inicializar un conjunto para llevar un registro de nodos visitados
    visited = set()

    while stack:
        # Obtener el nodo actual
        current_node = stack.pop()

        # Marcar el nodo como visitado y mostrarlo
        visited.add(current_node)
        print(f"Nodo visitado: {current_node}")

        # Verificar si hemos llegado al nodo objetivo
        if current_node == goal:
            return True

        # Agregar nodos vecinos no visitados a la pila
        for neighbor in graph[current_node]:
            if neighbor not in visited and neighbor not in stack:
                stack.append(neighbor)

    # Si no se encontró el objetivo, devolver False
    return False


start_node = 'A'
goal_node = 'M'

if busqueda_en_profundidad(graph, start_node, goal_node):
    print(f"Se encontró una ruta de {start_node} a {goal_node}")
else:
    print(f"No se encontró una ruta de {start_node} a {goal_node}")
