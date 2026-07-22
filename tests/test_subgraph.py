import pytest
from graphy import Node, Edge, Graph, Subgraph


def test_subgraph_keeps_only_induced_edges():
    g = Graph()
    a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
    g.add_edge(Edge(a, b))
    g.add_edge(Edge(b, c))
    g.add_edge(Edge(c, d))  # d excluded from the subgraph below

    sg = Subgraph(g, {a, b, c})

    assert set(sg.nodes) == {a, b, c}
    assert sg.has_edge(a, b)
    assert sg.has_edge(b, c)
    assert not sg.has_edge(c, d)  # c-d edge dropped: d not in the subset
    assert len(sg.edges) == 2


def test_subgraph_rejects_node_outside_parent():
    g = Graph()
    a, b = Node("a"), Node("b")
    g.add_edge(Edge(a, b))
    outsider = Node("z")

    with pytest.raises(ValueError, match="all nodes must belong to the parent graph"):
        Subgraph(g, {a, outsider})


def test_subgraph_handles_parallel_edges_and_loops():
    g = Graph()
    a, b = Node("a"), Node("b")
    g.add_edge(Edge(a, b, cost=1))
    g.add_edge(Edge(a, b, cost=2))  # parallel edge
    g.add_edge(Edge(a, a))          # loop

    sg = Subgraph(g, {a, b})

    assert len(sg.edges) == 3
    assert sg.degree(a) == 2 + 2  # 2 parallel edges to b + loop counts double


def test_subgraph_is_clique_true_for_complete_subset():
    g = Graph()
    a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
    g.add_edge(Edge(a, b))
    g.add_edge(Edge(b, c))
    g.add_edge(Edge(a, c))
    g.add_edge(Edge(c, d))  # d only connects to c: {a,b,c} stays a clique

    triangle = Subgraph(g, {a, b, c})
    not_clique = Subgraph(g, {a, b, d})

    assert triangle.is_clique is True
    assert not_clique.is_clique is False


def test_subgraph_is_stable_true_for_edgeless_subset():
    g = Graph()
    a, b, c = Node("a"), Node("b"), Node("c")
    g.add_edge(Edge(a, b))
    g.add_node(c)  # c isolated

    stable = Subgraph(g, {a, c})
    not_stable = Subgraph(g, {a, b})

    assert stable.is_stable is True
    assert not_stable.is_stable is False


def test_subgraph_single_node_is_both_clique_and_stable():
    g = Graph()
    a, b = Node("a"), Node("b")
    g.add_edge(Edge(a, b))

    solo = Subgraph(g, {a})

    assert solo.is_clique is True   # vacuously true: no pair to check
    assert solo.is_stable is True   # no edges
