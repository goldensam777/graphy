"""
Directed graph: Digraph (§2.1-2.2).
"""

from .entities import Arc
from .graph import Graph


class Digraph(Graph): 
    """Directed graph / digraph.

    Two separate dicts: adj (successors) and pred (predecessors) —
    needed independently for Dijkstra and topological/level-based
    ordering on a DAG.
    """

    def __init__(self):
        super().__init__()
        self.pred = {}  # {Node: {Node: [Arc, ...]}}

    def add_node(self, node):
        super().add_node(node)
        self.pred.setdefault(node, {})

    def add_edge(self, edge):
        if not isinstance(edge, Arc):
            raise ValueError("Digraph accepts only Arc objects.")
        u, v = edge.u, edge.v
        self.add_node(u)
        self.add_node(v)
        self.adj[u].setdefault(v, []).append(edge)
        self.pred[v].setdefault(u, []).append(edge)
        self._edges.append(edge)

    def remove_edge(self, edge):
        u, v = edge.u, edge.v
        self.adj[u][v].remove(edge)
        if not self.adj[u][v]:
            del self.adj[u][v]
        self.pred[v][u].remove(edge)
        if not self.pred[v][u]:
            del self.pred[v][u]
        self._edges.remove(edge)

    def successors(self, node):
        return list(self.adj[node].keys())

    def predecessors(self, node):
        return list(self.pred[node].keys())

    def out_degree(self, node):
        return sum(len(edges) for edges in self.adj[node].values())

    def in_degree(self, node):
        return sum(len(edges) for edges in self.pred[node].values())

    def degree(self, node):
        # Directed analogue of the handshaking lemma: no factor of 2,
        # each arc is either outgoing or incoming, never both.
        return self.out_degree(node) + self.in_degree(node)

    def __repr__(self):
        return f"Digraph(n={self.order}, m={len(self._edges)})"
