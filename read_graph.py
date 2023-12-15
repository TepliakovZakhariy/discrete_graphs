'''
This module provides a function to read a graph from a file and return it as a dictionary.
'''

def read_graph_from_file(filepath: str)-> dict:
    '''
    Read a graph from a file and return it as a dictionary.
    '''
    graph = {}
    with open(filepath, mode='r', encoding='utf-8') as file:
        for line in file:
            vertex1, vertex2 = line.strip().split(',')
            try:
                vertex1 = int(vertex1)
                vertex2 = int(vertex2)
            except ValueError:
                pass
            graph.setdefault(vertex1, []).append(vertex2)
    return {k: sorted(v) for k, v in sorted(graph.items())}
