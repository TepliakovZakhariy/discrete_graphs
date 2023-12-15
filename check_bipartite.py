"""
This module contains a function to check whether a given graph is bipartite.
"""

def check_bipartite(graph: dict) -> bool:
    """
    The function checks whether the graph is bipartite.
    """
    if not graph:
        return False

    visited = {}

    def dfs(node: int | str) -> bool:
        """
        Perform depth-first search (DFS) on a graph starting from a given node.
        """
        for adjacent_node in graph[node]:
            if adjacent_node in visited:
                if visited[adjacent_node] == visited[node]:
                    return False
            else:
                visited[adjacent_node] = 1 - visited[node]
                if not dfs(adjacent_node):
                    return False
        return True

    for node in graph:
        if node not in visited:
            visited[node] = 0
            if not dfs(node):
                return False

    return True
