"""
Directed Graphs utilities for graphy
"""


from graphy import *


def costs(digraph: Digraph, source: Node) -> dict[Node, float]:
    """Initial λ vector: costs[source]=0, costs[j]=min direct cost if
    there's a direct arc source->j, else infinity."""
    lam = {v: float("inf") for v in digraph.nodes}
    lam[source] = 0
    for v, arcs in digraph.adj[source].items():
        lam[v] = min(a.cost for a in arcs)
    return lam


def relax(lam: dict[Node, float], pred: dict[Node, Node], i: Node, j: Node, cost: float) -> bool:
    """Relax the arc i->j of weight `cost` if it improves λ(j).
    Mutates lam and pred in place. Returns True if an improvement happened."""
    if lam[j] > lam[i] + cost:
        lam[j] = lam[i] + cost
        pred[j] = i
        return True
    return False


def shortest_path(pred: dict[Node, Node], source: Node, target: Node) -> list[Node] | None:
    """Reconstruct the path source -> target from a pred dict built by
    a shortest-path algorithm (e.g. dijkstra). Returns None if target
    is unreachable from source."""
    if target == source:
        return [source]
    if pred.get(target) is None:
        return None
    path = [target]
    while path[-1] != source:
        path.append(pred[path[-1]])
    path.reverse()
    return path

