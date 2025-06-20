import uuid 
import matplotlib.pyplot as plt 
import networkx as nx

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None  # Лівий нащадок вузла
        self.right = None  # Правий нащадок вузла
        self.val = key  # Значення, яке зберігається в вузлі
        self.color = color  # Колір вузла, використовується для візуалізації
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):    
    if node is not None:  # Якщо вузол існує
        # Додаємо вузол до графа
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:  # Якщо існує лівий нащадок
            # Додаємо ребро між батьківським і лівим вузлом
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer  # Обчислюємо координати для лівого нащадка
            pos[node.left.id] = (l, y - 1)  # Зберігаємо позицію лівого вузла
            # Рекурсивно додаємо лівий піддерево
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:  # Якщо існує правий нащадок
            # Додаємо ребро між батьківським і правим вузлом
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer  # Обчислюємо координати для правого нащадка
            pos[node.right.id] = (r, y - 1)  # Зберігаємо позицію правого вузла
            # Рекурсивно додаємо правий піддерево
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root):    
    tree = nx.DiGraph()  # Ініціалізуємо орієнтований граф
    pos = {tree_root.id: (0, 0)}  # Початкова позиція для кореневого вузла
    tree = add_edges(tree, tree_root, pos)  # Додаємо всі вузли та ребра в граф
    # Отримуємо кольори для вузлів
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    # Отримуємо підписи для вузлів
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))  # Встановлюємо розмір графіка
    # Малюємо дерево
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.show()  # Виводимо графік

# Створення дерева
root = Node(0)  # Створюємо кореневий вузол
root.left = Node(4)  # Додаємо лівого нащадка до кореневого вузла
root.left.left = Node(5)  # Додаємо лівого нащадка до вузла з ключем 4
root.left.right = Node(10)  # Додаємо правого нащадка до вузла з ключем 4
root.right = Node(1)  # Додаємо правого нащадка до кореневого вузла
root.right.left = Node(3)  # Додаємо лівого нащадка до вузла з ключем 1
# Відображення дерева
draw_tree(root)  # Викликаємо функцію для побудови дерева