"""
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.minValStack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.getMin() == None or x <= self.getMin():
            self.minValStack.append(x)
        self.stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        value = self.stack.pop()
        if value == self.getMin():
            self.minValStack.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.minValStack) == 0:
            return None
        return self.minValStack[-1]


        # Your MinStack object will be instantiated and called as such:
        # obj = MinStack()
        # obj.push(x)
        # obj.pop()
        # param_3 = obj.top()
        # param_4 = obj.getMin()