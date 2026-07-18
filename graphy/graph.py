"""
Undirected graph: Graph (§1.1, connectivity/cyclomatic number §1.3).
"""

import random
from collections import deque

from .entities import Arc


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

    def random_cycle(self):
        """Return a random cycle in the graph, if one exists, else None."""
        if self.cyclomatic_number() == 0:
            return None

        # Random walk until we hit a visited node, then backtrack to form a cycle.
        start = random.choice(self.nodes)
        visited = {start: None}  # node -> predecessor
        current = start
        while True:
            neighbors = list(self.adj[current].keys())
            next_node = random.choice(neighbors)
            if next_node in visited:
                # Cycle found: backtrack to form the cycle path.
                cycle = [next_node]
                while current != next_node:
                    cycle.append(current)
                    current = visited[current]
                cycle.append(next_node)
                cycle.reverse()
                return cycle
            visited[next_node] = current
            current = next_node

    @property
    def cycle(self):
        """Return a cycle in the graph, if one exists, else None."""
        return self.random_cycle()
