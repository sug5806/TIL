# traversal (순회)
# 재방문 없이 어떤 자료구조의 모든 데이터(노드) 방문하는 것


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.container = list()

    def is_empty(self):
        if not self.container:
            return True
        else:
            return False

    def push(self, data):
        self.container.append(data)

    def pop(self):
        ret = self.container.pop()
        return ret

    def peek(self):
        return self.container[-1]


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, tree_node):
        new_node = Node(tree_node)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        ret_node = self.head.data
        self.head = self.head.next
        return ret_node


# 전위 순회
def pre_order(tree_node):
    if tree_node is None:
        return

    print(tree_node.data, end=" ")
    pre_order(tree_node.left_child)
    pre_order(tree_node.right_child)


# 중위 순회
def in_order(tree_node):
    if tree_node is None:
        return

    in_order(tree_node.left_child)
    print(tree_node.data, end=" ")
    in_order(tree_node.right_child)


# 후위 순회
def post_order(tree_node):
    if tree_node is None:
        return

    post_order(tree_node.left_child)
    post_order(tree_node.right_child)
    print(tree_node.data, end=" ")


# 전위 순회 반복문
def iter_pre_order(cur):
    s = Stack()

    while True:
        while cur:
            s.push(cur)
            print(cur.data, end=" ")
            cur = cur.left_child

        if s.is_empty():
            break

        cur = s.pop()
        cur = cur.right_child


# 중위 순회 반복문
def iter_in_order(cur):
    stack = Stack()

    while True:
        while cur:
            stack.push(cur)
            cur = cur.left_child

        if stack.is_empty():
            break

        cur = stack.pop()
        print(cur.data, end=" ")
        cur = cur.right_child


# 후위 순회 반복문
def iter_post_order(cur):
    stack1 = Stack()
    stack2 = Stack()

    stack1.push(cur)

    while not stack1.is_empty():
        cur = stack1.pop()

        stack2.push(cur)
        if cur.left_child:
            stack1.push(cur.left_child)

        if cur.right_child:
            stack1.push(cur.right_child)

    while not stack2.is_empty():
        cur = stack2.pop()
        print(cur.data, end=" ")


def level_order(cur):
    q = Queue()

    q.enqueue(cur)

    while not q.is_empty():
        cur = q.dequeue()

        print(cur.data, end=" ")
        if cur.left_child:
            q.enqueue(cur.left_child)

        if cur.right_child:
            q.enqueue(cur.right_child)


if __name__ == '__main__':
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n7 = TreeNode(7)

    n1.left_child = n2
    n1.right_child = n3
    n2.left_child = n4
    n2.right_child = n5
    n3.left_child = n6
    n3.right_child = n7

    print(f'전위 순회 재귀: ', end="")
    pre_order(n1)
    print()
    print(f'중위 순회 재귀: ', end='')
    in_order(n1)
    print()
    print(f'후위 순회 재귀: ', end='')
    post_order(n1)
    print()
    print()
    print(f'전위 순회 반복: ', end='')
    iter_pre_order(n1)
    print()
    print(f'중위 순회 반복: ', end='')
    iter_in_order(n1)
    print()
    print(f'후위 순회 반복: ', end='')
    iter_post_order(n1)
    print()
    print(f'레벨 순회 반복: ', end='')
    level_order(n1)
    print()
