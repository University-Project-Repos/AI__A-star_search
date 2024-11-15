# COSC367 Artificial Intelligence - A* Search

Finds the minimum cost path between a start and goal node implementing A* multiple-path pruning

# Instructions

## Requirements

* Python3

## Run

```bash
python3 test_a_star.py
```

# Example

Alternatively, view the [generated output](./results/output.dat):

```bash
Starting nodes: [(1, 3, 9), (3, 2, inf), (3, 5, 0)]
Outgoing arcs (available actions) at starting states:
(1, 3, 9)
  Arc(tail=(1, 3, 9), head=(1, 4, 8), label='E', cost=2)
  Arc(tail=(1, 3, 9), head=(2, 2, 8), label='SW', cost=2)
  Arc(tail=(1, 3, 9), head=(1, 2, 8), label='W', cost=2)
(3, 2, inf)
  Arc(tail=(3, 2, inf), head=(2, 2, inf), label='N', cost=2)
  Arc(tail=(3, 2, inf), head=(3, 3, inf), label='E', cost=2)
  Arc(tail=(3, 2, inf), head=(3, 1, inf), label='W', cost=2)
(3, 5, 0)

Is (1, 1, 5) goal? False
Outgoing arcs (available actions) at (1, 1, 5):
  Arc(tail=(1, 1, 5), head=(1, 2, 4), label='E', cost=2)
  Arc(tail=(1, 1, 5), head=(2, 2, 4), label='SE', cost=2)

Is (1, 7, 2) goal? True
Outgoing arcs (available actions) at (1, 7, 2):
  Arc(tail=(1, 7, 2), head=(2, 7, 1), label='S', cost=2)
  Arc(tail=(1, 7, 2), head=(2, 6, 1), label='SW', cost=2)

Is (3, 6, 5) goal? False
Outgoing arcs (available actions) at (3, 6, 5):
  Arc(tail=(3, 6, 5), head=(2, 6, 4), label='N', cost=2)
  Arc(tail=(3, 6, 5), head=(2, 7, 4), label='NE', cost=2)
  Arc(tail=(3, 6, 5), head=(3, 7, 4), label='E', cost=2)
  Arc(tail=(3, 6, 5), head=(3, 5, 4), label='W', cost=2)
  Arc(tail=(3, 6, 5), head=(3, 6, 9), label='Fuel up', cost=5)

Is (3, 6, 9) goal? False
Outgoing arcs (available actions) at (3, 6, 9):
  Arc(tail=(3, 6, 9), head=(2, 6, 8), label='N', cost=2)
  Arc(tail=(3, 6, 9), head=(2, 7, 8), label='NE', cost=2)
  Arc(tail=(3, 6, 9), head=(3, 7, 8), label='E', cost=2)
  Arc(tail=(3, 6, 9), head=(3, 5, 8), label='W', cost=2)

Starting nodes: [(1, 2, inf)]
Outgoing arcs (available actions) at the start:
  Arc(tail=(1, 2, inf), head=(1, 1, inf), label='W', cost=2)

Is (1, 1, 1) goal? True
Outgoing arcs (available actions) at (1, 1, 1):
  Arc(tail=(1, 1, 1), head=(1, 2, 0), label='E', cost=2)

Starting nodes: [(1, 1, inf), (1, 6, inf), (3, 1, inf)]
Actions:
  N,
  N.
Total cost: 4

Actions:
  E,
  E,
  E,
  NE,
  NE.
Total cost: 10

Actions:
  N,
  NE,
  Fuel up,
  SW,
  SE,
  E,
  E,
  E,
  NE,
  N.
Total cost: 23

Actions:
  W.
Total cost: 2

Actions:
  W,
  W.
Total cost: 4

Actions:
  SE,
  E.
Total cost: 4

There is no solution!

There is no solution!

Actions:
  SE,
  E,
  Fuel up,
  E,
  E,
  E,
  E,
  E,
  E,
  E,
  E,
  SE,
  Fuel up,
  NE,
  E,
  E,
  NE,
  NW,
  N,
  Fuel up,
  SW,
  W,
  W,
  W,
  W,
  W,
  W,
  W,
  W.
Total cost: 67

+-------+
|     XG|
|X XXX* |
| S***  |
+-------+

+--+
|GS|
+--+

+----+
|    |
| SX |
| X*G|
+----+

+------------+
|            |
|            |
|            |
|    S       |
|   *        |
|  *         |
| G          |
|            |
+------------+

+------------+
|  ......    |
|  ......    |
|  ......    |
|  ..S...    |
|  .*....    |
|  *.....    |
| G......    |
|            |
+------------+

+---------------+
|    G*******   |
|XXXXXXXXXXXX*  |
|..******...X*. |
|.*XXXXXX*..X*..|
|.*X.S**X*..X*..|
|.*X....*...X*..|
|.*XXXXXXXXXX*..|
|..**********...|
+---------------+

+---------+
|         |
|    G    |
|         |
+---------+

+-------------+
|         G   |
| S      .*.  |
|         S   |
+-------------+
```
