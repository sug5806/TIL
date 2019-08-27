class Stack:
    def __init__(self):
        self.container = []
        self.top = None

    def push(self, data):
        self.container.append(data)

    def pop(self):
        return self.container.pop()

    def is_empty(self):
        if not self.container:
            return True
        else:
            return False

    def peek(self):
        return self.container[-1]


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    while not stack.is_empty():
        print(stack.pop())
