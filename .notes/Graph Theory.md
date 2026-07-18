## 1. Undirected Graphs

### 1.1. Definitions and Ontology

- **An undirected graph $G = (V, E)$ consists of a finite set $V = \{v_1, v_2, \dots, v_n\}$** whose elements are called vertices (or nodes) and a finite family $E = \{e_1, e_2, \dots, e_m\}$ whose elements are called edges. Each edge is associated with an unordered pair of vertices representing its endpoints.

- We write $e = \{u, v\}$ or $e = uv$ interchangeably. If $e = \{u, v\}$, we say that $u$ and $v$ are neighbors, adjacent, or incident to $e$, and that $e$ is incident to $u$ and $v$.

- The pair associated with an edge can also be a repetition of the same vertex, in which case it is called a **loop** ($e = \{v, v\}$).

- A vertex with no incident edges is called **isolated**. A vertex incident to exactly one edge is a **pendant vertex** (or leaf), and its incident edge is a **pendant edge**.

- If multiple edges are incident to the same two vertices, they are called **parallel edges** or **multiple edges**. We also refer to this as a family of edges.

- If an undirected graph **contains at least one loop or parallel edge**, it is called a **multigraph**. A graph with no parallel edges and no loops is a **simple graph**.

- The **order** of a graph is its number of vertices $n = |V|$.

Programming:

```python
class Node:
    pass

class Edge:
    pass

class Graph:
    def __init__(self, order: int, edges: set[Edge], nodes: set[Node]):
        pass
```

#### 1.1.1. Graphical Representations

![[Pasted image 20260702163548.png]]

#### 1.1.2. Walks, Trails, Paths, and Cycles

- Let $G = (V, E)$ be a graph where $V$ is the set of vertices and $E$ is the set of edges.

- **A walk in a graph is an alternating sequence of vertices and edges starting with a vertex and ending with a vertex, such that each edge is flanked by its endpoints.**

- A walk is **simple** (often called a **trail** in English) if **it uses each of its edges at most once.**

- A walk is **elementary** (often called a **path** in English) if **it visits each of its vertices at most once.**

- **A cycle (or circuit/closed trail) in a graph is an alternating sequence of vertices and edges starting at a vertex $v_i$ and ending at that same vertex $v_i$.**

- A cycle is **simple** (often called a **circuit**) if **it uses each of its edges at most once.**

- **A cycle is elementary (or a simple cycle) if it visits each of its vertices at most once (except for the start and end vertex).**

- The length $l$ of a walk/trail/path is the **number of edges it contains.**


#### 1.1.3. Key Concepts

##### A- Degrees in a Graph
The **degree of a vertex $v$**, denoted $d(v)$, is the number of edges incident to $v$. **Note that a loop on a vertex counts twice.**

The **degree of a graph** is the **maximum degree among all its vertices**, i.e., $\Delta(G) = \max(d(v))$.

##### B- Theorem: The Handshaking Lemma
**The sum of the degrees of the vertices is equal to twice the number of edges.** That is, if $G = (V, E)$:
$$\boxed{\sum_{v \in V} d(v) = 2 \cdot |E|}$$
This is the degree sum formula, also known as the **handshaking lemma**: the intuition is that each edge has two endpoints, so counting degrees counts every edge exactly twice.

**Proof.** We count the number of pairs $(v, e)$ where $v \in V$ is an endpoint of the edge $e \in E$ (i.e., $v$ is incident to $e$) in two different ways:

- **By vertex:** for a fixed vertex $v$, the number of incident edges is $d(v)$ by definition. Summing over all vertices yields $\sum_{v \in V} d(v)$ pairs.
- **By edge:** each edge $e = \{u, v\}$ has exactly two endpoints (a loop also has two endpoints counted with multiplicity, which is consistent with the "loop counts twice" convention). Thus, each edge contributes exactly 2 to the count. Summing over all $|E|$ edges yields $2 \cdot |E|$ pairs.

