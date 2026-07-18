import pytest
from graphy import Node, Edge, Graph, Tree


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
