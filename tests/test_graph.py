import pytest
from graphy import Node, Edge, Arc, Graph


def test_graph_operations():
    g = Graph()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    g.add_node(n1)
    g.add_node(n2)
    assert n1 in g.nodes
    assert n2 in g.nodes

    # Undirected edge
    e1 = Edge(n1, n2, cost=10)
    g.add_edge(e1)

    assert g.has_edge(n1, n2)
    assert g.has_edge(n2, n1)
    assert not g.has_edge(n1, n3)
    assert g.degree(n1) == 1
    assert g.degree(n2) == 1

    # Should raise error when adding a directed Arc
    arc = Arc(n1, n2)
    with pytest.raises(ValueError, match="Graph \\(undirected\\) does not accept Arc objects"):
        g.add_edge(arc)

    # Parallel edge
    e2 = Edge(n1, n2, cost=5)
    g.add_edge(e2)
    assert g.degree(n1) == 2

    # Loop edge (counts twice for degree)
    e_loop = Edge(n1, n1, cost=2)
    g.add_edge(e_loop)
    assert g.degree(n1) == 4  # 2 from parallel + 2 from loop

    # Remove edge
    g.remove_edge(e2)
    assert g.degree(n1) == 3


def test_graph_connectivity_and_components():
    g = Graph()
    n1, n2, n3, n4 = Node(1), Node(2), Node(3), Node(4)

    # Empty graph
    assert g.is_connected()

    # Disconnected nodes
    g.add_node(n1)
    g.add_node(n2)
    assert not g.is_connected()
    assert len(g.connected_components()) == 2

    # Add connecting edge
    g.add_edge(Edge(n1, n2))
    assert g.is_connected()
    assert len(g.connected_components()) == 1

    # Add another component
    g.add_edge(Edge(n3, n4))
    assert not g.is_connected()
    components = g.connected_components()
    assert len(components) == 2
    assert {n1, n2} in components
    assert {n3, n4} in components


def test_graph_cyclomatic_number():
    g = Graph()
    n1, n2, n3 = Node(1), Node(2), Node(3)

    g.add_edge(Edge(n1, n2))
    g.add_edge(Edge(n2, n3))
    # Order: 3, Edges: 2, Components: 1 (it's a path)
    # Cyclomatic number: m - n + p = 2 - 3 + 1 = 0
    assert g.cyclomatic_number() == 0

    # Add edge to form a triangle
    g.add_edge(Edge(n3, n1))
    # Order: 3, Edges: 3, Components: 1
    # Cyclomatic number: 3 - 3 + 1 = 1
    assert g.cyclomatic_number() == 1