Both counts compute the cardinality of the same set, so $\sum_{v \in V} d(v) = 2 \cdot |E|$. $\blacksquare$

This proof technique—counting the same set in two different ways—is called a **double counting argument**, a common tool in combinatorics.

**Corollary (Handshaking Lemma, strict sense).** *In any finite undirected graph, the number of vertices with odd degree is even.*

**Proof.** Let us partition $V$ into two disjoint subsets: $P$, the set of vertices of even degree, and $I$, the set of vertices of odd degree. The theorem above gives:
$$\sum_{v \in P} d(v) + \sum_{v \in I} d(v) = 2 \cdot |E|$$
The right-hand side is even, and $\sum_{v \in P} d(v)$ is even since it is a sum of even terms. By subtraction, $\sum_{v \in I} d(v)$ must also be even. Since this is a sum of $|I|$ terms that are all odd, the sum can only be even if the number of terms $|I|$ is even (a sum of an odd number of odd terms is odd). Thus, $|I|$ is even. $\blacksquare$

**Concrete Interpretation:** At any gathering of people where some shake hands, the number of people who shake an odd number of hands is always even.

**Terminology Note:** Depending on the source, "Handshaking Lemma" may refer to the formula $\sum d(v) = 2|E|$ itself or specifically to its corollary about the parity of odd-degree vertices. Both results are mathematically bound, but it is useful to know there is no universal naming convention.

**Sources:** Koudi J., *Théorie des graphes et ses applications*, IFRI, 2022-2023, Theorem 1.3, p.7 · Diestel R., *Graph Theory*, Springer GTM 173, chap. 1.

---

### 1.2. Common Graph Types

#### 1.2.1. Subgraphs
Given a graph $G = (V, E)$, a **subgraph** $G' = (V', E')$ is a graph such that $V' \subset V$ and $E' \subset E$.

- **Induced Subgraph:** A subgraph obtained by taking a subset of vertices $V' \subset V$ and keeping all edges of $G$ that have both endpoints in $V'$.
- **Clique:** An induced subgraph that is complete (i.e., its vertices are pairwise adjacent).
- **Independent Set (or Stable Set):** An induced subgraph with no edges.

*Note: Complete graphs are not just subgraphs; a graph itself is complete if all of its vertices are pairwise adjacent (denoted $K_n$).*

#### 1.2.2. Spanning Subgraph (Partial Graph)
A **spanning subgraph** (referred to as *graphe partiel* in French) is a subgraph that contains all vertices of the original graph but only a subset of the edges ($V' = V$, $E' \subset E$).

#### 1.2.3. Planar Graph
A **planar graph** is a graph that can be drawn in the plane such that no two edges cross. It naturally satisfies Euler's formula:
$$\boxed{n - m + f = 2}$$
where $n$ is the number of vertices, $m$ is the number of edges, and $f$ is the number of faces (including the single unbounded outer face).

*This relation is also known as the Descartes-Euler relation.*

**Source:** Koudi J., *op. cit.*, supplemented by Euler's relation (cf. bibmath.net).

#### 1.2.4. Matchings
- **A matching** of a graph $G = (V, E)$ is a subset of edges $M \subset E$ such that no two edges share a common vertex.
- **A perfect matching** is a matching that saturates all vertices of the graph (each vertex is incident to exactly one edge in the matching). A necessary condition for a perfect matching is that $n = |V|$ must be **even**.
- **A maximal matching** is a matching to which no other edge can be added without violating the matching property (maximal under inclusion).
- **A maximum matching** is a matching of maximum possible cardinality. Note that a *maximal* matching is not necessarily a *maximum* matching.

**Source:** Koudi J., *op. cit.*, §1.2.3.

---

### 1.3. Connectivity and Cyclomatic Number

- **A graph is connected** if there is a path between every pair of vertices.
- A non-connected graph can be decomposed into **connected components**. A connected component is a maximal connected subgraph.

