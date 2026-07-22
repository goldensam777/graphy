"""
Tree (§1.4).
"""

from .graph import Graph
from .subgraph import SpanningGraph


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

    # TODO: Implement valued tree and oriented ones, and also complete lines 36-*

    def __repr__(self):
        return f"Tree(n={self.order}, m={len(self._edges)})"


class SpanningTree(Tree):
    """Spanning tree of `parent` (§1.2.2 + §1.4 combined): a Tree
    whose node set is exactly parent's node set.

    Deliberately single inheritance -- NOT SpanningTree(Tree,
    SpanningGraph). Tree and SpanningGraph don't share a compatible
    __init__ contract, so combining them via multiple inheritance
    creates a MRO where Tree's internal super().__init__() call
    resolves into SpanningGraph instead of Graph, and crashes
    (missing the `parent` argument SpanningGraph needs).

    Composition avoids that entirely: build the SpanningGraph first
    (validates edges belong to parent + keeps every node), then hand
    it to Tree's own constructor, which validates the tree invariants
    (|E| = n-1, connected) on top.
    """

    def __init__(self, parent: Graph, edges):
        spanning = SpanningGraph(parent, edges)
        super().__init__(spanning)

    def __repr__(self):
        return f"SpanningTree(n={self.order}, m={len(self._edges)})"