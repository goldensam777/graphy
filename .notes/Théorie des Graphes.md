## 1. Graphes non-orientés

### 1.1. Définitions et ontologie

- **Un graphe non-orienté G = (V, E) est la donnée d’un ensemble fini $V = \left\{v1 , v2 , · · · , v_n \right\}$** dont les éléments sont appelés sommets et d’une famille finie $E = \left\{e1 , e2 , · · · , e_m \right\}$ dont les éléments sont appelés arêtes (Edges en anglais), chacune associée à une paire non-ordonnée de sommets représentant les extrémités de l’arête.
    
- On écrit indifféremment $e = \left\{u, v\right\}$ ou $e = \left\{u, v\right\}$. Si $e = \left\{u, v\right\}$, on dit que u et v sont voisins et qu’ils sont adjacents, ou incidents à e et que e est incidente à u et à v.
    
- La paire associée à une arête peut également être la répétition d’un sommet, auquel cas on parle de boucle ($e = \left\{ v, v \right\}$).
    
- Un sommet auquel aucune arête n’est incidente est dit isolé. Un sommet incident à une seule arête est dit pendant et l’arête est une arête pendante.
    
- Si plusieurs arêtes sont incidentes à la fois à deux sommets, on dit qu’elles sont des arêtes parallèles ou arêtes multiples. On parle aussi de famille d’arêtes.
    
- Si graphe non orienté **contient au moins une boucle ou d’arêtes parallèles**, on dit qu’il est un _multigraphe_. Un graphe ne comportant pas d’arêtes parallèles ni de boucles est un graphe simple.
    
- On appelle ordre d’un graphe le nombre de sommets $n$ de ce graphe.
    

Programmation:

```python
class Sommmet:
	pass
	
class Arete:
	pass
	
class Graphe:
	def __init__(self, ordre: int, aretes: set[Arete], sommets: set[Sommet]):
		return ...

```

#### 1.1.1. Représentations Graphiques

![[Pasted image 20260702163548.png]]

#### 1.1.2. Chaines et Cycles

- Soit $G = (S, A)$ un graphe, $S$, l'ensemble des sommets et $A$, l'ensemble des arêtes de ce graphe.
    
- **Une chaîne dans un graphe est une suite alternée de sommets et d'arêtes qui commencent par un sommet et finissent par un autre sommet, tel que chaque arête est entourée par ses extrémités.**
    
- Une chaîne est _simple_ si **elle utilise une et une seule fois chacune de ses arêtes.**
    
- Une chaîne est _élémentaire_ si **elle utilise une et une seule fois chacun de ses sommets.**
    
- **Un cycle dans un graphe est une suite alternée de sommets et d'arêtes qui commencent par un sommet i de S(soit S l'ensemble des sommets de ce graphe G) et fini par ce même sommet.**
    
- Un cycle est _simple_ si **celui-ci utilise une et une seule fois chacune de ses arêtes.**
    
- **Un cycle est _élémentaire_ si celui-ci utilise une et une seule fois chacun de ses sommets.**
    
- La longueur $l$ d'une _chaîne_ est le **nombre d'arêtes de la chaîne.**
    

#### 1.1.3 Concepts Importants

##### A- Degrés dans un graphe

On appelle **degré d'un sommet $v$ et on note $d(v)$ le nombre d'arêtes incidentes à ce sommet. Il est à noter qu'==une boucle sur un sommet compte double==**.

On appelle **degré d'un graphe** le **degré maximum d'un graphe.** Autrement dit: $\max(d(v))$. C'est la définition la plus simple possible.

##### B- Théorème: Lemme des poignées de mains

**La somme des degrés des sommets est égale à deux fois le nombre d'arêtes.** Entre autres: Si $G = (V, E), \text{on a}:$ $\boxed{\sum_{v \in V} d(v) = 2 \cdot |E|}$ C'est le théorème des degrés, aussi appelé _lemme des poignées de main_ (handshaking lemma) : l'intuition est que chaque arête a **deux** extrémités, donc en comptant les degrés on compte chaque arête exactement deux fois.

**Démonstration.** On compte de deux façons différentes le nombre de couples $(v, e)$ où $v \in V$ est une extrémité de l'arête $e \in E$ (on dit que $v$ est _incident_ à $e$) :

- **Par sommet :** pour un sommet $v$ fixé, le nombre d'arêtes qui lui sont incidentes est par définition $d(v)$. En sommant sur tous les sommets, on obtient $\sum_{v \in V} d(v)$ couples.
- **Par arête :** chaque arête $e = {u, v}$ possède exactement deux extrémités (une boucle en possède aussi deux, comptées avec multiplicité, ce qui est cohérent avec la convention _"une boucle compte double"_ pour le degré). Chaque arête contribue donc pour exactement 2 au décompte. En sommant sur les $|E|$ arêtes, on obtient $2 \cdot |E|$ couples.