**Theorem (Cyclomatic Number).** For a graph $G$ with $m$ edges, $n$ vertices, and $p$ connected components, we define:
$$\nu(G) = m - n + p$$
called the **cyclomatic number** of $G$. We always have $\nu(G) \geq 0$, and $\nu(G) = 0$ if and only if $G$ is acyclic (i.e., a forest).

**Intuition:** $\nu(G)$ counts the number of edges that must be removed to break all cycles (the number of "extra" edges relative to a spanning forest).

**Source:** Koudi J., *op. cit.*, Theorem 1.6.

---

### 1.4. Trees and Forests

- **A tree** is a connected, acyclic graph.
- **A forest** is an acyclic graph (its connected components are trees).

**Proposition 1.7.** *If $G = (V, E)$ is a tree of order $n$, then $|E| = n - 1$.*

**Proof (Sketch, by induction on $n$).** For $n = 1$, a tree has $0 = 1 - 1$ edges. Suppose it holds for any tree of order $n - 1$ ($n \geq 2$). Any tree of order $n \geq 2$ has at least one **leaf** (a vertex of degree 1)—otherwise, all degrees would be $\geq 2$, and we could trace a cycle, contradicting acyclicity. Removing this leaf and its single incident edge yields a tree of order $n - 1$, which has $n - 2$ edges by induction. Thus, the original tree had $(n - 2) + 1 = n - 1$ edges. $\blacksquare$

**Proposition 1.8.** *If $G = (V, E)$ is a forest of order $n$ with $p$ connected components, then $|E| = n - p$.*

**Proof.** Since each connected component is a tree, if the $i$-th component has $n_i$ vertices, it has $n_i - 1$ edges by Proposition 1.7. Summing over all $p$ components:
$$|E| = \sum_i (n_i - 1) = \left(\sum_i n_i\right) - p = n - p. \quad \blacksquare$$

**Definition 1.9 (Spanning Tree).** A spanning tree of a graph $G = (V, E)$ is a spanning subgraph of $G$ that is a tree. It contains all vertices of $G$, is acyclic, and has $n - 1$ edges. A graph has a spanning tree if and only if it is connected.

**Source:** Koudi J., *op. cit.*, §1.4.2.

---

### 1.5. Eulerian Graphs

- **An Eulerian circuit** is a closed walk that visits every edge of $G$ exactly once. A graph is **Eulerian** if it contains an Eulerian circuit.
- **An Eulerian trail** is an open walk that visits every edge of $G$ exactly once. A graph containing an Eulerian trail but no Eulerian circuit is **semi-Eulerian**.
- By convention, a graph consisting only of isolated vertices is Eulerian.

**Theorem 1.10 (Eulerian Graph).** *A connected multigraph $G = (V, E)$ is Eulerian if and only if every vertex of $G$ has an even degree.*

**Proof.**
($\Rightarrow$) If $G$ has an Eulerian circuit, each time the circuit passes through a vertex $v$, it uses two incident edges (one to enter, one to leave). Since the circuit uses every edge exactly once, $d(v)$ must be even.

($\Leftarrow$) By induction on $|E|$ (sketch): if every vertex has an even degree and $G$ is connected, we can trace a cycle $C$. Removing the edges of $C$ leaves a graph where all vertices still have even degrees (since we removed 2 edges from each visited vertex). By induction, the remaining connected components have Eulerian circuits, which can be merged with $C$ at their junction points. $\blacksquare$

**Theorem 1.11 (Semi-Eulerian Graph).** *A connected multigraph $G = (V, E)$ is semi-Eulerian if and only if it has exactly 0 or 2 vertices of odd degree.*

This follows from the previous theorem: if there are exactly 2 odd-degree vertices $u$ and $v$, adding a virtual edge $\{u, v\}$ makes all degrees even. An Eulerian circuit in this augmented graph yields an Eulerian trail from $u$ to $v$ once the virtual edge is removed.

