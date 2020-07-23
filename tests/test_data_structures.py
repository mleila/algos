import unittest

from ds import Node, LinkedList
from ds.graph import AdjacencyList, BinaryTree, Node as graphNode


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

    def test_from_matrix(self):
        adjlist = AdjacencyList()

        matrix = [
            # 0  1  2  3  4  5
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        adjlist.from_matrix(matrix)

    def test_dfs(self):
        """Test Depth First Search Implementation."""
        adjlist = AdjacencyList()

        # case 1
        matrix = [
            # 0  1  2  3  4  5
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0]
        ]
        adjlist.from_matrix(matrix)
        assert adjlist.dfs() == [0, 1, 3, 5, 2, 4]

        # case 2
        matrix = [
            # 0  1  2  3  4  5
            [0, 1, 1, 0, 0, 1],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0]
        ]
        adjlist.from_matrix(matrix)
        assert adjlist.dfs() == [0, 1, 3, 2, 4, 5]

    def test_bfs(self):
        """"Test Breadth First Search Implementation."""
        adjlist = AdjacencyList()

        # case 1
        matrix = [
            # 0  1  2  3  4  5
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 0]
        ]
        adjlist.from_matrix(matrix)
        assert adjlist.bfs() == [0, 2, 1, 4, 3, 5]


class test_binary_tree(unittest.TestCase):

    def test_add_node(self):
        tree = BinaryTree(0)
        nodes = [1, 2, 3, 4]
        for n in nodes:
            tree.add_node(n)

    def test_inorder(self):
        tree = BinaryTree(4)
        nodes = [3, 2, 5]
        for n in nodes:
            tree.add_node(n)

        in_order = [2, 3, 4, 5]
        assert in_order == tree.inorder(tree.root)


if __name__ == '__main__':
    unittest.main()
