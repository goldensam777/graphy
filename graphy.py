"""
graphy - graph theory library


graph = {
    "nodes": [1, 2, 3, 4],
    "edges": [
        {"u": 1, "v": 2, "cost": 5},
        {"u": 2, "v": 3, "cost": 3},
        {"u": 3, "v": 4, "cost": 2},
        {"u": 4, "v": 1, "cost": 4}
    ]
}


"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Node:
    """Graph vertex."""
    value: object


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
            raise ValueError("Graph (non-orienté) n'accepte pas de Arc.")
        self.edges.append(edge)

    def __iter__(self):
        return iter(self.nodes)

    def __repr__(self):
        return f"Graph(nodes={self.nodes}, edges={self.edges})"


class Digraph(Graph):
    """Directed graph; ``Digraph`` and ``directed graph`` are synonymous."""
    def add_edge(self, edge):
        if not isinstance(edge, Arc):
            raise ValueError("Digraph n'accepte que des Arc.")
        self.edges.append(edge)

    def __repr__(self):
        return f"Digraph(nodes={self.nodes}, edges={self.edges})"
