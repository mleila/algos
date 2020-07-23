import unittest

from ds.graph import AdjacencyList
from algos.graph import tarjan


class TestLinkedList(unittest.TestCase):

    def test_tarjan(self):
        """
        Test the tarjan implementation for finding strongly
        connected components in a DAG
        """
        adjlist = AdjacencyList()

        # create dag
        matrix = [
            # 0  1  2  3  4  5  6  7
            [0, 1, 0, 0, 1, 0, 0, 0],  # 0
            [0, 0, 1, 0, 0, 0, 0, 0],  # 1
            [0, 0, 0, 1, 0, 0, 0, 0],  # 2
            [0, 1, 0, 0, 0, 0, 0, 0],  # 3
            [0, 0, 0, 1, 0, 1, 0, 0],  # 4
            [1, 0, 0, 0, 0, 0, 0, 0],  # 5
            [1, 0, 0, 0, 0, 0, 0, 1],  # 6
            [0, 0, 0, 0, 0, 1, 1, 0],  # 7
        ]
        adjlist.from_matrix(matrix)
        tarjan(adjlist)


if __name__ == '__main__':
    unittest.main()
