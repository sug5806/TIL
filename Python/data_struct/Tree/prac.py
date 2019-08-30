# traversal (순회)
# 재방문 없이 어떤 자료구조의 모든 데이터(노드) 방문하는 것
from queue import Queue


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None


def pre_order(tree_node):
    if tree_node is None:
        return

    print(tree_node.data, end=' ')
    pre_order(tree_node.left_child)
    pre_order(tree_node.right_child)


def in_order(tree_node):
    if tree_node is None:
        return

    in_order(tree_node.left_child)
    print(tree_node.data, end=' ')
    in_order(tree_node.right_child)


def post_order(tree_node):
    if tree_node is None:
        return

    post_order(tree_node.left_child)
    post_order(tree_node.right_child)
    print(tree_node.data, end=' ')


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


def iter_preorder(cur):
    s = Stack()

    while True:
        while cur:
            print(cur.data, end=" ")
            s.push(cur)
            cur = cur.left_child
        if s.is_empty():
            break

        cur = s.pop()
        cur = cur.right_child


def iter_inorder(cur):
    s = Stack()

    while True:
        while cur:
            s.push(cur)
            cur = cur.left_child
        if s.is_empty():
            break
        cur = s.pop()
        print(cur.data, end=" ")
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
        s2.push(cur.data)

    while not s2.is_empty():
        cur = s2.pop()
        print(cur.data, end=" ")


def level_order(cur):
    q = Queue()

    q.put(cur)
    while not q.empty():
        cur = q.get()
        print(cur.date, end=" ")
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
    iter_preorder(n1)
    print()
    # iter_inorder(n1)
    print()
    # iter_postorder(n1)
