# traversal (순회)
# 재방문 없이 어떤 자료구조의 모든 데이터(노드) 방문하는 것


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order(node):
    # base case
    if not node:
        return

    # 방문
    print(node.data, end=' ')
    # 왼쪽 자식
    pre_order(node.left_child)
    # 오른쪽 자식
    pre_order(node.right_child)


def in_order(node):
    # base case
    if not node:
        return

    # 왼쪽 자식
    in_order(node.left_child)
    # 방문
    print(node.data, end=' ')
    # 오른쪽 자식
    in_order(node.right_child)


def post_order(node):
    # base case
    if not node:
        return

    # 왼쪽 자식
    post_order(node.left_child)

    # 오른쪽 자식
    post_order(node.right_child)

    # 방문
    print(node.data, end=' ')


class Stack:
    def __init__(self, data):
        self.container = list()
        self.data = data

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


def iter_preorder(cur):
    s = Stack(cur)

    while True:
        while cur:
            print(cur.data, end="  ")
            s.push(cur)
            cur = cur.left_child
        if s.is_empty():
            break

        cur = s.pop()
        cur = cur.right_child


def iter_inorder(cur):
    s = Stack(cur)

    while True:
        while cur:
            s.push(cur)
            cur = cur.left_child
        if s.is_empty():
            break
        cur = s.pop()
        print(cur.data, end="  ")
        cur = cur.right_child


def iter_postorder(cur):
    s1 = Stack()
    s2 = Stack()

    s1.push(cur)
    while not s1.is_empty():
        cur = s1.pop()
        if cur.left:
            s1.push(cur.left_child)
        if cur.right:
            s1.push(cur.right_child)
        s2.push(cur)

    while not s2.is_empty():
        cur = s2.pop()
        print(cur.data, end="  ")


from queue import Queue


def level_order(cur):
    q = Queue()

    q.put(cur)
    while not q.empty():
        cur=q.get()
        print(cur.date, end="  ")
        if cur.left_child:
            q.put(cur.left_child)
        if cur.right_child:
            q.put(cur.right_child)

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

    pre_order(n1)
    print()
    in_order(n1)
    print()
    post_order(n1)
    print()
    print()
    iter_preorder(n1)
    print()
    iter_inorder(n1)
    print()
    iter_postorder(n1)
