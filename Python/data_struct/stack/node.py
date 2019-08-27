class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    # 왼쪽 -> 오른쪽으로 진행방향이 아닌
    # 오른쪽 -> 왼쪽으로 진행을 하면 pop을 하기 쉬움
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        ret_data = self.top.data
        self.top = self.top.next
        return ret_data

    def is_empty(self):
        if self.top is None:
            return True
        else:
            return False

    def peek(self):
        return self.top.data


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
