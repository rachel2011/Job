class stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, data):
        self.items.append(data)

    def peek(self):
        return self.items[len(self.items)-1]

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

s = stack()
print(s.isEmpty())
s.push(4) #[4]
s.push('dog') #[4,dog]
print(s.peek())
s.push(True)
print(s.size())
print(s.isEmpty())
s.push(8.4) #[4,dog,8.4]
print(s.pop()) #[4,dog]
print(s.pop()) #[4]
print(s.size())

