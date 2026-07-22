"""
graphy ~ graph theory library
References: check @.notes/"Graph Theory" for more information.

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

from .entities import Node, Edge, Arc
from .graph import Graph
from .digraph import Digraph
from .tree import Tree
from .subgraph import Subgraph

__all__ = ["Node", "Edge", "Arc", "Graph", "Digraph", "Tree", "Subgraph"]
