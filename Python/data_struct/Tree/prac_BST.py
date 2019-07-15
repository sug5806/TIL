class TreeNode:
    def __init__(self, key=None):
        self.__key = key
        self.__left = None
        self.__right = None

    # getter
    @property
    def key(self):
        return self.__key

    # setter
    @key.setter
    def key(self, key):
        self.__key = key

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


class BST:
    def __init__(self):
        self.__root = None

    @property
    def root(self):
        return self.__root

    def preorder(self, cur):
        if not cur:
            return

        print(cur.key, end=" ")
        self.preorder(cur.left)
        self.preorder(cur.right)

    def insert(self, key):
        new_node = TreeNode(key)

        cur = self.__root
        if not cur:
            self.__root = new_node
            return

        while True:
            parent = cur
            if key < cur.key:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
            else:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return

    def search(self, target):
        cur = self.__root
        while cur:
            if cur.key == target:
                return cur
            elif target <= cur.key:
                cur = cur.left
            else:
                cur = cur.right

        return None
        # return cur

    def delete(self, target):
        # 1. 삭제할 노드가 리프노드일 경우
        # print('진입')
        self.__root = self.__delete_recursion(self.__root, target)

    # 재귀 함수
    def __delete_recursion(self, cur, target):
        # delete와 remove의 차이
        #   delete : 삭제한 데이터를 반환하지 않음
        #   remove : 삭제한 데이터를 반환함
        # 탈출 조건
        if not cur:
            return None

        elif target < cur.key:
            cur.left = self.__delete_recursion(cur.left, target)

        elif target > cur.key:
            cur.right = self.__delete_recursion(cur.right, target)

        # target == cur.key
        else:
            # 1. 삭제 노드가 리프 노드인 경우
            if not cur.left and not cur.right:
                cur = None
            # 2. 삭제 노드의 자식이 한개인 경우
            # 왼쪽 자식만 있는 경우
            elif not cur.right:
                cur = cur.left

            # 오른쪽 자식만 있는 경우
            elif not cur.left:
                cur = cur.right

            # 3. 삭제 노드의 자식이 둘인 경우
            else:
                rep = cur.left
                while rep.right:
                    rep = rep.right
                # 삭제 노드와 대체 노드의 키를 교환
                cur.key, rep.key = rep.key, cur.key

                cur.left = self.__delete_recursion(cur.left, rep.key)

        return cur


if __name__ == '__main__':
    bst = BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(8)
    bst.insert(2)
    bst.insert(4)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    bst.preorder(bst.root)
    print()
    # bst.insert(5)
    bst.preorder(bst.root)
    print()
    ret = bst.search(9)
    if ret:
        print(f'{ret.key} is found')
    else:
        print("No Such data")

    # 삭제노드가 리프노드 일 때
    bst.delete(11)
    bst.preorder(bst.root)
