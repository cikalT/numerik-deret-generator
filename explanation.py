import random
import networkx as nx
import streamlit as st
import matplotlib.pyplot as plt

def render_explanation(plt_in, G, pos, labels, node_colors):
    fig, ax = plt_in.subplots(figsize=(10, 4.8))

    ax.set_facecolor("none")
    fig.patch.set_alpha(0)

    nx.draw(
        G, pos, ax=ax, with_labels=True, labels=labels,
        node_size=2000, node_color=node_colors, edge_color="gray",
        font_size=10, font_weight="bold"
    )

    st.pyplot(fig)

def bertingkat(number_list, answer_count):
    first_diff = [number_list[i] - number_list[i-1] for i in range(1, len(number_list))]
    second_diff = [first_diff[i] - first_diff[i-1] for i in range(1, len(first_diff))]

    G = nx.DiGraph()

    pos = {}
    for i, num in enumerate(number_list):
        G.add_node(f'N{i}', label=str(num))
        pos[f'N{i}'] = (i * 2, 3)

    for i, diff in enumerate(first_diff):
        G.add_node(f'F{i}', label=f'+{diff}')
        pos[f'F{i}'] = (i * 2 + 1, 2)

    for i, diff in enumerate(second_diff):
        G.add_node(f'S{i}', label=f'+{diff}')
        pos[f'S{i}'] = (i * 2 + 1.5, 1)

    for i in range(len(number_list) - 1):
        G.add_edge(f'N{i}', f'N{i+1}')
        G.add_edge(f'N{i}', f'F{i}')
        G.add_edge(f'F{i}', f'N{i+1}')
        
    for i in range(len(first_diff) - 1):
        G.add_edge(f'F{i}', f'S{i}')
        G.add_edge(f'S{i}', f'F{i+1}')
        
    node_colors = []
    num_nodes = len(number_list)
    for idx, node in enumerate(G.nodes()):
        if node.startswith("N"):
            if (idx >= num_nodes-answer_count):
                node_colors.append("lightgreen")
            else:
                node_colors.append("lightblue")
        elif node.startswith("F"):
            node_colors.append("peachpuff")
        elif node.startswith("S"):
            node_colors.append("lightcoral")

    labels = nx.get_node_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(10, 6))
    # nx.draw(G, pos, ax=ax, with_labels=True, labels=labels, node_color=node_colors, node_size=2000, edge_color="gray", font_size=10, font_weight="bold")
    # st.pyplot(fig)
    render_explanation(plt, G, pos, labels, node_colors)

def berpola_berulang(number_list, answer_count, patterns):
    G = nx.DiGraph()
    pos = {}

    for i, num in enumerate(number_list):
        G.add_node(f'N{i}', label=str(num))
        pos[f'N{i}'] = (i * 2, 3)

    for i in range(len(number_list) - 1):
        operation = patterns[i % len(patterns)]
        G.add_node(f'P{i}', label=operation)
        pos[f'P{i}'] = (i * 2 + 1, 2)

    for i in range(len(number_list) - 1):
        G.add_edge(f'N{i}', f'P{i}')
        G.add_edge(f'P{i}', f'N{i+1}')

    node_colors = []
    num_nodes = len(number_list)
    for idx, node in enumerate(G.nodes()):
        if node.startswith("N"):
            if (idx >= num_nodes-answer_count):
                node_colors.append("lightgreen")    
            else:
                node_colors.append("lightblue")
        elif node.startswith("P"):
            node_colors.append("lightcoral")

    labels = nx.get_node_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(10, 6))
    render_explanation(plt, G, pos, labels, node_colors)


def fibonacci(number_list, answer_count):
    first_diff = [number_list[i-1] for i in range(1, len(number_list))]

    G = nx.DiGraph()
    pos = {}

    for i, num in enumerate(number_list):
        G.add_node(f'N{i}', label=str(num))
        pos[f'N{i}'] = (i * 2, 3)

    for idx, i in enumerate(range(1, len(number_list))):
        if idx == 0:
            continue
        G.add_node(f'F{i}', label=f'{number_list[i-2]} + {number_list[i-1]}')
        pos[f'F{i}'] = (i * 2 - 1, 2)

    for i in range(2, len(number_list)):
        G.add_edge(f'N{i-2}', f'F{i}')
        G.add_edge(f'N{i-1}', f'F{i}')
        G.add_edge(f'F{i}', f'N{i}')

    node_colors = []
    num_nodes = len(number_list)
    for node in G.nodes():
        if node.startswith("N"):
            index = int(node[1:])
            if index >= num_nodes - answer_count:
                node_colors.append("lightgreen")
            else:
                node_colors.append("lightblue")
        elif node.startswith("F"):
            node_colors.append("lightcoral")

    labels = nx.get_node_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(10, 6))
    render_explanation(plt, G, pos, labels, node_colors)
    

def larik(number_list, answer_count, patterns):
    unique_colors = [
        "lightcoral", "peachpuff", "plum"
    ]
    random.shuffle(unique_colors)
    pattern_colors = {pattern: unique_colors[i % len(unique_colors)] for i, pattern in enumerate(patterns)}

    pattern_mapping = {op: [] for op in patterns}

    for i, num in enumerate(number_list):
        pattern_index = i % len(patterns)
        pattern_mapping[patterns[pattern_index]].append(i)

    G = nx.DiGraph()
    pos = {}

    for i, num in enumerate(number_list):
        G.add_node(f'N{i}', label=str(num))
        pos[f'N{i}'] = (i * 2, 3)

    node_colors = []
    num_nodes = len(number_list)

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

    
    for idx, node in enumerate(G.nodes()):
        if node.startswith("N"):
            if (idx >= num_nodes-answer_count):
                node_colors.append("lightgreen")    
            else:
                node_colors.append("lightblue")
        else:
            node_colors.append(node_colors.pop(0))

    labels = nx.get_node_attributes(G, 'label')
    fig, ax = plt.subplots(figsize=(10, 6))
    render_explanation(plt, G, pos, labels, node_colors)

def to_superscript(num):
    """Convert a number to its superscript equivalent, including numbers 100+."""
    superscript_map = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")
    return str(num).translate(superscript_map)

def pangkat(number_list, answer_count, root_list, angka_pangkat, selisih):
    G = nx.DiGraph()
    pos = {}

    for i, num in enumerate(number_list):
        G.add_node(f'N{i}', label=str(num))
        pos[f'N{i}'] = (i * 3, 3)

    for i, root in enumerate(root_list):
        G.add_node(f'R{i}', label=f"{root}{to_superscript(angka_pangkat)}")
        pos[f'R{i}'] = (i * 3, 2)

    for i in range(len(root_list) - 1):
        G.add_node(f'S{i}', label=f"+{selisih}")
        pos[f'S{i}'] = (i * 3 + 1.5, 1)

    for i in range(len(number_list)):
        G.add_edge(f'N{i}', f'R{i}')

    for i in range(len(root_list) - 1):
        G.add_edge(f'R{i}', f'S{i}')
        G.add_edge(f'S{i}', f'R{i+1}')

    labels = nx.get_node_attributes(G, 'label')

    node_colors = []
    num_nodes = len(number_list)

    for node in G.nodes():
        if node.startswith("N"):
            index = int(node[1:])
            if index >= num_nodes - answer_count:
                node_colors.append("lightgreen")
            else:
                node_colors.append("lightblue")
        elif node.startswith("R"):
            node_colors.append("peachpuff")
        elif node.startswith("S"):
            node_colors.append("lightcoral")

    render_explanation(plt, G, pos, labels, node_colors)
