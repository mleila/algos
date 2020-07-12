import unittest

from ds import Node, LinkedList
from algos.graph import AdjacencyList


class TestLinkedList(unittest.TestCase):

    def test_len(self):
        ll = LinkedList(head=Node(1))
        ll.insert_node(Node(5))
        assert len(ll) == 2

    def test_print(self):
        ll = LinkedList(head=Node(1))
        ll.insert_node(Node(5))
        assert str(ll) == '5->1->None'

    def test_delete(self):
        ll = LinkedList(head=Node(1))
        ll.insert_node(Node(5))
        ll.delete_node(val=5)
        assert str(ll) == '1->None'
        ll.insert_node(Node(7))
        ll.insert_node(Node(8))
        assert str(ll) == '8->7->1->None'
        ll.delete_node(1)
        assert str(ll) == '8->7->None'
        ll.delete_node(8)
        ll.delete_node(7)
        assert len(ll) == 0

    def test_list(self):
        ll = LinkedList(head=Node(1))
        ll.insert_node(Node(5))
        ll.insert_node(Node(7))
        assert ll.tolist() == [7, 5, 1]


class TestAjacencyList(unittest.TestCase):

    def __init__(self):
        self.adjlist = AdjacencyList()

    def test_dfs(self):
        """Test Depth First Search Implementation."""
        matrix = [
            # 0  1  2  3  4  5
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        self.adjlist.from_matrix(matrix)
        assert adjlist.dfs() == [0, 1, 3, 5, 2, 4]


if __name__ == '__main__':
    unittest.main()
