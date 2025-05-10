from collections import defaultdict


def convert_network(G):
    V_prime = []
    E_prime = []

    # Step 1: Split vertices
    vertex_map = {}
    for v in G['vertices']:
        v_in = f"{v}_in"
        v_out = f"{v}_out"
        vertex_map[v] = (v_in, v_out)
        V_prime.append(v_in)
        V_prime.append(v_out)
        E_prime.append((v_in, v_out, G['vertex_capacity'][v]))

    # Step 2: Reconnect edges
    for u, v, capacity in G['edges']:
        u_out = vertex_map[u][1]
        v_in = vertex_map[v][0]
        E_prime.append((u_out, v_in, capacity))

    return {'vertices': V_prime, 'edges': E_prime}


# 示例用法
G = {
    'vertices': ['A', 'B', 'C'],
    'vertex_capacity': {'A': 10, 'B': 5, 'C': 8},
    'edges': [('A', 'B', 7), ('B', 'C', 6)]
}

G_prime = convert_network(G)
print("Converted Network:", G_prime)

import networkx as nx


def can_escape(grid_size, start_points):
    G = nx.DiGraph()

    # Add source and sink nodes
    G.add_node('source')
    G.add_node('sink')

    # Add grid nodes and edges
    for i in range(grid_size):
        for j in range(grid_size):
            node = f"{i},{j}"
            G.add_node(node)

            if i > 0:
                G.add_edge(f"{i - 1},{j}", node, capacity=1)
            if i < grid_size - 1:
                G.add_edge(f"{i + 1},{j}", node, capacity=1)
            if j > 0:
                G.add_edge(f"{i},{j - 1}", node, capacity=1)
            if j < grid_size - 1:
                G.add_edge(f"{i},{j + 1}", node, capacity=1)

            if i == 0 or i == grid_size - 1 or j == 0 or j == grid_size - 1:
                G.add_edge(node, 'sink', capacity=1)

    # Connect start points to source
    for x, y in start_points:
        G.add_edge('source', f"{x},{y}", capacity=1)

    # Calculate maximum flow
    max_flow_value = nx.maximum_flow_value(G, 'source', 'sink')

    return max_flow_value == len(start_points)


# 示例用法
grid_size = 4
start_points = [(1, 1), (2, 2)]

result = can_escape(grid_size, start_points)
print("Can escape:", result)