**Corollary 1.12.** *If a multigraph $G$ has only one connected component with edges (plus any number of isolated vertices), and every vertex has an even degree, then $G$ is Eulerian.*

**Historical Application — Seven Bridges of Königsberg (Euler, 1736):** The Königsberg bridge graph has 4 vertices, all with odd degrees (3 or 5). By Theorem 1.11, it is neither Eulerian nor semi-Eulerian: it is impossible to cross every bridge exactly once. This is the founding problem of graph theory.

**Source:** Koudi J., *op. cit.*, Theorems 1.10 & 1.11, p.10 · Euler L., *Solutio problematis ad geometriam situs pertinentis*, 1736.

---

### 1.6. Hamiltonian Graphs

- **A Hamiltonian graph** (resp. **semi-Hamiltonian**) is a graph that contains a cycle (resp. a path) visiting every vertex exactly once. Unlike the Eulerian case, the constraint is on **vertices**, not edges.
- **Deciding if a graph is Hamiltonian is NP-complete**, so there is no simple degree characterization. We rely instead on **sufficient conditions**.

**Theorem (Complete Graph).** *A complete graph $K_n$ ($n \geq 3$) is Hamiltonian.*

**Dirac's Theorem (1952).** *A simple graph with $n \geq 3$ vertices is Hamiltonian if every vertex has a degree of at least $n/2$.*

**Ore's Theorem (1960).** *A simple graph with $n \geq 3$ vertices is Hamiltonian if, for every pair of non-adjacent vertices $u$ and $v$, $d(u) + d(v) \geq n$.* (Ore's theorem generalizes Dirac's.)

**Pósa's Theorem.** *A simple graph with $n \geq 3$ vertices is Hamiltonian if:*
- *For all integers $k$ such that $1 \leq k < \frac{n-1}{2}$, the number of vertices of degree $\leq k$ is strictly less than $k$;*
- *The number of vertices of degree $\leq \frac{n-1}{2}$ is less than or equal to $\frac{n-1}{2}$.*

**Definition (Graph Closure).** The closure $\text{cl}(G)$ of $G$ is the graph obtained by repeatedly adding edges between pairs of non-adjacent vertices $u, v$ such that $d(u) + d(v) \geq n$, until no such pairs remain.

**Bondy–Chvátal Theorem (1976).** *A graph is Hamiltonian if and only if its closure is Hamiltonian.*

**Source:** Koudi J., *op. cit.*, §1.4.4, p.11-12 · Bondy J.A. & Murty U.S.R., *Graph Theory*, Springer GTM 244, chap. 4.

---

### 1.7. Matrix Representations

#### 1.7.1. Adjacency Matrix
The **adjacency matrix** of a multigraph $G = (V, E)$ with $V = \{v_1, \dots, v_n\}$ is a symmetric $n \times n$ matrix $M = (m_{ij})$ where $m_{ij}$ is the number of edges connecting $v_i$ and $v_j$.
For a simple graph, $m_{ij} = 1$ if $v_i \sim v_j$, and $0$ otherwise.

**Proposition 1.17 (Number of Walks of Length $k$).** *If $M$ is the adjacency matrix of $G$, then the $(i, j)$-entry of $M^k$ is the number of walks of length $k$ from $v_i$ to $v_j$.*

**Proof (By induction on $k$).** For $k=1$, this is the definition of $M$. If it holds for $k$, a walk of length $k+1$ from $v_i$ to $v_j$ consists of a walk of length $k$ from $v_i$ to some intermediate vertex $v_\ell$, followed by an edge from $v_\ell$ to $v_j$. The total number is $\sum_\ell M^k_{i\ell} M_{\ell j} = (M^{k+1})_{ij}$. $\blacksquare$

