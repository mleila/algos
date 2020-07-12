from ds import Node, LinkedList


class AdjacencyList:

    def __init__(self):
        self.array = []

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

    def dfs(self):
        visited = [False]*len(self.array)
        stack = [0]
        traversal = []
        while len(stack):
            curr = stack.pop()
            visited[curr] = True
            traversal.append(curr)
            children = self.array[curr].tolist()
            if children == []:
                continue
            for child in children:
                if visited[child]:
                    continue
                stack.append(child)
        return traversal
