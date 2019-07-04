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
