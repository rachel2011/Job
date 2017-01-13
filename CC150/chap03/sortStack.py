# Use s2 as cache. Pop a node A from s1, pop top of s2 back to
# s1 until A < top of s2, then push A onto s2. Repeat until all nodes
# are poped from s1 to s2. Now s2 is sorted in decending order (biggest
# in head). Finally we pop all nodes from s2 back to s1.
def sortStack(unsortedStack):
    # O(n^2) time O(n) space
    sortedStack = []
    while unsortedStack:
        cur = unsortedStack.pop()
        while sortedStack and sortedStack[-1] > cur:
            unsortedStack.append(sortedStack.pop())
        sortedStack.append(cur)
    return sortedStack

stack = [5,7,10,12,3,6]
print sortStack(stack)