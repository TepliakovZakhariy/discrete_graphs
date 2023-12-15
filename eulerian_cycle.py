""" 
A module to find Euler's circut. 
"""

def is_connected(graph, start):
    """
    Check if the graph is connected.
    """
    visited = set()
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                dfs(neighbor)
    dfs(start)
    return len(visited) == len(graph)

def find_euler_circuit(graph):
    """
    Return the Euler's circuit of the graph, if it exists.
    """
    def has_even_degree(graph):
        return all(len(edges) % 2 == 0 for edges in graph.values())

    def find_next_edge(vertex, graph):
        for neighbor in graph[vertex]:
            if (neighbor, vertex) not in removed_edges and (vertex, neighbor) not in removed_edges:
                removed_edges.add((vertex, neighbor))
                return neighbor
        return None

    if not has_even_degree(graph) or not is_connected(graph, list(graph.keys())[0]):
        return None

    circuit = []
    stack = [list(graph.keys())[0]]
    removed_edges = set()

    while stack:
        vertex = stack[-1]
        next_vertex = find_next_edge(vertex, graph)
        if next_vertex:
            stack.append(next_vertex)
        else:
            circuit.append(stack.pop())
    return circuit[::-1]
