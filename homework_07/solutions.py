from collections import deque
import heapq


def has_cycle(graph: dict[int, list[int]]) -> bool:
    # создаем пустой массив для отслеживания посещенных вершин
    # перебираем все вершины графа
    # если вершина еще не посещена
    # запускаем DFS для этой вершины
    visited: set[int] = set()

    for vertex in graph:
        if vertex not in visited and dfs(graph, vertex, None, visited):
            return True

    return False


def dfs(graph: dict[int, list[int]], vertex: int, parent: int | None, visited: set[int]) -> bool:
    # добавляем текущую вершину в множество посещенных
    # перебираем соседей текущей вершины
    # если сосед не является родительской вершиной,
    # чтобы избежать обратного перехода
    # если сосед уже посещен
    # или dfs для соседа вернул true
    # возвращаем true, так как мы нашли цикл
    
    visited.add(vertex)

    for neighbor in graph[vertex]:
        if neighbor != parent:
            if neighbor in visited or dfs(graph, neighbor, vertex, visited):
                return True

    return False

def is_tree(graph: dict[int, list[int]], start: int) -> bool:
    """
    Проверить, является ли граф деревом (связный и без циклов).
    
    Использует BFS с очередью и отслеживанием родителей.
    Дерево имеет ровно n-1 ребро для n вершин, связное и без циклов.
    """
    if start not in graph:
        return False

    visited = []
    queue = deque([start])
    parent: dict[int, int | None] = {start: None}

    while queue:
        vertex = queue.popleft()
        visited.append(vertex)

        for neighbor in graph[vertex]:
            # Если сосед ещё не посещён, добавляем его
            if neighbor not in visited:
                queue.append(neighbor)
                parent[neighbor] = vertex
            else:
                # Если сосед уже посещён, проверяем, не образует ли он цикл
                # (то есть не является ли родителем текущей вершины)
                if parent[vertex] != neighbor:
                    return False

    # Граф является деревом, если связный (все вершины посещены)
    return len(visited) == len(graph)


def dijkstra(graph: dict[int, list[tuple[int, int]]], start: int) -> dict[int, float]:
    """
    Найти кратчайшие расстояния от вершины start до всех вершин графа.

    graph: список смежности вида
    {u: [(v1, w1), (v2, w2), ...]}, где w >= 0.
    """
    if start not in graph:
        return {}

    distances: dict[int, float] = {vertex: float("inf") for vertex in graph}
    distances[start] = 0.0

    # Куча хранит пары (текущее_расстояние, вершина)
    priority_queue: list[tuple[float, int]] = [(0.0, start)]

    while priority_queue:
        current_distance, vertex = heapq.heappop(priority_queue)

        # Пропускаем устаревшие записи из кучи
        if current_distance > distances[vertex]:
            continue

        for neighbor, weight in graph[vertex]:
            if weight < 0:
                raise ValueError("Алгоритм Дейкстры не поддерживает отрицательные веса")

            new_distance = current_distance + weight

            if new_distance < distances[neighbor]:
                distances[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return distances


def is_bipartite(graph: dict[int, list[int]]) -> bool:
    """
    Проверить, является ли неориентированный граф двудольным.

    Идея: пытаемся раскрасить вершины в два цвета так,
    чтобы любые соседние вершины имели разные цвета.
    """
    colors: dict[int, int] = {}

    for start in graph:
        if start in colors:
            continue

        queue = deque([start])
        colors[start] = 0

        while queue:
            vertex = queue.popleft()

            for neighbor in graph[vertex]:
                if neighbor not in colors:
                    colors[neighbor] = 1 - colors[vertex]
                    queue.append(neighbor)
                elif colors[neighbor] == colors[vertex]:
                    return False

    return True



