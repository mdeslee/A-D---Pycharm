class Stack:
    def __init__(self):
        self.elements = []

    def push(self, element):
        self.elements.append(element)

    def is_empty(self):
        return self.elements == []

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else: self.elements.pop()


s = Stack()
s.push(1)
print(s.elements)

for i in range(10):
    s.pop()

print(s.elements)
