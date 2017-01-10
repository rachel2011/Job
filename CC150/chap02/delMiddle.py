class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    def delMiddle(self, node):
        node.val = node.next.val
        node.next = node.next.next

