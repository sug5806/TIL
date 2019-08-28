class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.d_size = 0

    def is_empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size

    def first(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
            return

        new_node.next = self.head
        self.head = new_node
        self.d_size += 1

    def append(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            self.d_size += 1
            return

        self.tail.next = new_node
        self.tail = new_node
        self.d_size += 1

    def add(self, data):
        new_node = Node(data)
        # if self.is_empty():
        #     self.head = new_node
        #     return

        new_node.next = self.head
        self.head = new_node
        self.d_size += 1

    def delete(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        self.d_size -= 1
        return ret_data

    def search(self, target):
        cur = self.head

        while cur:
            if cur.data == target:
                return target
            else:
                cur = cur.next

        return None


def show_list(sll):
    cur = sll.head
    while cur:
        print(f'{cur.data}', end=' ')
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
    show_list(SLL)
    print()
    print('*' * 100)

    target = 2
    result = SLL.search(target)
    if result:
        print(f'target = {target}')
        print(f'searched data : {result}')
    else:
        print(f'there is no such data')
