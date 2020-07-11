"""Basic data structures from scratch."""


class Node:

    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __repr__(self):
        return print(f'Node({self.val})')


class LinkedList:
    """Singly Linked List."""

    def __init__(self, head: Node):
        self.head = head
        self.count = 0 if head is None else 1

    def insert_node(self, node: Node):
        temp = self.head
        self.head = node
        self.head.next = temp
        self.count += 1

    def delete_node(self, val: int):
        if self.is_empty():
            raise NameError('List is empty')

        node = self.head
        prev = None
        while node:
            if node.val == val:
                if prev is None:
                    self.head = node.next
                else:
                    prev.next = node.next
                self.count -= 1
                return True
            prev = node
            node = node.next

        return False

    def __str__(self):
        n = self.head
        s = ''
        while n:
            s += f'{n.val}->'
            n = n.next
        s += 'None'
        return s

    def __repr__(self):
        return str(self)

    def is_empty(self):
        return self.count == 0

    def __len__(self):
        return self.count

    def tolist(self):
        lst = []
        n = self.head
        while n:
            lst.append(n.val)
            n = n.next
        return lst
