from graphy import Node, Arc, Digraph
from graphy.algorihtms.dijkstra import dijkstra
from graphy.utils.digraphfuncs import shortest_path


def test_shortest_path_reconstructs_indirect_route():
    dg = Digraph()
    a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
    dg.add_edge(Arc(a, b, cost=10))
    dg.add_edge(Arc(a, c, cost=2))
    dg.add_edge(Arc(c, b, cost=3))
    dg.add_edge(Arc(b, d, cost=1))

    lam, pred = dijkstra(dg, a)

    assert shortest_path(pred, a, d) == [a, c, b, d]


def test_shortest_path_source_equals_target():
    dg = Digraph()
    a = Node("a")
    dg.add_node(a)
    lam, pred = dijkstra(dg, a)

    assert shortest_path(pred, a, a) == [a]


def test_shortest_path_unreachable_returns_none():
    dg = Digraph()
    a, b = Node("a"), Node("b")
    dg.add_edge(Arc(a, b, cost=1))
    z = Node("z")
    dg.add_node(z)

    lam, pred = dijkstra(dg, a)

    assert shortest_path(pred, a, z) is None


def test_shortest_path_direct_edge():
    dg = Digraph()
    a, b = Node("a"), Node("b")
    dg.add_edge(Arc(a, b, cost=5))

    lam, pred = dijkstra(dg, a)

    assert shortest_path(pred, a, b) == [a, b]
