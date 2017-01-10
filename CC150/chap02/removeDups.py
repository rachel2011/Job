class Node:
    def __init__(self, x):
        self.val = x
        self.next = None


class solution:
    # Given 1->1->2->3->3, return 1->2->3.
    # literate through the linkedlist,add each element to a hash table,
    # when find duplictae element,remove the element and then continue iterating.
    # O(N)
    def removeDups1(self, head):
        dic = {}
        current = head
        previous = None
        while current is not None:
            if current.val in dic:
                previous.next = current.next
            else:
                dic[current.val] = True
                previous = current
            current = current.next
        return head

    def removeDups2(self, head):
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head

    # Given 1->2->3->3->4->4->5, return 1->2->5.
    # Given 1->1->1->2->3->1->1, return 2->3.
    def removeDups2(self, head):
        dummy = pre = Node(0)
        dummy.next = head
        while head and head.next:
            if head.val == head.next.val:
                while head and head.next and head.val == head.next.val:
                    head = head.next
                head = head.next
                pre.next = head
            else:
                pre = pre.next
                head = head.next
        return dummy.next