#### 1.7.2. Incidence Matrix
For $G = (V, E)$ with $V = \{v_1, \dots, v_n\}$ and $E = \{e_1, \dots, e_m\}$, the **incidence matrix** $I(G) = (a_{ij})$ is an $n \times m$ matrix where:
$$a_{ij} = \begin{cases} 
1 & \text{if } v_i \text{ is incident to } e_j \\ 
2 & \text{if } v_i \text{ is incident to } e_j \text{ and } e_j \text{ is a loop} \\ 
0 & \text{otherwise} 
\end{cases}$$

**Source:** Koudi J., *op. cit.*, §1.5, p.12-14.

---

### 1.8. Minimum Spanning Trees (MST)

- A **weighted graph** assigns a weight $w(e) \in \mathbb{R}$ to each edge $e$.
- A **minimum spanning tree (MST)** of a connected weighted graph $G = (V, E)$ is a spanning tree whose sum of edge weights is minimized.

**Kruskal's Algorithm.** Sort the edges by weight in non-decreasing order, then greedily add each edge to the growing forest if and only if it does not create a cycle. Complexity: $O(m \log m)$ using a union-find data structure.

**Prim's Algorithm.** Grow the tree starting from an arbitrary root vertex $r$. At each step, add the minimum-weight edge connecting the tree to a vertex not yet in the tree. Complexity: $O(m \log n)$ using a binary heap, or $O(m + n \log n)$ using a Fibonacci heap.

**Why they work:** Both algorithms rely on the **cut property**: for any cut of the graph, the minimum-weight edge crossing the cut belongs to some MST.

**Source:** Koudi J., *op. cit.*, §1.7.1, p.15-17 · Kruskal J., *On the Shortest Spanning Subtree of a Graph...*, 1956 · Prim R.C., *Shortest Connection Networks...*, BSTJ, 1957.

---

## 2. Directed Graphs (Digraphs)

### 2.1. Definitions

**A directed graph (digraph) $G = (V, A)$** consists of a set of vertices $V$ and a set of ordered pairs of vertices $A$ called **arcs**. For an arc $u = (i, j)$, $i$ is the **tail** (initial endpoint) and $j$ is the **head** (terminal endpoint).

- **Loop:** An arc $u = (i, i)$ whose endpoints coincide.
- **Successors** of $i$: $\text{Succ}(i) = \{j \mid (i, j) \in A\}$.
- **Predecessors** of $i$: $\text{Pred}(i) = \{j \mid (j, i) \in A\}$.

---

### 2.2. Degrees and Adjacency Matrices in Digraphs

The **adjacency matrix** $M = (a_{ij})$ of a digraph satisfies $a_{ij} = 1$ if there is an arc $(v_i, v_j)$, and $0$ otherwise.

**Proposition 2.8.**
1. Out-degree: $d^+(v_i) = \sum_{j=1}^n a_{ij}$ (row sum).
2. In-degree: $d^-(v_i) = \sum_{j=1}^n a_{ji}$ (column sum).
3. Sum of degrees: $\sum_i d^+(v_i) = \sum_i d^-(v_i) = |A|$.
4. The trace $\text{tr}(M)$ is the number of loops.
5. $M^k$ gives the number of directed walks of length $k$ between two vertices.

The **incidence matrix** $I = (b_{ij})$ of size $n \times m$ is defined by:
$$b_{ij} = \begin{cases} 
1 & \text{if } v_i \text{ is the tail of } a_j \\ 
-1 & \text{if } v_i \text{ is the head of } a_j \text{ and } a_j \text{ is not a loop} \\ 
0 & \text{otherwise} 
\end{cases}$$

**Bipartite Graph:** A graph is bipartite if $V$ can be partitioned into two sets $V_1, V_2$ such that every edge has one endpoint in $V_1$ and the other in $V_2$.

---

### 2.3. Directed Paths and Circuits

- **Directed Path:** An alternating sequence of vertices and arcs starting at $u$ and ending at $v$, traversed in the direction of the arcs.
- **Distance** $d(u, v)$: Length of the shortest directed path from $u$ to $v$. Note that $d(u, v) \neq d(v, u)$ in general.
- **Directed Cycle (Circuit):** A directed path that starts and ends at the same vertex.

