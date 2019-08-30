class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.top = new_node
            return

        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None

        ret_data = self.top.data
        self.top = self.top.next
        return ret_data


if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(3)
    stack.push(5)
    stack.push(7)
    stack.push(9)

    print(stack.pop())
    print(stack.pop())

    stack.push(4)
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
    print(stack.pop())
