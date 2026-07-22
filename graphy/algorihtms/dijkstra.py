from graphy import *
from graphy.utils.digraphfuncs import costs, relax

# Write the algorithm as a function


def dijkstra(digraph: Digraph, source: Node) -> tuple[dict[Node, float], dict[Node, Node]]:
    """
    Computes the shortest path from a single source vertex to all other vertices in a weighted digraph with non-negative weights.
    If weights are negative, Bellman-Ford must be used.
    """
    lam = costs(digraph, source)
    # Direct neighbors of `source` already have their λ set by costs();
    # pred must be initialized in lockstep, or relax() will never fire
    # for them later (lam[j] > lam[i]+cost is False when they're equal).
    pred = {
        v: (source if v != source and lam[v] != float("inf") else None)
        for v in digraph.nodes
    }
    s = set()
    while len(s) < len(digraph.nodes):
        i = min({v for v in digraph.nodes if v not in s}, key=lam.get)
        s.add(i)
        for j, arcs in digraph.adj[i].items():
            for arc in arcs:
                relax(lam, pred, i, j, arc.cost)
    return lam, pred
