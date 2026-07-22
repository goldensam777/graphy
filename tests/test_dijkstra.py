from graphy import Node, Arc, Digraph
from graphy.algorihtms.dijkstra import dijkstra


def test_dijkstra_simple_path_prefers_shorter_route():
    # a->b direct (10) is more expensive than a->c->b (2+3=5).
    dg = Digraph()
    a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
    dg.add_edge(Arc(a, b, cost=10))
    dg.add_edge(Arc(a, c, cost=2))
    dg.add_edge(Arc(c, b, cost=3))
    dg.add_edge(Arc(b, d, cost=1))

    lam, pred = dijkstra(dg, a)

    assert lam[a] == 0
    assert lam[c] == 2
    assert lam[b] == 5
    assert lam[d] == 6
    assert pred[b] == c
    assert pred[d] == b
    assert pred[a] is None


def test_dijkstra_unreachable_node_stays_infinite():
    dg = Digraph()
    a, b = Node("a"), Node("b")
    dg.add_edge(Arc(a, b, cost=1))
    unreachable = Node("z")
    dg.add_node(unreachable)

    lam, pred = dijkstra(dg, a)

    assert lam[unreachable] == float("inf")
    assert pred[unreachable] is None


def test_dijkstra_picks_min_among_parallel_arcs():
    dg = Digraph()
    a, b = Node("a"), Node("b")
    dg.add_edge(Arc(a, b, cost=10))
    dg.add_edge(Arc(a, b, cost=3))

    lam, _ = dijkstra(dg, a)

    assert lam[b] == 3


def test_dijkstra_single_node_graph():
    dg = Digraph()
    a = Node("a")
    dg.add_node(a)

    lam, pred = dijkstra(dg, a)

    assert lam == {a: 0}
    assert pred == {a: None}


def test_dijkstra_terminates_on_a_cycle():
    # a -> b -> c -> a (cycle) plus a -> d, must not loop forever.
    dg = Digraph()
    a, b, c, d = Node("a"), Node("b"), Node("c"), Node("d")
    dg.add_edge(Arc(a, b, cost=1))
    dg.add_edge(Arc(b, c, cost=1))
    dg.add_edge(Arc(c, a, cost=1))
    dg.add_edge(Arc(a, d, cost=5))

    lam, pred = dijkstra(dg, a)

    assert lam[a] == 0
    assert lam[b] == 1
    assert lam[c] == 2
    assert lam[d] == 5
