import heapq
from typing import Dict, List, Optional, Tuple

def dijkstra(
    graph: Dict[str, List[Tuple[str, float]]], start: str
) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    # Ініціалізуємо відстані як нескінченність для всіх вершин
    distances = {vertex: float("inf") for vertex in graph}
    distances[start] = 0  # Відстань до стартової вершини дорівнює 0
    previous_nodes = {vertex: None for vertex in graph}  # Для відновлення шляху
    # Пріоритетна черга (бінарна купа)
    priority_queue = [(0, start)]  # (відстань, вершина)
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        # Перевіряємо, чи цей шлях не гірший за відомий найкоротший
        if current_distance > distances[current_vertex]:
            continue
        # Проходимо по всіх сусідах поточної вершини
        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight
            # Якщо знайдено коротший шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    return distances, previous_nodes

def reconstruct_path(
    previous_nodes: Dict[str, Optional[str]], start: str, end: str
) -> List[str]:
    path = []
    current = end
    while current is not None:
        path.append(current)
        current = previous_nodes[current]
    path.reverse()
    return path if path[0] == start else []

# Створення графу
graph = {
    "A": [("B", 7), ("C", 9), ("F", 14)],
    "B": [("A", 7), ("C", 10), ("D", 15)],
    "C": [("A", 9), ("B", 10), ("D", 11), ("F", 2)],
    "D": [("B", 15), ("C", 11), ("E", 6)],
    "E": [("D", 6), ("F", 9)],
    "F": [("A", 14), ("C", 2), ("E", 9)],
}
# Виклик функції
start_node = "A"
distances, previous_nodes = dijkstra(graph, start_node)
# Виведення результатів
for vertex, distance in distances.items():
    print(f"Відстань від '{start_node}' до '{vertex}': {distance}")
# Відновлення та друк найкоротшого шляху
end_node = "E"
path = reconstruct_path(previous_nodes, start_node, end_node)
print(f"Найкоротший шлях від '{start_node}' до '{end_node}': {' -> '.join(path)}")