---

### 2.4. Shortest Paths — Dijkstra's Algorithm

**Context.** Computes the shortest path from a single source vertex to all other vertices in a weighted digraph with **non-negative weights**. If weights are negative, Bellman-Ford must be used.

**Algorithm:**
- **Initialization:**
  - $\lambda(source) = 0$; $\lambda(j) = w(source, j)$ if there is an arc, else $\infty$.
  - $P(j) = source$ if adjacent, else $\text{NIL}$.
  - $S = \{source\}$, $T = V \setminus \{source\}$.
- **Iterations:**
  - While $T$ is not empty:
    - Choose $i \in T$ that minimizes $\lambda(i)$.
    - Remove $i$ from $T$ and add it to $S$.
    - For each successor $j \in T$ of $i$:
      - If $\lambda(j) > \lambda(i) + w(i, j)$, update:
        $\lambda(j) = \lambda(i) + w(i, j)$
        $P(j) = i$

**Source:** Koudi J., *op. cit.*, §2.1.1, p.25-27 · Dijkstra E.W., *A note on two problems in connexion with graphs*, 1959.

---

### 2.5. Shortest Paths in Acyclic Digraphs (DAGs)

A digraph is acyclic (a DAG) **if and only if** we can topologically sort its vertices such that for every arc $(u, v)$, $u$ appears before $v$.

1. Assign level 0 to all vertices with in-degree 0, then remove them and their outgoing arcs from the graph.
2. Repeat to find level 1, 2, etc., until the graph is empty.

Once topological levels are established, shortest paths can be computed in a single pass in $O(n + m)$ using dynamic programming:
$$\lambda(i) = \min_{j \in \text{Pred}(i)} \{\lambda(j) + w(j, i)\}$$

**Source:** Koudi J., *op. cit.*, §2.1.2, p.28-32.

---

### 2.6. Project Scheduling — MPM (Metra Potential Method)

Used to manage tasks with precedence constraints.
Key metrics for task $X$ with duration $d_X$:
- **Earliest Start Time** $t_X = \max \{t_Y + d_Y : Y \in \text{Pred}(X)\}$.
- **Earliest Finish Time** $= t_X + d_X$.
- **Latest Start Time** $t_X^* = \min \{t_Y^* - d_X : Y \in \text{Succ}(X)\}$.
- **Latest Finish Time** $= \min \{t_Y^* : Y \in \text{Succ}(X)\}$.
- **Total Float (Total Slack)** $M_t(X) = t_X^* - t_X$: Allowable delay for $X$ without delaying the project completion.
- **Free Float (Free Slack)** $M_l(X) = \min \{t_Y - d_X - t_X : Y \in \text{Succ}(X)\}$: Allowable delay without affecting successor tasks.
- **Critical Task:** A task $X$ with $M_t(X) = 0$.
- **Critical Path:** A path from start to end consisting only of critical tasks.

**Source:** Koudi J., *op. cit.*, §2.2.1, p.34-36.

---

## 3. Graph Coloring

- **Vertex Coloring:** Assign colors to vertices such that no two adjacent vertices share the same color. Each color class is an **independent set**.
- **Chromatic Number** $\chi(G)$: Minimum number of colors required to color $G$.
- **Lower Bound:** If $G$ contains a clique of size $\omega(G)$, then $\chi(G) \geq \omega(G)$.
- **Complexity:** Finding $\chi(G)$ is **NP-hard** in general, but polynomial for specific classes like **interval graphs** (solved using a greedy algorithm).
- **Four Color Theorem (Appel & Haken, 1976):** The chromatic number of any planar graph is at most 4.

**Source:** Koudi J., *op. cit.*, §1.8, p.17-19 · Appel K. & Haken W., *Every Planar Map is Four Colorable*, 1976.
