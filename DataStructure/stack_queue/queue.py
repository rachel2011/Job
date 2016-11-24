class queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

q = queue()
print(q.isEmpty())
q.enqueue(4) #[4]
q.enqueue('dog') #[dog,4]
q.enqueue(True) #[True.dog,4]
print(q.size())
print(q.isEmpty())
q.enqueue(8.4) #[8.4,True,4,dog]
print(q.dequeue()) #[8.4,True,4]
print(q.dequeue()) #[8.4,True]
print(q.size())