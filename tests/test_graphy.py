import pytest
from graphy import Node, Edge, Arc, Graph, Digraph, Tree


def test_node_equality_and_hashing():
    n1 = Node(1)
    n2 = Node(1)
    n3 = Node(2)

    assert n1 == n2
    assert n1 != n3
    assert hash(n1) == hash(n2)
    assert hash(n1) != hash(n3)
    assert repr(n1) == "Node(1)"
    assert repr(Node("A")) == "Node('A')"


def test_edge_and_arc_creation():
    u = Node(1)
    v = Node(2)
    edge = Edge(u, v, cost=5.5)
    arc = Arc(u, v, cost=3)

    assert edge.u == u
    assert edge.v == v
    assert edge.cost == 5.5
    assert isinstance(edge, Edge)
    assert not isinstance(edge, Arc)

    assert arc.u == u
    assert arc.v == v
    assert arc.cost == 3
    assert isinstance(arc, Arc)
    assert isinstance(arc, Edge)  # Arc inherits from Edge


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


def test_digraph_operations():
    dg = Digraph()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)

    # Should raise error when adding an undirected Edge
    edge = Edge(n1, n2)
    with pytest.raises(ValueError, match="Digraph accepts only Arc objects"):
        dg.add_edge(edge)

    arc1 = Arc(n1, n2, cost=1.5)
    arc2 = Arc(n2, n3, cost=2.5)
    dg.add_edge(arc1)
    dg.add_edge(arc2)

    assert dg.successors(n1) == [n2]
    assert dg.predecessors(n2) == [n1]
    assert dg.successors(n2) == [n3]

    assert dg.out_degree(n1) == 1
    assert dg.in_degree(n1) == 0
    assert dg.degree(n1) == 1

    assert dg.out_degree(n2) == 1
    assert dg.in_degree(n2) == 1
    assert dg.degree(n2) == 2

    # Remove arc
    dg.remove_edge(arc1)
    assert dg.in_degree(n2) == 0


def test_tree_validation():
    g = Graph()
    n1, n2, n3 = Node(1), Node(2), Node(3)

    # 1. Disconnected graph
    g.add_node(n1)
    g.add_node(n2)
    g.add_node(n3)
    # |E| = 0, n = 3. |E| != n - 1
    with pytest.raises(ValueError, match="Not a tree: \\|E\\|=0 != n-1=2"):
        Tree(g)

    # 2. Add edges but still not connected (loop + parallel edge)
    # Let's add 2 edges but make it disconnected
    g2 = Graph()
    g2.add_edge(Edge(n1, n2))
    g2.add_edge(Edge(n1, n2))
    g2.add_node(n3)
    # |E| = 2, n = 3. |E| == n - 1, but not connected
    with pytest.raises(ValueError, match="Not a tree: the graph is not connected"):
        Tree(g2)

    # 3. Valid Tree
    g_tree = Graph()
    g_tree.add_edge(Edge(n1, n2))
    g_tree.add_edge(Edge(n2, n3))
    tree = Tree(g_tree)
    assert tree.order == 3
    assert len(tree.edges) == 2
    assert repr(tree) == "Tree(n=3, m=2)"
