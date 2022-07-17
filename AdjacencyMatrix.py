from Interfaces import Graph, List
import numpy as np
import ArrayList
import ArrayQueue
import ArrayStack
"""An implementation of the adjacency list representation of a graph"""

class AdjacencyMatrix(Graph):

    def __init__(self, n : int):
        self.n = n
        self.adj = np.zeros((self.n, self.n), dtype=int)

    def add_edge(self, i : int, j : int):
        self.adj[i][j] = 1


    def remove_edge(self, i : int, j : int):
        if self.adj[i][j] == 1:
            self.adj[i][j] = 0
            return True
        return False


    def has_edge(self, i : int, j: int) ->bool:
        return self.adj[i][j] == 1


    def out_edges(self, i) -> List:
        out_e = ArrayList.ArrayList()
        for k in range(len(self.adj)):
            if self.adj[i][k] == 1:
                out_e.append(k)
        return out_e


    def in_edges(self, i) -> List:
        in_e = ArrayList.ArrayList()
        for k in range (len(self.adj)):
            if self.has_edge(k, i):
                in_e.append(k)
        return in_e


    def bfs(self, r : int):
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
        visited = np.zeros(self.n, dtype=int)
        stack = ArrayStack.ArrayStack()
        stack.push(r)
        while stack.size() > 0:
            cur = stack.pop()
            if visited[cur] == 0:
                traversal.append(cur)
                visited[cur] = 1
            neighbors = self.out_edges(cur)
            for i in reversed(range(neighbors.size())):
                neighbor = neighbors.get(i)
                if visited[neighbor] == 0:
                    stack.push(neighbor)
        return traversal

    def __str__(self):
        s = ""
        for i in range(0, self.n):
            s += "%i:  %r\n" % (i, self.adj[i].__str__())
        return s

'''
g = AdjacencyMatrix(6)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(0, 3)
g.add_edge(2, 4)
g.add_edge(4, 5)
g.add_edge(1, 4)
g.add_edge(4, 5)

print(g.dfs(0,1))

'''

