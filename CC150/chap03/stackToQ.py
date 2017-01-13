#use second stack to reverse the orderof its element(by popping the s1 and pushing the element to s2)


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack =[], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        self.outStack.pop()


    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return self.outStack == [] and self.inStack == []
    # add a "move()" method to simplify code:
    # it moves all elements of the "inStack" to the "outStack" when the "outStack" is empty.
    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())