Les deux décomptes portent sur le même ensemble, donc $\sum_{v \in V} d(v) = 2 \cdot |E|$. $\blacksquare$

Cette technique de preuve — dénombrer un même ensemble de deux façons différentes — s'appelle un **argument de double comptage** (double counting) ; elle revient très souvent en combinatoire.

**Corollaire (lemme des poignées de main, au sens strict).** _Dans tout graphe non orienté fini, le nombre de sommets de degré impair est pair._

**Démonstration.** Séparons $V$ en deux sous-ensembles disjoints : $P$ les sommets de degré pair, et $I$ les sommets de degré impair. Le théorème précédent donne : $$\sum_{v \in P} d(v) + \sum_{v \in I} d(v) = 2 \cdot |E|$$ Le membre de droite est pair, et $\sum_{v \in P} d(v)$ est une somme de termes pairs donc elle est paire. Par différence, $\sum_{v \in I} d(v)$ est donc pair. Or c'est une somme de $|I|$ termes tous impairs : une telle somme n'est paire que si $|I|$ est pair (une somme d'un nombre impair de termes impairs est impaire). Donc $|I|$ est pair. $\blacksquare$

**Interprétation concrète (nom du lemme) :** dans une réunion de plusieurs personnes où certaines se serrent la main (chaque poignée de main = une arête entre deux personnes), le nombre de personnes ayant serré un nombre impair de mains est nécessairement pair.

**N.B. — attention terminologique :** selon les sources, le nom _"lemme des poignées de main"_ désigne soit la formule $\sum d(v) = 2|E|$ elle-même (convention de ce cours, cf. Koudi, _Théorie des graphes et ses applications_, IFRI, 2022-2023, Théorème 1.3), soit uniquement son corollaire sur la parité des sommets de degré impair (convention plus répandue dans la littérature anglo-saxonne, cf. Diestel, _Graph Theory_, ou bibmath.net). Les deux résultats sont mathématiquement liés (le second se déduit du premier) mais il vaut mieux garder à l'esprit qu'il n'y a pas de convention universelle sur le nom.

**Sources :** Koudi J., _Théorie des graphes et ses applications_, IFRI, 2022-2023, Théorème 1.3, p.7 · Diestel R., _Graph Theory_, Springer GTM 173, chap. 1.

### 1.2. Quelques types de graphes

#### 1.2.1. Notion de sous-graphes

##### **==C'est quoi un sous-graphe ?==**

Sois un graphe $G=(S, A)$ Un sous-graphe $G' = (S', A'), S' \subset S, A' \subset A$ est un graphe dont les arêtes et les sommets sont des éléments de A' et S' respectivement.

- **Sous-graphe induit: sous-graphe dont les sommets et les arêtes du graphe initial sont conservées, dans la façon dont elles sont liées.**
- **Sous-graphe induit complet: sous-graphe induit dont les sommets sont deux à deux liés par une arête(entre autres deux à deux adjacents). Elle est appelée _==clique==_.**
- **Stable/ ==independent set==: sous-graphe induit sans arêtes.**

**N.B: Les sous-graphes ne sont pas les seuls à être complets. On peut avoir des graphes complets. Ce sont des graphes dont les sommets sont deux-à-deux adjacents.**

Quelques types de graphes:

#### 1.2.2. Graphe Partiel

Un graphe partiel est un (sous-) graphe (couvrant) qui possède tous les sommets du graphe initial, mais n'en possède pas toutes les arêtes.

#### 1.2.3. Graphe planaire

Un graphe planaire est un graphe dont les arêtes ne se croisent pas en représentation. Il satisfait naturellement la formule:

$\boxed{s-a+f = 2}$

$s: \text{nombre de sommets}$ $a: \text{nombre d'arêtes}$ $f: \text{nombre de faces (la face à l'extérieur compte aussi!)}$ [==C'est la relation de Descartes-Euler==](https://www.bibmath.net/dico/index.php?action=affiche&quoi=./g/grapheplanaire.html)

Cette formule ne se démontre pas facilement à ce stade (récurrence sur le nombre d'arêtes en retirant une arête d'un cycle à chaque étape, cas de base = arbre où $f=1$) ; elle sera reprise plus rigoureusement quand la notion d'arbre couvrant sera posée (§1.4). **Source :** Koudi J., _op. cit._, complété par la relation d'Euler, cf. bibmath.net.

#### 1.2.4. Couplages

- **Un couplage (matching) d'un graphe $G = (V, E)$ est un sous-graphe (ou, de façon équivalente, un sous-ensemble d'arêtes) composé d'arêtes deux à deux non adjacentes** (i.e. ne partageant aucune extrémité).
- **Un couplage parfait (perfect matching)** est un couplage qui sature tous les sommets du graphe (chaque sommet est extrémité d'exactement une arête du couplage). Une condition nécessaire immédiate : un couplage parfait ne peut exister que si $n = |V|$ est **pair**, puisque chaque arête consomme 2 sommets.
- **Un couplage est dit maximal** s'il contient un nombre maximal d'arêtes deux à deux non adjacentes (i.e. on ne peut lui ajouter aucune arête sans casser la propriété). Attention à ne pas confondre _maximal_ (au sens de l'inclusion, on ne peut pas ajouter d'arête) et _maximum_ (de cardinal le plus grand possible) — un couplage maximal n'est pas nécessairement maximum.

**Source :** Koudi J., _op. cit._, §1.2.3.

### 1.3. Connexité et nombre cyclomatique

- **Un graphe est connexe** s'il est possible, à partir de n'importe quel sommet, de rejoindre tous les autres en suivant les arêtes (autrement dit, il existe une chaîne entre toute paire de sommets).
- Un graphe non connexe se décompose en **composantes connexes**. Une composante connexe est un sous-graphe induit maximal et connexe : elle regroupe exactement les sommets accessibles les uns depuis les autres.

**Théorème (nombre cyclomatique).** Pour un graphe $G$ ayant $m$ arêtes, $n$ sommets et $p$ composantes connexes, on définit : $$\nu(G) = m - n + p$$ appelé **nombre cyclomatique** de $G$ (prononcer _"nu de G"_). On a toujours $\nu(G) \geq 0$, et $\nu(G) = 0$ si et seulement si $G$ est sans cycle (i.e. $G$ est une forêt).

**Intuition :** $\nu(G)$ compte, en un sens, le nombre d'arêtes "en trop" par rapport à un arbre couvrant de chaque composante — c'est-à-dire le nombre d'arêtes qu'il faudrait retirer pour casser tous les cycles. Ce résultat se justifie via la Proposition 1.8 ci-dessous ($|E| = n - p$ pour une forêt), en observant qu'ajouter une arête à une forêt sans créer de sommet supplémentaire crée nécessairement un cycle.

**Source :** Koudi J., _op. cit._, Théorème 1.6.

### 1.4. Arbres et forêts

- **Un arbre** est un graphe connexe sans cycle ni boucle.
- **Une forêt** est un graphe sans cycle ni boucle (pas nécessairement connexe). Chaque composante connexe d'une forêt est un arbre.

**Proposition 1.7.** _Si $G = (V, E)$ est un arbre d'ordre $n$, alors $|E| = n - 1$._

**Démonstration (esquisse, par récurrence sur $n$).** Pour $n = 1$, un arbre réduit à un sommet isolé a $0 = 1 - 1$ arête. Supposons la propriété vraie pour tout arbre à $n-1$ sommets ($n \geq 2$). Un arbre à $n \geq 2$ sommets possède toujours au moins une **feuille** (un sommet de degré 1) — sinon, tous les sommets seraient de degré $\geq 2$ et on pourrait construire un cycle en suivant les arêtes sans jamais revenir sur ses pas, ce qui contredit l'absence de cycle. En retirant cette feuille et son unique arête incidente, on obtient un arbre à $n-1$ sommets, qui a par hypothèse de récurrence $n-2$ arêtes. L'arbre original avait donc $n-2+1 = n-1$ arêtes. $\blacksquare$

**Proposition 1.8.** _Soit $G = (V, E)$ une forêt d'ordre $n$ possédant $p$ composantes connexes. Alors $|E| = n - p$._

**Démonstration.** Chaque composante connexe est un arbre (par définition de forêt) ; si la $i$-ème composante a $n_i$ sommets, la Proposition 1.7 donne $n_i - 1$ arêtes pour cette composante. En sommant sur les $p$ composantes : $|E| = \sum_i (n_i - 1) = \left(\sum_i n_i\right) - p = n - p$. $\blacksquare$

**Définition 1.9 (Arbre couvrant).** Un arbre couvrant d'un graphe $G = (V, E)$ est un graphe partiel de $G$ qui est un arbre. Il contient tous les sommets de $G$, est sans cycle, et comporte $n - 1$ arêtes de $G$. Un graphe possède un arbre couvrant si et seulement si il est connexe.

**Source :** Koudi J., _op. cit._, §1.4.2.

### 1.5. Graphes eulériens

- **Un cycle eulérien** d'un graphe $G$ est un cycle passant une et une seule fois par chacune des arêtes de $G$. $G$ est dit **eulérien** s'il possède un cycle eulérien.
- **Une chaîne eulérienne** passe une et une seule fois par chacune des arêtes. Un graphe ne possédant que des chaînes eulériennes (et pas de cycle eulérien) est dit **semi-eulérien**.
- Intuition : un graphe est eulérien (ou semi-eulérien) si on peut le dessiner sans lever le crayon et sans repasser deux fois sur la même arête.
- N.B. : par convention, un graphe constitué uniquement de sommets isolés est eulérien.

**Théorème 1.10 (Graphe eulérien).** _Un multigraphe $G = (V, E)$ connexe est eulérien si et seulement si tout sommet de $G$ est de degré pair._

**Démonstration.** ($\Rightarrow$) Si $G$ possède un cycle eulérien, chaque passage du cycle par un sommet $v$ "consomme" deux arêtes incidentes à $v$ (une pour arriver, une pour repartir), sauf éventuellement au sommet de départ/arrivée où c'est également le cas puisque le cycle est fermé. Comme le cycle utilise **toutes** les arêtes exactement une fois, $d(v)$ est nécessairement pair pour chaque $v$.

($\Leftarrow$) Réciproque, par récurrence sur $|E|$ (esquisse) : si tout sommet est de degré pair et $G$ est connexe, on montre qu'il existe un cycle (fermeture possible car repartir d'un sommet non isolé de degré pair mène toujours à un retour au point de départ, faute d'arête "de sortie" manquante). On extrait un premier cycle $C$, on retire ses arêtes : les composantes restantes ont encore tous leurs sommets de degré pair (on a retiré un nombre pair d'arêtes à chaque sommet traversé), on leur applique l'hypothèse de récurrence, puis on "recolle" les cycles obtenus au cycle $C$ aux points de jonction. $\blacksquare$

