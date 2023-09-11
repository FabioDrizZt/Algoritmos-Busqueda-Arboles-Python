from collections import deque

# Definir un grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}


def bfs(grafo, inicio):
    visitados = set()  # Conjunto para realizar un seguimiento de los nodos visitados
    cola = deque()  # Cola para realizar el recorrido BFS
    cola.append(inicio)

    while cola:
        nodo_actual = cola.popleft()  # Sacar el primer nodo de la cola
        if nodo_actual not in visitados:
            print(nodo_actual, end=' ')  # Imprimir el nodo actual
            visitados.add(nodo_actual)  # Marcar el nodo como visitado
            # Agregar los nodos adyacentes no visitados a la cola
            cola.extend(
                adyacente for adyacente in grafo[nodo_actual] if adyacente not in visitados)


# Ejemplo de uso
print("Recorrido BFS a partir de 'A':")
bfs(grafo, 'A')
