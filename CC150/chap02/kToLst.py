class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class solution:
    def ktolast(self, head, k):

        fast = slow = head
        for i in range(k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow.val




