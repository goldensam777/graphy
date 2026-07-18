import pytest
from graphy import Node, Edge, Arc, Digraph


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
