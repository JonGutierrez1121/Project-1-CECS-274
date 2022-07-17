"""An implementation of the adjacency list representation of a graph"""
from Interfaces import Graph, List
import numpy as np
import copy
import ArrayList
import ArrayStack
import ArrayQueue
import algorithms as alg

class AdjacencyList(Graph):
    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros(n, object)
        for i in range(self.n):
            self.adj[i] = ArrayList.ArrayList()

    def add_edge(self, i : int, j : int):
        if not self.adj[i].contains(j):
            self.adj[i].append(j)
            # alg.quick_sort(self.adj[i])

    def remove_edge(self, i : int, j : int):
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                self.adj[i].remove(k)
                return True
        return False

    def has_edge(self, i : int, j: int) ->bool:
        for k in range(self.adj[i].size()):
            if self.adj[i].get(k) == j:
                return True
        return False

    def out_edges(self, i) -> List:
        return self.adj[i]

    def in_edges(self, i) -> List:
        in_edge = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.has_edge(k, i):
                in_edge.append(k)
        return in_edge

    def bfs(self, r: int):
        traversal = ArrayList.ArrayList()
        visited = np.zeros(self.n)
        queue = ArrayQueue.ArrayQueue()
        traversal.append(r)
        visited[r] = 1
        queue.add(r)
        while queue.size() > 0:
            cur = queue.remove()
            neighbors = self.out_edges(cur)
            for i in range(neighbors.size()):
                neighbor = neighbors.get(i)
                if visited[neighbor] == 0:
                    traversal.append(neighbor)
                    visited[neighbor] = 1
                    queue.add(neighbor)
        return traversal

    def dfs(self, r : int):
        traversal = ArrayList.ArrayList()
        seen = np.zeros(self.n)
        stack = ArrayStack.ArrayStack()
        stack.push(r)
        while stack.size() > 0:
            cur = stack.pop()
            if not seen[cur]:
                traversal.append(cur)
                seen[cur] = True
            neighbors = self.out_edges(cur)
            for neighbor in reversed(neighbors):
                if not seen[neighbor]:
                    stack.push(neighbor)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i,%r\n" % (i, self.adj[i].__str__())
        return s





g = AdjacencyList(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(0, 4)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g)
print("BFS(0)", g.bfs(0))

# g = AdjacencyList(12)
# g.add_edge(0, 1)
# g.add_edge(0, 9)
# g.add_edge(1, 0)
# g.add_edge(1, 2)
# g.add_edge(1, 10)
# g.add_edge(1, 11)
# g.add_edge(2, 1)
# g.add_edge(2, 3)
# g.add_edge(2, 11)
# g.add_edge(3, 2)
# g.add_edge(3, 4)
# g.add_edge(4, 3)
# g.add_edge(4, 5)
# g.add_edge(4, 11)
# g.add_edge(5, 4)
# g.add_edge(5, 6)
# g.add_edge(6, 5)
# g.add_edge(6, 7)
# g.add_edge(6, 11)
# g.add_edge(7, 6)
# g.add_edge(7, 8)
# g.add_edge(7, 10)
# g.add_edge(8, 7)
# g.add_edge(8, 9)
# g.add_edge(9, 0)
# g.add_edge(9, 8)
# g.add_edge(9, 10)
# g.add_edge(10, 1)
# g.add_edge(10, 7)
# g.add_edge(10, 9)
# g.add_edge(10, 11)
# g.add_edge(11, 2)
# g.add_edge(11, 4)
# g.add_edge(11, 6)
# g.add_edge(11, 10)
#
# print(g)
# print("BFS(0):", g.bfs(0))
# print("Expected: [0, 1, 9, 2, 10, 11, 8, 3, 7, 4, 6, 5]")
# print("\nDFS(0):", g.dfs(0))
# print("Expected: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]")

