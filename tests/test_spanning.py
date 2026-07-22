import pytest
from graphy import Node, Edge, Graph
from graphy.subgraph import SpanningGraph
from graphy.tree import Tree, SpanningTree


def _triangle():
    """Connected graph with a cycle: a-b, b-c, c-a."""
    g = Graph()
    a, b, c = Node("a"), Node("b"), Node("c")
    e1, e2, e3 = Edge(a, b), Edge(b, c), Edge(c, a)
    g.add_edge(e1)
    g.add_edge(e2)
    g.add_edge(e3)
    return g, a, b, c, e1, e2, e3


def test_spanning_graph_keeps_all_nodes_but_chosen_edges_only():
    g, a, b, c, e1, e2, e3 = _triangle()

    sg = SpanningGraph(g, [e1, e2])

    assert set(sg.nodes) == {a, b, c}  # spanning: every parent node kept
    assert sg.has_edge(a, b)
    assert sg.has_edge(b, c)
    assert not sg.has_edge(c, a)  # e3 excluded


def test_spanning_graph_keeps_isolated_nodes():
    g = Graph()
    a, b, isolated = Node("a"), Node("b"), Node("isolated")
    e = Edge(a, b)
    g.add_edge(e)
    g.add_node(isolated)

    sg = SpanningGraph(g, [e])

    assert isolated in sg.nodes  # spanning even though it has no edges


def test_spanning_graph_rejects_edge_outside_parent():
    g, a, b, c, e1, e2, e3 = _triangle()
    outsider = Edge(a, b)  # same endpoints as e1, but a different object

    with pytest.raises(ValueError, match="all edges must belong to the parent graph"):
        SpanningGraph(g, [outsider])


def test_spanning_tree_selects_valid_tree_from_a_cyclic_graph():
    g, a, b, c, e1, e2, e3 = _triangle()

    st = SpanningTree(g, [e1, e2])

    assert isinstance(st, Tree)
    assert set(st.nodes) == {a, b, c}
    assert len(st.edges) == 2


def test_spanning_tree_rejects_wrong_edge_count():
    g, a, b, c, e1, e2, e3 = _triangle()

    with pytest.raises(ValueError, match=r"Not a tree: \|E\|=3 != n-1=2"):
        SpanningTree(g, [e1, e2, e3])  # all 3 edges: still has the cycle
