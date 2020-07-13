from collections import deque

from numpy import inf

from ds import Node, LinkedList


class AdjacencyList:

    def __init__(self):
        self.array = []
        self.inf = inf

    def from_matrix(self, matrix: list):
        """Convert adjacency matrix to adjacency list."""
        # init the array
        self.array = []
        rows = len(matrix)
        self.array = [LinkedList() for row in range(rows)]
        for idx, row in enumerate(matrix):
            ll = self.array[idx]
            for vert_indx, vertex in enumerate(row):
                if vertex:
                    ll.insert_node(Node(val=vert_indx))

    def bfs(self):
        """Run BFS."""
        # create Queue
        q = deque()

        # book keeping
        visited = [False]*len(self.array)
        parent = [None]*len(self.array)
        distance = [self.inf]*len(self.array)
        traversal = []

        # initialize source
        q.appendleft(0)
        distance[0] = 0
        parent[0] = 0
        visited[0] = True

        while len(q):
            curr = q.pop()
            traversal.append(curr)
            distance[curr] = distance[parent[curr]] + 1
            children = self.array[curr].tolist()
            for child in children:
                if visited[child]:
                    continue
                visited[child] = True
                parent[child] = curr
                q.appendleft(child)
        return traversal

    def dfs(self):
        visited = [False]*len(self.array)
        stack = [0]
        traversal = []
        visited[0] = True
        while len(stack):
            curr = stack.pop()
            traversal.append(curr)
            children = self.array[curr].tolist()
            for child in children:
                if visited[child]:
                    continue
                visited[child] = True
                stack.append(child)
        return traversal

    def __str__(self):
        s = ''
        for indx, ll in enumerate(self.array):
            s += f'Node({indx})->{ll.tolist()}\n'
        return s

    def __repr__(self):
        return str(self)
