class Stack:
# implementating a stack in Python
# A stack should have push, pop, top, empty, and size
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def top(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return self.items == []

#Testing the stack class:
# testStack = Stack()
# testStack.push("a")
# testStack.push("b")
# testStack.push("c")
# testStack.push("d")

# print("Stack Size: ", testStack.size())
# print("Top Item of the Stack: ", testStack.top())
# print("Popping out one element: ", testStack.pop())
# print("Stack Size: ",testStack.size())