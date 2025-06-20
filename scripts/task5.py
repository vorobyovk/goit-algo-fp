import uuid
from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):    
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2**layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2**layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, title=""):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)
    colors = [node[1]["color"] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]["label"] for node in tree.nodes(data=True)}
    plt.figure(figsize=(8, 5))
    nx.draw(
        tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors
    )
    plt.title(title)
    plt.show()

def bfs_visual(tree_root):    
    queue = deque([tree_root])
    color_step = 255 // (tree_size(tree_root) - 1) if tree_size(tree_root) > 1 else 0
    step = 0
    while queue:
        node = queue.popleft()
        node.color = f"#{step:02x}{step:02x}{255-step:02x}"
        step += color_step
        draw_tree(tree_root, title=f"BFS Step with {node.val}")
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs_visual(tree_root):    
    stack = [tree_root]
    color_step = 255 // (tree_size(tree_root) - 1) if tree_size(tree_root) > 1 else 0
    step = 0
    while stack:
        node = stack.pop()
        node.color = f"#{step:02x}{step:02x}{255-step:02x}"
        step += color_step
        draw_tree(tree_root, title=f"DFS Step with {node.val}")
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

def tree_size(node):    
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)

# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)
# Візуалізація обходу в ширину (BFS)
bfs_visual(root)
# Візуалізація обходу в глибину (DFS)
dfs_visual(root)