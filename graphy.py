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

>>> from graphy import Graph, Node, Edge
>>> g = Graph()
>>> a, b = Node(1), Node(2)
>>> g.add_edge(Edge(a, b, cost=5))
>>> g.degree(a)
1
"""

from dataclasses import dataclass
from collections import deque


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


class Graph:
    """Undirected graph.

    adj[u][v] = list of edges between u and v — a LIST, not a single
    edge, since the graph may be a multigraph (parallel edges / loops).
    """

    def __init__(self):
        self.adj = {}      # {Node: {Node: [Edge, ...]}}
        self._edges = []   # source of truth, insertion order (useful for Kruskal)

    def add_node(self, node):
        self.adj.setdefault(node, {})

    def add_edge(self, edge):
        if isinstance(edge, Arc):
            raise ValueError("Graph (undirected) does not accept Arc objects.")
        u, v = edge.u, edge.v
        self.add_node(u)
        self.add_node(v)
        self.adj[u].setdefault(v, []).append(edge)
        if u != v:  # loop: don't duplicate the dict entry
            self.adj[v].setdefault(u, []).append(edge)
        self._edges.append(edge)

    def remove_edge(self, edge):
        u, v = edge.u, edge.v
        self.adj[u][v].remove(edge)
        if not self.adj[u][v]:
            del self.adj[u][v]
        if u != v:
            self.adj[v][u].remove(edge)
            if not self.adj[v][u]:
                del self.adj[v][u]
        self._edges.remove(edge)

    def has_edge(self, u, v):
        return v in self.adj.get(u, {})

    def degree(self, node):
        """d(v) — a loop counts twice."""
        d = 0
        for neighbor, edges in self.adj[node].items():
            d += len(edges) * (2 if neighbor == node else 1)
        return d

    def is_connected(self):
        """BFS from an arbitrary vertex."""
        if not self.adj:
            return True
        start = next(iter(self.adj))
        seen = {start}
        queue = deque([start])
        while queue:
            u = queue.popleft()
            for v in self.adj[u]:
                if v not in seen:
                    seen.add(v)
                    queue.append(v)
        return len(seen) == len(self.adj)

    def connected_components(self):
        """List of Node sets, one entry per connected component."""
        unseen = set(self.adj)
        components = []
        while unseen:
            start = next(iter(unseen))
            seen = {start}
            queue = deque([start])
            while queue:
                u = queue.popleft()
                for v in self.adj[u]:
                    if v not in seen:
                        seen.add(v)
                        queue.append(v)
            components.append(seen)
            unseen -= seen
        return components

    def cyclomatic_number(self):
        """nu(G) = m - n + p."""
        return len(self._edges) - self.order + len(self.connected_components())

    @property
    def nodes(self):
        return list(self.adj.keys())

    @property
    def edges(self):
        return list(self._edges)

    @property
    def order(self):
        return len(self.adj)

    def __iter__(self):
        return iter(self.adj)

    def __repr__(self):
        return f"Graph(n={self.order}, m={len(self._edges)})"


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