import random
import networkx as nx
import matplotlib.pyplot as plt

# Bertingkat

# Fibonacci
# numbers = [3, 2, 5, 7, 12]
# first_diff = [numbers[i-1] for i in range(1, len(numbers))]

# G = nx.DiGraph()
# pos = {}

# for i, num in enumerate(numbers):
#     G.add_node(f'N{i}', label=str(num))
#     pos[f'N{i}'] = (i * 2, 3)

# for idx, i in enumerate(range(1, len(numbers))):
#     if idx == 0:
#         continue
#     G.add_node(f'F{i}', label=f'{numbers[i-2]} + {numbers[i-1]}')
#     pos[f'F{i}'] = (i * 2 - 1, 2)

# for i in range(2, len(numbers)):
#     G.add_edge(f'N{i-2}', f'F{i}')
#     G.add_edge(f'N{i-1}', f'F{i}')
#     G.add_edge(f'F{i}', f'N{i}')

# node_colors = []
# for node in G.nodes():
#     if node.startswith("N"):
#         node_colors.append("lightblue")
#     elif node.startswith("F"):
#         node_colors.append("lightgreen")

# labels = nx.get_node_attributes(G, 'label')
# plt.figure(figsize=(10, 5))
# nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color=node_colors, 
#         edge_color="gray", font_size=10, font_weight="bold")

# edge_labels = nx.get_edge_attributes(G, 'label')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)

# plt.title("Fibonacci Sequence Explanation")
# plt.show()

# Berpola Berulang
# numbers = [5, 7, 6, 12, 14, 13, 26, 28, 27, 54]
# pattern = ['+2', '-1', 'x2']

# G = nx.DiGraph()
# pos = {}

# for i, num in enumerate(numbers):
#     G.add_node(f'N{i}', label=str(num))
#     pos[f'N{i}'] = (i * 2, 3)

# for i in range(len(numbers) - 1):
#     operation = pattern[i % len(pattern)]
#     G.add_node(f'P{i}', label=operation)
#     pos[f'P{i}'] = (i * 2 + 1, 2)

# for i in range(len(numbers) - 1):
#     G.add_edge(f'N{i}', f'P{i}')
#     G.add_edge(f'P{i}', f'N{i+1}')

# node_colors = []
# for node in G.nodes():
#     if node.startswith("N"):
#         node_colors.append("lightblue")
#     elif node.startswith("P"):
#         node_colors.append("lightgreen")

# labels = nx.get_node_attributes(G, 'label')
# plt.figure(figsize=(12, 6))
# nx.draw(G, pos, with_labels=True, labels=labels, node_size=3000, node_color=node_colors, 
#         edge_color="gray", font_size=10, font_weight="bold")
# plt.title("Number Pattern Explanation")
# plt.show()

# larik
numbers = [3, 2, 5, 5, 6, 6, 7, 18, 7, 9, 54, 8]

patterns = ['+2', 'x3','+1', 'x4',]

unique_colors = [
    "#FF9999", "#99FF99", "#9999FF", "#FFCC99", "#FF99FF", "#99FFFF"
]
random.shuffle(unique_colors)
pattern_colors = {pattern: unique_colors[i % len(unique_colors)] for i, pattern in enumerate(patterns)}

pattern_mapping = {op: [] for op in patterns}

for i, num in enumerate(numbers):
    pattern_index = i % len(patterns)
    pattern_mapping[patterns[pattern_index]].append(i)

G = nx.DiGraph()
pos = {}

for i, num in enumerate(numbers):
    G.add_node(f'N{i}', label=str(num))
    pos[f'N{i}'] = (i * 2, 3)

node_colors = []

for pattern, indices in pattern_mapping.items():
    color = pattern_colors[pattern]

    for j in range(len(indices) - 1):
        start, end = indices[j], indices[j + 1]
        op_node = f'Op{start}'
        G.add_node(op_node, label=pattern)
        pos[op_node] = ((start + end) / 2 * 2, 2)
        G.add_edge(f'N{start}', op_node)
        G.add_edge(op_node, f'N{end}')
        node_colors.append(color)

node_colors = ["lightblue" if node.startswith("N") else node_colors.pop(0) for node in G.nodes()]

labels = nx.get_node_attributes(G, 'label')
plt.figure(figsize=(10, 4))
nx.draw(G, pos, with_labels=True, labels=labels, node_size=2000, node_color=node_colors, 
        edge_color="gray", font_size=10, font_weight="bold")
plt.title("Automatically Assigned Patterns with Dynamic Colors")
plt.show()