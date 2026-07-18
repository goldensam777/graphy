"""
Core entities: Node, Edge, Arc (§1.1).
"""

from dataclasses import dataclass


class Node:
    """Graph vertex. Hashable by value: used as a key in Graph/Digraph
    adjacency dicts."""

    def __init__(self, value):
        self.value = value

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        return isinstance(other, Node) and self.value == other.value

    def __repr__(self):
        return f"Node({self.value!r})"


@dataclass
class Edge:
    """Undirected edge {u, v}, optionally weighted.

    No custom __hash__/__eq__: undirectedness is carried by Graph.adj
    (adj[u][v] and adj[v][u] reference the same edge), not by the Edge
    object itself.
    """
    u: Node
    v: Node
    cost: float = 0


@dataclass
class Arc(Edge):
    """Directed edge (u -> v). Distinct from Edge only by type, used to
    enforce that directed/undirected edges are never mixed in
    Graph.add_edge / Digraph.add_edge."""
    pass
