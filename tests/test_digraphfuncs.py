from graphy import Node, Arc, Digraph
from graphy.utils.digraphfuncs import costs, relax


def test_costs_direct_arcs_and_unreachable():
    dg = Digraph()
    a, b, c = Node("a"), Node("b"), Node("c")
    dg.add_edge(Arc(a, b, cost=10))
    dg.add_node(c)  # no arc from a -> unreachable

    lam = costs(dg, a)

    assert lam[a] == 0
    assert lam[b] == 10
    assert lam[c] == float("inf")


def test_costs_picks_min_among_parallel_arcs():
    dg = Digraph()
    a, b = Node("a"), Node("b")
    dg.add_edge(Arc(a, b, cost=10))
    dg.add_edge(Arc(a, b, cost=3))
    dg.add_edge(Arc(a, b, cost=7))

    lam = costs(dg, a)

    assert lam[b] == 3


def test_relax_improves_when_cheaper():
    lam = {"a": 0, "b": 10, "c": 2}
    pred = {"a": None, "b": None, "c": None}

    improved = relax(lam, pred, "c", "b", 3)  # a->c=2, c->b=3 => 5 < 10

    assert improved is True
    assert lam["b"] == 5
    assert pred["b"] == "c"


def test_relax_does_not_worsen():
    lam = {"a": 0, "b": 5, "c": 2}
    pred = {"a": None, "b": "c", "c": None}

    improved = relax(lam, pred, "c", "b", 10)  # a->c=2, c->b=10 => 12, not < 5

    assert improved is False
    assert lam["b"] == 5
    assert pred["b"] == "c"  # untouched
