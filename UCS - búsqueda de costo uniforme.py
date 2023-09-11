import heapq


def costo_uniforme(graph, start, goal):
    # Inicializar la cola de prioridad con el nodo de inicio y su costo
    priority_queue = [(0, start)]
    # Inicializar el diccionario para rastrear el costo acumulado
    cost_so_far = {node: float('inf') for node in graph}
    cost_so_far[start] = 0
    # Inicializar el diccionario para rastrear el camino
    came_from = {}

    while priority_queue:
        # Obtener el nodo actual y su costo acumulado
        current_cost, current_node = heapq.heappop(priority_queue)

        # Si hemos llegado al nodo objetivo, reconstruir la ruta y devolverla
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from.get(current_node)
            path.reverse()
            return cost_so_far[goal], path

        # Explorar los vecinos del nodo actual
        for neighbor, cost in graph[current_node].items():
            # Calcular el costo acumulado para el vecino
            total_cost = cost_so_far[current_node] + cost
            # Si encontramos un costo menor para el vecino, actualizarlo
            if total_cost < cost_so_far[neighbor]:
                cost_so_far[neighbor] = total_cost
                # Agregar el vecino a la cola de prioridad
                heapq.heappush(priority_queue, (total_cost, neighbor))
                # Registrar el nodo anterior para reconstruir el camino
                came_from[neighbor] = current_node

    # Si no se encontró una ruta al objetivo, devolver None
    return None


# Ejemplo de un grafo ponderado representado como un diccionario de diccionarios
graph = {
    'A': {'B': 14, 'C': 9, 'D': 7},
    'B': {'A': 4, 'C': 2, 'F': 9},
    'C': {'A': 9, 'B': 2, 'D': 10, 'E': 11},
    'D': {'A': 7, 'C': 10, 'E': 15},
    'E': {'C': 11, 'D': 15, 'F': 6},
    'F': {'B': 9, 'D': 6}
}

start_node = 'A'
goal_node = 'F'

result = costo_uniforme(graph, start_node, goal_node)
if result is not None:
    cost, path = result
    print(
        f"El costo de la ruta más corta de {start_node} a {goal_node} es {cost}")
    print(f"La ruta es: {' -> '.join(path)}")
else:
    print(f"No se encontró una ruta de {start_node} a {goal_node}")
