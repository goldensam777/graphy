"""
graphy - graph theory library

Example input format:
    graph = {
        "nodes": [1, 2, 3, 4],
        "edges": [
            {"u": 1, "v": 2, "cost": 5},
            {"u": 2, "v": 3, "cost": 3},
            {"u": 3, "v": 4, "cost": 2},
            {"u": 4, "v": 1, "cost": 4}
        ]
    }

>>> from graphy import Graph
>>> g = Graph()
"""

from dataclasses import dataclass


class Node:
    """Graph vertex. Mutable entity: neighbors grow as the graph is built."""
    def __init__(self, value):
        self.value = value
        self.neighbors = []  # list of incident Edge/Arc

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __repr__(self):
        return f"Node({self.value})"


@dataclass(frozen=True)
class Edge:
    """Undirected edge: an unordered pair {u, v}, optionally weighted."""
    u: Node
    v: Node
    cost: float = 0


@dataclass(frozen=True)
class Arc(Edge):
    """Directed edge: an ordered pair (u, v). Always directed by nature."""
    pass


class Graph:
    """Undirected graph, the default case."""
    def __init__(self):
        self.nodes = []
        self.edges = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        if isinstance(edge, Arc):
            raise ValueError("Graph (undirected) does not accept Arc objects.")
        edge.u.neighbors.append(edge)
        edge.v.neighbors.append(edge)
        self.edges.append(edge)

    @property
    def order(self):
        return len(self.nodes)

    def __iter__(self):
        return iter(self.nodes)

    def __repr__(self):
        return f"Graph(nodes={self.nodes}, edges={self.edges})"


class Digraph(Graph):
    """Directed graph; 'Digraph' and 'directed graph' are synonymous."""
    def add_edge(self, edge):
        if not isinstance(edge, Arc):
            raise ValueError("Digraph accepts only Arc objects.")
        edge.u.neighbors.append(edge)  # seul u connaît l'arc — c'est orienté
        self.edges.append(edge)

    def __repr__(self):
        return f"Digraph(nodes={self.nodes}, edges={self.edges})"