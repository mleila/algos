from collections import deque
from math import inf

from .basic import LinkedList


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


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

    def __iter__(self):
        return self.array.__iter__()


class BinaryTree:

    def __init__(self, root):
        self.root = Node(val=root)

    def add_node(self, val):
        curr = self.root
        new = Node(val=val)
        while True:
            if val < curr.val:
                if curr.left is None:
                    curr.left = new
                    break
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = new
                    break
                curr = curr.right

    def inorder(self, root):
        if root:
            if (root.left is None) and root.right is None:
                return [root.val]
            left = self.inorder(root.left)
            middle = [root.val]
            right = self.inorder(root.right)
            return left + middle + right
        return []
