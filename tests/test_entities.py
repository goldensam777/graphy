from graphy import Node, Edge, Arc


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
