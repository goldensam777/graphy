"""
Tree (§1.4).
"""

from .graph import Graph


class Tree(Graph):
    """Tree: connected graph with no cycle and no loop.

    Built from an existing Graph, validating the invariants of the
    tree proposition (|E| = n - 1) plus connectivity — |E| = n - 1
    alone doesn't guarantee it's a tree (it only guarantees acyclicity
    IF the graph is also connected).
    """

    def __init__(self, graph: Graph):
        super().__init__()
        self.adj = graph.adj
        self._edges = list(graph.edges)

        if len(self._edges) != self.order - 1:
            raise ValueError(
                f"Not a tree: |E|={len(self._edges)} != n-1={self.order - 1}."
            )
        if not self.is_connected():
            raise ValueError("Not a tree: the graph is not connected.")

    def __repr__(self):
        return f"Tree(n={self.order}, m={len(self._edges)})"
