"""
Induced subgraph, and its two special cases: clique and stable set
(§1.2.1).
"""

from itertools import combinations

from .graph import Graph


class Subgraph(Graph):
    """Induced subgraph of a parent Graph.

    Given a subset of the parent's nodes, keeps exactly those nodes
    and every edge of the parent whose both endpoints are in the
    subset — i.e. it is always the *induced* subgraph (§1.2.1), never
    an arbitrary A' subset chosen independently of S'.

    Built as an independent, frozen copy of the relevant slice of the
    parent — same pattern as Tree(graph) — not a live view: later
    changes to the parent are not reflected here.

    Clique and stable are not separate subclasses: they are conditions
    checked on an existing Subgraph via the is_clique / is_stable
    properties, since they're the same kind of object (an induced
    subgraph), just satisfying an extra property.
    """

    def __init__(self, parent: Graph, nodes):
        super().__init__()
        nodes = set(nodes)
        if not nodes.issubset(parent.adj):
            raise ValueError("Subgraph: all nodes must belong to the parent graph.")

        for node in nodes:
            self.add_node(node)
        for edge in parent.edges:
            if edge.u in nodes and edge.v in nodes:
                self.add_edge(edge)

    @property
    def is_clique(self):
        """True if every pair of distinct nodes is adjacent (§1.2.1)."""
        return all(
            self.has_edge(u, v) for u, v in combinations(self.nodes, 2)
        )

    @property
    def is_stable(self):
        """True if the subgraph has no edges at all (independent set, §1.2.1)."""
        return len(self._edges) == 0

    def __repr__(self):
        return f"Subgraph(n={self.order}, m={len(self._edges)})"