**Théorème 1.11 (Graphe semi-eulérien).** _Un multigraphe $G = (V, E)$ connexe est semi-eulérien si et seulement si $G$ possède 0 ou 2 sommets de degré impair._

Ce résultat se déduit du précédent : s'il y a exactement 2 sommets de degré impair $u$ et $v$, on ajoute une arête fictive ${u,v}$ pour rendre tous les degrés pairs, on applique le Théorème 1.10 pour obtenir un cycle eulérien du graphe augmenté, puis on retire l'arête fictive : le cycle devient une chaîne eulérienne de $u$ à $v$ dans $G$.

**Conséquence 1.12.** _Soit $G = (V, E)$ un multigraphe non connexe contenant une seule composante connexe non réduite à un sommet isolé. Si tout sommet de $G$ est de degré pair, alors $G$ est eulérien_ (les sommets isolés n'affectent pas le parcours).

**Application historique — les sept ponts de Königsberg (Euler, 1736) :** le graphe associé aux quatre quartiers de Königsberg reliés par sept ponts possède 4 sommets tous de degré impair (3 ou 5) ; par le Théorème 1.11 (et même son cas limite), il n'est ni eulérien ni semi-eulérien : il est **impossible** de traverser chaque pont exactement une fois. C'est le problème fondateur de la théorie des graphes.

**Source :** Koudi J., _op. cit._, Théorèmes 1.10 et 1.11, p.10 · Euler L., _Solutio problematis ad geometriam situs pertinentis_, 1736 (article fondateur).

### 1.6. Graphes hamiltoniens

- **Un graphe hamiltonien** (resp. **semi-hamiltonien**) est un graphe sur lequel on peut trouver un cycle (resp. une chaîne) passant par tous les sommets une et une seule fois — contrairement au cas eulérien, la contrainte porte sur les **sommets**, pas sur les arêtes.
- **Décider si un graphe est (semi-)hamiltonien est NP-complet** (contrairement au cas eulérien qui se décide en temps polynomial via le simple test de parité des degrés) — il n'existe donc, à ce jour, aucune caractérisation aussi simple que le Théorème 1.10. On dispose seulement de **conditions suffisantes**.

**Théorème (graphe complet).** _Un graphe complet est hamiltonien._ C'est un cas particulier immédiat du théorème de Dirac ci-dessous (dans $K_n$, tout sommet est de degré $n-1 \geq n/2$ pour $n \geq 2$).

**Théorème de Dirac (1952).** _Un graphe simple à $n$ sommets ($n \geq 3$) dont chaque sommet est de degré au moins $\dfrac{n}{2}$ est hamiltonien._

**Théorème de Ore (1960).** _Un graphe simple à $n$ sommets ($n \geq 3$) tel que la somme des degrés de toute paire de sommets non adjacents vaut au moins $n$ est hamiltonien._ (Ore généralise Dirac : la condition de Dirac implique celle d'Ore.)

**Théorème de Pósa.** _Un graphe simple à $n$ sommets ($n \geq 3$) est hamiltonien si :_

- _pour tout entier $k$ tel que $1 \leq k < \dfrac{n-1}{2}$, le nombre de sommets de degré $\leq k$ est strictement inférieur à $k$ ;_
- _le nombre de sommets de degré $\leq \dfrac{n-1}{2}$ est inférieur ou égal à $\dfrac{n-1}{2}$._

**Définition (fermeture d'un graphe).** La fermeture $\text{cl}(G)$ de $G$ est le graphe obtenu en ajoutant, tant qu'il en existe, une arête entre chaque paire de sommets non adjacents $a, b$ telle que $d(a) + d(b) \geq n$.

**Théorème de Bondy–Chvátal (1976).** _Un graphe est hamiltonien si et seulement si sa fermeture est hamiltonienne._ Ce théorème n'est utile en pratique que combiné à l'un des critères précédents appliqué sur la fermeture (qui a plus d'arêtes donc satisfait plus facilement Dirac/Ore).

Les démonstrations de Dirac, Ore et Pósa reposent sur un argument commun (par l'absurde : on suppose $G$ non hamiltonien maximal pour l'ajout d'arêtes sous la contrainte, on construit une chaîne hamiltonienne, puis on montre par un argument de "retournement" — _rotation-extension technique_ de Pósa — qu'un cycle hamiltonien existerait quand même, contredisant l'hypothèse). Elles ne sont pas reproduites ici en détail ; voir la référence ci-dessous pour la preuve complète.

**Source :** Koudi J., _op. cit._, §1.4.4, p.11-12 · Bondy J.A. & Murty U.S.R., _Graph Theory_, Springer GTM 244, chap. 4 (démonstrations complètes de Dirac/Ore/Chvátal-Erdős).

### 1.7. Représentations matricielles

#### 1.7.1. Matrice d'adjacence

La **matrice d'adjacence** d'un multigraphe $G = (V,E)$, $V = {v_1, \dots, v_n}$, est la matrice carrée $M = (m_{ij})_{1 \leq i,j \leq n}$ où $m_{ij}$ est le nombre d'arêtes incidentes à la fois à $v_i$ et $v_j$ (dans le cas simple : $m_{ij} = 1$ si $v_i \sim v_j$, $0$ sinon).

Propriétés : $M$ est carrée, symétrique ($m_{ij} = m_{ji}$), n'a que des zéros sur la diagonale sauf en cas de boucle (un "1" en $(i,i)$ indique une boucle), et est unique une fois l'ordre des sommets fixé.

**Proposition 1.17 (nombre de chaînes de longueur $k$).** _Soit $M$ la matrice d'adjacence de $G$ et $k \in \mathbb{N}^{*}$. Alors le coefficient $(i,j)$ de $M^k$ donne le nombre de chaînes de longueur $k$ allant de $v_i$ à $v_j$.*

**Idée de démonstration (récurrence sur $k$).** Pour $k=1$, c'est la définition même de $M$. Si la propriété est vraie au rang $k$, un chemin de longueur $k+1$ de $v_i$ à $v_j$ se décompose en un chemin de longueur $k$ de $v_i$ à un sommet intermédiaire $v_\ell$, suivi d'une arête de $v_\ell$ à $v_j$ ; le nombre total est donc $\sum_\ell M^k_{i\ell} \cdot M_{\ell j} = (M^{k+1})_{ij}$ par définition du produit matriciel. $\blacksquare$

#### 1.7.2. Matrice d'incidence

Pour $G = (V, E)$, $V = {v_1, \dots, v_n}$, $E = {e_1, \dots, e_m}$, la **matrice d'incidence** $I(G) = (a_{ij})$ est de type $n \times m$ : $$a_{ij} = \begin{cases} 1 & \text{si } v_i \text{ est incident à } e_j \ 2 & \text{si } v_i \text{ est incident à } e_j \text{ et } e_j \text{ est une boucle} \ 0 & \text{sinon} \end{cases}$$

**Source :** Koudi J., _op. cit._, §1.5, p.12-14.

### 1.8. Graphe valué et arbre couvrant minimal

- **Un graphe valué (pondéré)** associe à chaque arête $e$ un poids $p(e) \in \mathbb{R}$.
- La **valeur** d'une chaîne (ou d'un cycle) est la somme des poids de ses arêtes.
- **Un arbre couvrant à coût minimal (minimum spanning tree)** d'un graphe connexe pondéré $G = (V,E)$ est un arbre couvrant dont la somme des poids est minimale.

**Algorithme de Kruskal.** Principe : trier les arêtes par poids croissant, puis ajouter chaque arête à l'arbre en construction si et seulement si elle ne crée pas de cycle avec les arêtes déjà choisies, jusqu'à obtenir $n-1$ arêtes. Complexité : $O(m \log m)$ avec de bonnes structures de données (union-find).

**Algorithme de Prim.** Principe : construire l'arbre progressivement à partir d'un sommet de départ $a$ ; à chaque étape, on ajoute l'arête de poids minimal reliant l'arbre en construction ($W$) au reste du graphe (le _cocycle_ de $W$). Complexité : $O(mn)$ (naïf), $O(m \log n)$ (tas binaire), $O(m + n\log n)$ (tas de Fibonacci).

**Pourquoi ces algorithmes gloutons fonctionnent (idée) :** les deux reposent sur la **propriété de coupe** des MST : pour toute partition de $V$ en deux ensembles non vides, l'arête de poids minimal traversant la coupe appartient à _un_ arbre couvrant minimal. Kruskal l'applique globalement (tri par poids), Prim l'applique localement (coupe $W$ / $V \setminus W$ à chaque itération).

**Source :** Koudi J., _op. cit._, §1.7.1, p.15-17 · Kruskal J., _On the Shortest Spanning Subtree of a Graph..._, 1956 · Prim R.C., _Shortest Connection Networks..._, Bell System Technical Journal, 1957.

---

## 2. Graphes orientés

### 2.1. Définitions

**Un graphe orienté (digraphe) $G = (X, U)$** est déterminé par un ensemble $U$ dont les éléments $u \in U$ sont des couples **ordonnés** de sommets, appelés **arcs**. Si $u = (i,j)$, $i$ est l'**extrémité initiale** et $j$ l'**extrémité terminale** de $u$. On note $m = |U|$ le nombre d'arcs.

- **Boucle :** un arc $u=(i,i)$ dont les extrémités coïncident.
- **Successeurs** de $i$ : $\text{Suv}(i) = {j \mid (i,j) \in U}$.
- **Prédécesseurs** de $i$ : $\text{Pred}(i) = {j \mid (j,i) \in U}$.
- Un digraphe peut être défini de façon équivalente par son **dictionnaire des précédents** (liste des prédécesseurs de chaque sommet) ou son **dictionnaire des suivants**.

### 2.2. Degrés dans un digraphe et matrice booléenne

La **matrice d'adjacence (booléenne)** $M = (a_{ij})$ d'ordre $n$ vérifie $a_{ij} = 1$ si $(x_i, x_j) \in E$, $0$ sinon.

**Proposition 2.8.**

1. _Degré sortant_ $d^+(x_i) = \sum_{j=1}^n a_{ij}$ (somme sur la ligne $i$).
2. _Degré entrant_ $d^-(x_i) = \sum_{j=1}^n a_{ji}$ (somme sur la colonne $i$).
3. $\displaystyle\sum_{i,j} a_{ij} = \sum_i d^+(x_i) = \sum_i d^-(x_i) = |E|$ — l'analogue orienté du lemme des poignées de main : ici pas de facteur 2, car un arc n'est compté qu'une fois (comme sortant pour son origine, comme entrant pour sa destination).
4. La trace $\text{tr}(M)$ est égale au nombre de boucles du graphe.
5. $M^k$ donne, comme dans le cas non orienté, le nombre de chemins de longueur $k$ entre deux sommets.

**Matrice d'incidence** $I = (b_{ij})$ de type $n \times m$ : $$b_{ij} = \begin{cases} 1 & \text{si } x_i \text{ est l'extrémité initiale de } e_j \ -1 & \text{si } x_i \text{ est l'extrémité finale de } e_j \text{ et } e_j \text{ n'est pas une boucle} \ 0 & \text{sinon} \end{cases}$$

**Graphe biparti.** $G=(X,U)$ est **biparti** s'il existe une partition $X = S_1 \sqcup S_2$ telle que chaque arête ait une extrémité dans $S_1$ et l'autre dans $S_2$.

### 2.3. Chemins et circuits

- **Chemin** de $a$ à $b$ : suite alternée sommets/arcs, commençant en $a$, finissant en $b$, où chaque arc est parcouru dans son sens (on ne peut pas prendre un arc "à rebours"). Par convention, tout chemin comporte au moins un arc.
- **Distance** $d(x,y)$ : longueur du plus court chemin de $x$ à $y$ ; $d(x,y) = \infty$ s'il n'existe pas de chemin. **Attention :** dans un digraphe, $d(x,y) \neq d(y,x)$ en général (la distance n'est pas symétrique, contrairement au cas non orienté).
- **Circuit** : chemin dont les sommets de départ et d'arrivée coïncident (l'analogue orienté du cycle).

### 2.4. Plus court chemin — algorithme de Dijkstra

**Contexte.** Proposé par Edsger W. Dijkstra en 1959, il calcule le plus court chemin entre un sommet source et tous les autres, dans un graphe pondéré à **poids positifs** (condition nécessaire à sa correction — avec des poids négatifs, il faut l'algorithme de Bellman-Ford).

**Principe.** On construit un vecteur de coûts $\lambda(1), \dots, \lambda(n)$ initialisé à $\lambda(j) = c_{1j}$ (coût direct depuis la source, $\infty$ si pas d'arc), avec $S = {1}$ (sommets "traités") et $T = {2, \dots, n}$ (sommets restants). À chaque itération : on choisit $i \in T$ minimisant $\lambda(i)$, on le déplace de $T$ vers $S$, puis pour chaque successeur $j \in T$ de $i$, on relâche l'arête (_relaxation_): 
$$\text{si } \lambda(j) > \lambda(i) + \delta(i,j) \text{ alors } \lambda(j) \leftarrow \lambda(i) + \delta(i,j), \quad P(j) \leftarrow i$$

**Pourquoi ça marche (idée de preuve, invariant de boucle) :** à chaque étape, on montre par récurrence que pour tout sommet $i \in S$, $\lambda(i)$ est bien la distance exacte depuis la source. C'est vrai initialement (le sommet source a $\lambda=0$). Quand on ajoute $i^* = \arg\min_{i \in T} \lambda(i)$ à $S$ : tout chemin plus court vers $i$ devrait sortir de $S$ à un moment donné par un sommet $j \in T$, mais alors $\lambda(j) \geq \lambda(i)$ (minimalité) et le reste du chemin ne peut qu'ajouter du poids (poids **positifs** — c'est ici que l'hypothèse est essentielle), donc ce chemin ne peut pas être plus court que $\lambda(i^*)$.

**Présentation de l'Algorithme:**
— $Initialisations$
	— $λ(j)$ = $c_{ij}$ et $P(j) = NIL$ pour $1 ≤ j ≤ n$
	— pour $2 ≤ j ≤ n$ fair :
	Si $c_{ij} < ∞ \text{ }p(j) = 1$
		— $S= 1 \text{ et T} = 2 ; · · · ; n$
— $Itérations$
— Tant que T n’est pas vide, faire :
— Choisir i dans T tel que $λ(i)$ soit le minimum.
— Retirer i de T et l’ajouter à S.
— Pour chaque successeur j de i avec j ∈ T , faire :
	— Si $λ(j) > λ(i) + δ(i, j)$ alors
		$λ(j) = λ(i) + δ(i, j)$
		$P(j) = i$

**Remarque 2.16 :** Dijkstra fonctionne pour tout graphe orienté, avec ou sans circuit. Pour un graphe **sans circuit**, on dispose d'un algorithme plus simple (§2.5).

**Source :** Koudi J., _op. cit._, §2.1.1, p.25-27 · Dijkstra E.W., _A note on two problems in connexion with graphs_, Numerische Mathematik, 1959.

### 2.5. Plus court chemin dans un graphe sans circuit — organisation par niveaux

**Principe.** $G$ orienté est sans circuit **si et seulement si** on peut attribuer à chaque sommet $v$ un rang $r(v)$ tel que pour tout arc $(u,v)$, $r(u) < r(v)$ (c'est un **tri topologique** par niveaux). Algorithme :

1. Attribuer le niveau $0$ à tout sommet sans prédécesseur restant, puis le "barrer" du dictionnaire des précédents des autres sommets.
2. Répéter jusqu'à épuisement (le processus termine car $G$ est sans circuit — s'il y avait un circuit, aucun sommet du circuit n'aurait jamais un dictionnaire de précédents vide).

Une fois les niveaux établis et les sommets numérotés en conséquence, le calcul du plus court chemin se simplifie : on parcourt les sommets dans l'ordre des niveaux (donc des indices) et on améliore le coût de chaque sommet $i$ par $$\lambda'(i) = \min_{j \in \text{Pré}(i)} {\lambda(i), \ \delta(j,i) + \lambda(j)}$$ — chaque sommet n'est traité qu'une fois puisque tous ses prédécesseurs (de niveau strictement inférieur) sont déjà définitivement fixés. C'est un cas particulier de **programmation dynamique** sur un DAG (Directed Acyclic Graph), plus rapide que Dijkstra ($O(n+m)$ contre $O(n^2)$ ou $O(m \log n)$).

**Source :** Koudi J., _op. cit._, §2.1.2, p.28-32.

### 2.6. Ordonnancement — méthode MPM (Méthode des Potentiels Métra)

**Contexte.** La gestion de projet impose des contraintes d'antériorité entre tâches (certaines tâches doivent précéder d'autres). Trois étapes classiques : planification, exécution, contrôle. Trois méthodes usuelles : Gantt, **MPM**, PERT.

**Principe MPM.** On associe un sommet à chaque tâche, un arc $(X,Y)$ si $X$ précède $Y$, puis on ordonnance par niveaux (comme en §2.5). Quantités clés, pour une tâche $X$ de durée $d_X$ :

- **Début au plus tôt** $t_X = \max{t_Y + d_Y : Y \in \text{pred}(X)}$ — on ne peut commencer $X$ qu'une fois toutes ses tâches antérieures terminées.
- **Fin au plus tôt** $= t_X + d_X$.
- **Début au plus tard** $t_X^* = \min{t_Y^* - d_X : Y \in \text{suiv}(X)}$ — le plus tard qu'on puisse commencer $X$ sans retarder le projet.
- **Fin au plus tard** $=$ minimum des débuts au plus tard des tâches déclenchées par $X$.
- **Marge totale** $M_t(X) = t_X^* - t_X$ : retard admissible sur $X$ sans repousser la fin du projet (mais qui peut consommer les marges des tâches suivantes).
- **Marge libre** $M_l(X) = \min{t_Y - d_X - t_X : Y \in \text{suiv}(X)}$ : retard admissible sans affecter le calendrier des tâches suivantes.
- **Tâche critique** : $M_t(X) = 0$. Un **chemin critique** relie le début à la fin du projet en ne passant que par des tâches critiques ; sa longueur donne la durée minimale du projet.

**Source :** Koudi J., _op. cit._, §2.2.1, p.34-36.

---

## 3. Coloration de graphe (rattaché à la partie non orientée, §1.9)

- **Coloration des sommets :** affecter une couleur à chaque sommet de sorte que deux sommets adjacents n'aient jamais la même couleur. Une classe de couleur correspond à un **stable** (sous-ensemble de sommets deux à deux non adjacents).
- **Nombre chromatique** $\chi(G)$ : nombre minimal de couleurs nécessaires.
- **Borne inférieure :** si $G$ contient une clique de taille $x$ (un sous-graphe induit complet $K_x$), alors $\chi(G) \geq x$, car tous les sommets de la clique doivent recevoir des couleurs distinctes deux à deux. Plus généralement, en notant $\omega(G)$ la taille de la clique maximum : $$\omega(G) \leq \chi(G)$$ (l'inégalité peut être stricte : il existe des graphes sans triangle mais de nombre chromatique arbitrairement grand — ex. les graphes de Mycielski).

**Complexité.** Le problème de coloration minimale est **NP-difficile** en général (aucun algorithme polynomial connu, et il n'en existera pas si $P \neq NP$). Il devient cependant polynomial pour des classes particulières de graphes, par ex. les **graphes d'intervalles** : trier les intervalles par borne inférieure croissante, puis affecter glouton (à chaque sommet, la plus petite couleur disponible) donne une coloration **optimale** pour cette classe.

**Théorème des quatre couleurs (Appel & Haken, 1976).** _Le nombre chromatique de tout graphe planaire est au plus 4._ Conjecturée par Francis Guthrie (1852) en coloriant les comtés d'Angleterre, elle n'a été prouvée qu'en 1976, avec l'assistance d'un ordinateur pour énumérer un grand nombre de configurations — à ce jour, aucune preuve n'existe qui n'ait recours à un calcul informatique, ce qui en fait un cas emblématique en philosophie des mathématiques (statut des preuves assistées par ordinateur).

**Source :** Koudi J., _op. cit._, §1.8, p.17-19 · Appel K. & Haken W., _Every Planar Map is Four Colorable_, Illinois J. Math., 1976-1977.

---

## Annexe — feuille de route et liens

- Le lemme des poignées de main (§1.1.3.B) et le théorème d'Euler sur les graphes eulériens (§1.5) partagent la même signature de preuve : un argument de parité / double comptage. Bon réflexe de reconnaissance de motif à garder en tête pour ISSM et Elementals, où la parité et les invariants combinatoires reviennent régulièrement.
- Les algorithmes de Kruskal/Prim (§1.8) et Dijkstra (§2.4) sont tous les deux des algorithmes **gloutons avec preuve par échange/coupe** — un schéma de preuve à comparer, le jour venu, avec les preuves d'optimalité en programmation par contraintes ou en ordonnancement (Feautrier, PLuTo).
- Le graphe MPM (§2.6) et la programmation dynamique sur DAG (§2.5) sont formellement le même objet que les graphes de dépendances utilisés en compilation (analyse de dépendances, ordonnancement d'instructions) — lien direct avec Elementals si un jour le compilateur a besoin d'un ordonnanceur de tâches ou d'une analyse de chemin critique sur le graphe de dépendances des `::` process.