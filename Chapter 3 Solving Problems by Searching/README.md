# Chapter 3 Implementation Exercises

## Shortest Path

__3.7__ Consider the problem of finding the shortest path between two points on a plane that has convex polygonal obstacles as shown in Figure 3.31. This is an idealization of the problem that a robot has to solve to navigate in a crowded environment.

* __a.__ Suppose the state space consists of all positions (_x_,_y_) in the plane. How many states are there? How many paths are there to the goal?

* __b.__ Explain briefly why the shortest path from one polygon vertex to any other in the scene must consist of straight-line segments joining some of the vertices of the polygons. Define a good state space now. How large is this state space?

* __c.__ Define the necessary functions to implement the search problem, including an `ACTIONS` function that takes a vertex as input and returns a set of vectors, each of which maps the current vertex to one of the vertices that can be reached in a straight line. (Do not forget the neighbors on the same polygon.) Use the straight-line distance for the heuristic function.

* __d.__ Apply one or more of the algorithms in this chapter to solve a range of problems in the domain, and comment on their performance.

## Missionaries and Cannibals

__3.9__ The __missionaries and cannibals__ problem is usually stated as follows. Three missionaries and three cannibals are on one side of a river, along with a boat that can hold one or two people. Find a way to get everyone to the other side without ever leaving a group of missionaries in one place outnumbered by the cannibals in that place. This problem is famous in AI becauseit was the subject of the first paper that approached problem formulation from an analytical viewpoint (Amarel, 1968).

* __a.__ Formulate the problem precisely, making only those distinctions necessary to ensure a valid solution. Draw a diagram of the complete state space.

* __b.__ Implement and solve the problem optimally using an appropriate search algorithm. Is it a good idea to check for repeated states?

* __c.__ Why do you think people have a hard time solving this puzzle, given that the state space is so simple?

## 8-puzzle and Traveling Salesperson

__3.17__ Implement two versions of the `RESULT`(_s_,_a_) function for the 8-puzzle: one that copies and edits the data structure for the parent node _s_ and one that modifies the parent state directly (undoing the modifications as needed). Write versions of iterative deepening depth-first search that uses these functions and compare their performance.

__3.18__ On page 90, we mentioned __iterative lengthening search__, an iterative analog of uniform cost search. The idea is to use increasing limits on path cost. If a node is generated whose path cost exceeds the current limit, it is immediately discarded. For each new iteration, the limit is set to the lowest path cost of any node discarded in the previous iteration.

* __a.__ Show that this algorithm is optimal for general path costs.

* __b.__ Consider a uniform tree with branching factor _b_, solution depth _d_, and unit step costs. How many iterations will iterative lengthening require?

* __c.__ Now consider step costs drawn from the continuous range [_ε_,1], where 0 < _ε_ < 1. How many iterations are required in the worst case?

* __d.__ Implement the algorithm and apply it to instances of the 8-puzzle and traveling salesperson problems. Compare the algorithm's performance to that of uniform-cost search, and comment on your results.

__3.23__ Compare the performance of A* and RBFS on a set of randomly generated problems in the 8-puzzle (with Manhattan distance) and TSP (with MST - see Exercise 3.33) domains. Discuss your results. What happens tothe performance of RBFS when a small random nu,ber is added to the heuristic values in the 8-puzzle domain?

__3.33__ The traveling salesperson problem (TSP) can be solved with the minimum-spanning-tree (MST) heuristic, which estimates the cost of completinga tour, given that a partial tour has already been constructed. The MST cost of a set of cities is the smallest sum of the link costs of any tree that connects all the cities.

* __a.__ Show how this heuristic can be derived from a relaxed version of the TSP.

* __b.__ Show that the MST heuristic dominates straight-line distance.

* __c.__ Write a problem generator for instances of the TSP where cities are represented by random points in the unit square.

* __d.__ Find an efficient algorithm in the literature for constructing the MST, and use it with A* graph search to solve instances of the TSP.

__3.35__ We gave two simple heuristics for the 8-puzzle: Manhattan distance and misplaced tiles. Several heuristics in the literature purport to improve on this - see,  for example, Nilsson (1971), Mostow and Prieditis (1989), and Hansson _et al_. (1992). Test these claims by implementing the heuristics and comparing the performance of the resulting algorithms. 

## Web Page URLs

__3.20__ Write a program that will take as input two Web page URLs and find a path of links from one to the other. What is an appropriate search strategy? Is bidirectional search a good idea? Could a search engine be used toimplement a predecessor function?

## Vacuum-Cleaner World

__3.21__ Consider the vacuum-world problem defined in Figure 2.2.

* __a.__ Which of the algorithms defined in this chapter would be appropriate for this problem? Should the algorithm use tree search or graph search?

* __b.__ Apply your chosen algorithm to compute an optimal sequence of actions for a 3 × 3 world whose initial state has dirt in the three top squares and the agent in the center.

* __c.__ Construct a search agent for the vacuum world, and evaluate its performance in a set of 3 × 3 worlds with probability 0.2 of dirt in each square. Include the search cost as well as path cost in the performance measure, using a reasonable exchange rate.

* __d.__ Compare your best search agent with a simple randomized reflex agent that sucks if there is dirt and otherwise moves randomly.

* __e.__ Consider what would happen if the world were enlarged to _n_ × _n_. How does the performance of the search agent and of the reflex agent vary with _n_?

## A* Graph Search

__3.26__ Devise a state space in which A* using `GRAPH-SEARCH` returns a suboptimal solution with an _h_(_n_) function that is admissable but inconsistent.