class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def peek(self):
        return self.head.data

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        ret_data = self.head.data
        self.head = self.head.next
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
