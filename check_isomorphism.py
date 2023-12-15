"""
The module checks two graphs for isomorphism.
"""

import math
from copy import deepcopy
from itertools import permutations
import numpy as np

def check_isomorphism(graph1_dict: dict, graph2_dict: dict)-> bool:
    """
    The main function to check if graphs are isomorphic.
    """
    def graph_matrix_creation(graph_dict: dict)-> np.array:
        """
        Turn the graph from dictionary into a matrix.
        """
        def make_undirected(graph: dict)-> dict:
            undirected_graph = {}
            for vertex, edges in graph.items():
                for edge in edges:
                    undirected_graph.setdefault(vertex, []).append(edge)
                    undirected_graph.setdefault(edge, []).append(vertex)
            for vertex, edges in undirected_graph.items():
                undirected_graph[vertex] = sorted(list(set(edges)))
            return undirected_graph
        graph_dict = make_undirected(graph_dict)
        list_of_rows = []
        list_of_vertices = list(graph_dict)
        for _, value in graph_dict.items():
            row = []
            for vertice in list_of_vertices:
                if vertice in value:
                    row.append(1)
                else:
                    row.append(0)
            list_of_rows.append(row)
        return np.array(list_of_rows)

    def matrix_change(graph_matrix: np.array, init_permut: tuple, permut: int)-> np.array:
        """
        The function with the main logic to return permutations.
        """
        graph_matrix[[*init_permut]] = graph_matrix[[*permut]]
        graph_matrix[:, [*init_permut]] = graph_matrix[:, [*permut]]
        return graph_matrix

    def check_vertices_number_inv(graph1_dict: dict, graph2_dict: dict)-> bool:
        """
        Invariant 1: check if both graphs have equal amount of vertices.
        """
        return len(graph1_dict) == len(graph2_dict)

    def check_edges_number_inv(graph1_dict: dict, graph2_dict: dict)-> bool:
        """
        Invariant 2: check if both graphs have equal amount of edges.
        """
        edges_double_number1 = 0
        edges_double_number2 = 0
        for value in graph1_dict.values():
            edges_double_number1 += len(value)
        for value in graph2_dict.values():
            edges_double_number2 += len(value)
        return edges_double_number1 == edges_double_number2

    def chech_degrees_of_vertices(graph1_dict: dict, graph2_dict: dict)-> bool:
        """
        Invariant 3: check if both graphs have equal degrees.
        """
        vertices_degrees_list1 = []
        vertices_degrees_list2 = []
        for value in graph1_dict.values():
            vertices_degrees_list1.append(len(value))
        for value in graph2_dict.values():
            vertices_degrees_list2.append(len(value))
        vertices_degrees_list1.sort()
        vertices_degrees_list2.sort()
        return vertices_degrees_list1 == vertices_degrees_list2

    if not check_vertices_number_inv(graph1_dict, graph2_dict):
        return False

    if not check_edges_number_inv(graph1_dict, graph2_dict):
        return False

    if not chech_degrees_of_vertices(graph1_dict, graph2_dict):
        return False

    number_of_vertices = len(graph1_dict)
    graph1_matrix = graph_matrix_creation(graph1_dict)
    graph2_matrix = graph_matrix_creation(graph2_dict)

    init_permut = tuple(range(number_of_vertices))
    permutations_generator = permutations(init_permut)

    number_of_iterations = math.factorial(number_of_vertices)

    for _ in range(number_of_iterations):
        graph1_matrix_copy = deepcopy(graph1_matrix)
        permut = next(permutations_generator)
        graph1_matrix_change = matrix_change(graph1_matrix_copy, init_permut, permut)

        if np.array_equal(graph1_matrix_change, graph2_matrix):
            return True

    return False
