'''
This module provides a function to color the vertices of a graph using a greedy algorithm.
'''

def color_graph(graph: dict) -> list:
    """
    Colors the vertices of a graph using a greedy algorithm.
    """
    colors = {}
    colored_vertices = []

    for vertex in graph:
        neighbors = graph[vertex]

        used_colors = set()

        for neighbor in neighbors:
            if neighbor in colors:
                used_colors.add(colors[neighbor])

        for color in range(3):
            if color not in used_colors:
                colors[vertex] = color
                colored_vertices.append((vertex, color))
                break
        else:
            return False

    return colored_vertices
