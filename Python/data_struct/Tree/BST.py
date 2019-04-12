class TreeNode:
    def __init__(self, key):
        self.__key = key
        self.__left = None
        self.__right = None

    def __del__(self):
        print(f'deleted key:{self.__key}')

    @property
    def key(self):
        return self.__key
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

class BST():
    def __init__(self):
        self.root=None

    def get_root(self):
        return self.root
    
    def preorder_traverse(self, cur, func):
        if not cur:
            return

        func(cur)
        self.preorder_traverse(cur.left, func)
        self.preorder_traverse(cur.right, func)

    def insert(self, key):
        new_node = TreeNode(key)
        parent = self.root
        cur = parent

        if self.root == None:
            self.root = new_node
            return

        while True:
            parent = cur
            if new_node.key > cur.key:
                cur = cur.right
                if not cur:
                    parent.right = new_node
                    return
            else:
                cur = cur.left
                if not cur:
                    parent.left = new_node
                    return
                    

    def search(self, target):
        cur = self.root
        while cur:
            if target==cur.key:
                return cur
            elif target < cur.key:
                cur=cur.left
            else:
                cur=cur.right

    def __remove_recursion(self, cur, target):
        # base case 1
        if not cur:
            return None, None
        elif target < cur.key:
            self.left, rem = self.__remove_recursion(cur.left, target)
        elif target > cur.key:
            cur.right, rem = self.__remove_recursion(cur.right, target)
        
        # 지우려는 노드를 찾음
        else:
            # 삭제 노드가 리프노드
            if not cur.left and not cur.right:
                rem=cur
                cur=None
            # 삭제 노드가 자식이 1개중 왼쪽자식이 있을때
            elif not cur.right:
                rem=cur
                cur=cur.left
            # 삭제 노드가 자식이 1개중 오른쪽자식이 있을때
            elif not cur.left:
                rem=cur
                cur=cur.right
            # 자식노드가 둘일 때
            else:
                replace = cur.left
                while replace.right:
                    replace = replace.right
                # 삭제 노드와 대체 노드의 키를 교환
                cur.key, replace.key = replace.key, cur.key
                cur.left, rem = self.__remove_recursion(cur.left, replace.key)
        return cur, None
                            
    def remove(self, target):
        self.root, removed = self._BST__remove_recursion(self.root, target)
        if removed:
            removed.left = removed.right = None
        return removed

if __name__=="__main__":
    print('*'*100)
    bst=BST()

    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(5)
    bst.insert(8)
    bst.insert(10)
    bst.insert(9)
    bst.insert(11)

    f=lambda x: print(x.key, end='  ')

    bst.preorder_traverse(bst.get_root(), f)
    print()
    print('*'*100)

    bst.remove(9)
    bst.remove(8)
    bst.remove(6)

    print(bst.remove(15))

    bst.preorder_traverse(bst.get_root(), f)
    print()
    print('*'*100)

    #print('searched key : {}'.format(bst.search(8).key))




