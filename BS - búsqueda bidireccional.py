from collections import deque


def bidirectional_search(graph, start, end):
    if start == end:
        return [start]

    # Inicializar las dos colas de búsqueda
    queue_start = deque([(start, [start])])
    queue_end = deque([(end, [end])])

    # Diccionarios para realizar un seguimiento de los nodos visitados desde ambos extremos
    visited_start = {start: [start]}
    visited_end = {end: [end]}

    while queue_start and queue_end:
        # Realizar una expansión desde el extremo de inicio
        node_start, path_start = queue_start.popleft()
        for neighbor in graph[node_start]:
            if neighbor not in visited_start:
                new_path_start = path_start + [neighbor]
                visited_start[neighbor] = new_path_start
                if neighbor in visited_end:
                    # Se encontró una intersección, concatenar los caminos y devolverlo
                    intersection_node = neighbor
                    path_end = visited_end[intersection_node]
                    return visited_start[intersection_node] + path_end[::-1]
                queue_start.append((neighbor, new_path_start))

        # Realizar una expansión desde el extremo de fin
        node_end, path_end = queue_end.popleft()
        for neighbor in graph[node_end]:
            if neighbor not in visited_end:
                new_path_end = path_end + [neighbor]
                visited_end[neighbor] = new_path_end
                if neighbor in visited_start:
                    # Se encontró una intersección, concatenar los caminos y devolverlo
                    intersection_node = neighbor
                    path_start = visited_start[intersection_node]
                    return path_start + visited_end[intersection_node][::-1]
                queue_end.append((neighbor, new_path_end))

    # Si no se encuentra un camino entre los nodos, devolver None
    return None


graph = {
    '0': ['5', '1', '2', '11'],
    '1': ['0', '3', '7'],
    '2': ['0', '10', '12'],
    '3': ['1', '4', '9'],
    '4': ['3'],
    '5': ['0', '6', '7'],
    '6': ['5'],
    '7': ['1', '5', '8'],
    '8': ['7'],
    '9': ['3'],
    '10': ['2'],
    '11': ['0'],
    '12': ['2'],
}

start = '5'
end = '4'

# graph = {
#     'A': ['B', 'C', 'E'],
#     'B': ['A', 'D', 'E'],
#     'C': ['A', 'F', 'G'],
#     'D': ['B'],
#     'E': ['A', 'B', 'F'],
#     'F': ['C', 'E'],
#     'G': ['C', 'H'],
#     'H': ['G', 'I'],
#     'I': ['H', 'J'],
#     'J': ['I', 'K'],
#     'K': ['J', 'L'],
#     'L': ['K', 'M'],
#     'M': ['L', 'N'],
#     'N': ['M', 'O'],
#     'O': ['N']
# }

# start = 'A'
# end = 'O'

result = bidirectional_search(graph, start, end)
if result:
    print("Camino más corto:", result)
else:
    print("No se encontró un camino entre los nodos.")
