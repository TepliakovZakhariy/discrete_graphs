'''
This module provides a function to check if a given graph has a Hamiltonian cycle.
'''

def hamiltonian_cycle(graph: dict) -> list | None:
    """
    Checks if a given graph has a Hamiltonian cycle.
    """
    if not graph or not all(graph.values()):
        return None

    start_node = list(graph.keys())[0]
    path = []

    def dfs_hamiltonian_cycle(node: int | str, path: list) -> list | None:
        '''
        Depth-first search algorithm to find a Hamiltonian cycle in a graph.
        '''

        path.append(node)

        if len(path) == len(graph):
            if start_node in graph[node]:
                return path + [start_node]
            return None

        for adjacent_node in graph[node]:
            if adjacent_node not in path:
                result = dfs_hamiltonian_cycle(adjacent_node, path.copy())
                if result:
                    return result

        return None

    return dfs_hamiltonian_cycle(start_node, path)
