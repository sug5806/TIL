class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.d_size = 0

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def first(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.d_size += 1

    def append(self, data):
        new_node = Node(data)
        if self.empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.d_size += 1

    def delete_first(self):
        self.head = self.head.next
        self.d_size -= 1

    def delete_target(self, target):
        cur = self.head
        pre = self.head
        while cur:
            if cur.data == target:
                pre.next = cur.next
                self.d_size -= 1
                return
            pre = cur
            cur = cur.next
        return None

    def search(self, target):
        cur = self.head
        while cur:
            if target == cur.data:
                return cur.data
            cur = cur.next

        return None


def show_list(sll):
    cur = sll.head
    while cur:
        if cur is None:
            return None
        print(cur.data)
        cur = cur.next


if __name__ == "__main__":
    SLL = SingleLinkedList()
    SLL.append(1)
    SLL.append(3)
    SLL.first(4)
    SLL.first(5)
    SLL.append(8)

    # SLL.add(1)
    # SLL.add(3)
    # SLL.add(5)
    # SLL.add(7)
    # SLL.add(9)

    show_list(sll=SLL)
    print()
    print('*' * 100)

    target = 3
    result = SLL.search(target)
    if result:
        print(f'target = {target}')
        print(f'searched data : {result}')
    else:
        print(f'there is no such data')

    print()
    SLL.delete_target(3)
    show_list(sll=SLL)
