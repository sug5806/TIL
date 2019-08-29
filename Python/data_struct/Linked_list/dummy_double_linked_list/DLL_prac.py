class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList:
    def __init__(self):
        self.head = Node("head")
        self.tail = Node("tail")
        self.d_size = 0
        self.head.next = self.tail
        self.tail.previous = self.head

    def size(self):
        return self.d_size

    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def add_first(self, data):
        new_node = Node(data)

        new_node.previous = self.head
        new_node.next = self.head.next

        self.head.next.previous = new_node
        self.head.next = new_node

        print(f'{data} 추가 완료')

        self.d_size += 1

    def add_last(self, data):
        new_node = Node(data)

        new_node.next = self.tail
        new_node.previous = self.tail.previous

        self.tail.previous.next = new_node
        self.tail.previous = new_node

        print(f'{data} 추가 완료')

        self.d_size += 1

    def insert_after(self, data, node):
        if node is None:
            print("노드가 존재하지 않습니다.")
            return

        new_node = Node(data)

        new_node.next = node.next
        new_node.previous = node

        node.next = new_node
        node.next.previous = new_node

        print(f'{data} 추가 완료')

        self.d_size += 1

    def insert_before(self, data, node):
        if node is None:
            print("노드가 존재하지 않습니다.")
            return

        new_node = Node(data)

        new_node.next = node
        new_node.previous = node.previous

        node.previous = new_node
        node.previous.next = new_node

        print(f'{data} 추가 완료')

        self.d_size += 1

    def search_forward(self, target):
        cur = self.head.next
        while cur:
            if cur.data == target:
                return cur
            else:
                cur = cur.next

        return None

    def search_backward(self, target):
        cur = self.tail.previous
        while cur:
            if cur.data == target:
                return cur
            else:
                cur = cur.previous
        return None

    def delete_first(self):
        if self.empty():
            print("연결된 노드가 없습니다.")
            return

        self.head.next = self.head.next.next
        self.head.next.previous = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            print("연결된 노드가 없습니다.")
            return

        self.tail.previous = self.tail.previous.previous
        self.tail.previous.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        if node is None:
            print('삭제할 노드가 없습니다.')
            return

        node.next.previous = node.previous
        node.previous.next = node.next

        self.d_size -= 1


if __name__ == "__main__":
    dll1 = DoublyLinkedList()

    dll1.add_last(1)
    dll1.add_last(3)
    dll1.add_last(5)
    dll1.add_last(7)
    dll1.add_last(9)

    # print(dll1.search_forward(7))

    dll1.insert_after(4, dll1.search_forward(1))
    dll1.insert_before(2, dll1.search_forward(5))
    dll1.insert_before(10, dll1.search_forward(9))

    # show_list(dll1)
    # 얘가 4를 가리키고 있으므로 None으로 해주지 않으면 delete 메시지가 뜨지 않음
    searched_data = dll1.search_forward(4)
    if searched_data:
        print(f"searched data : {searched_data.data}")
    else:
        print("there is no data")

    dll1.delete_first()
    dll1.delete_last()
    dll1.delete_last()
    dll1.delete_last()
    dll1.delete_node(searched_data)
    searched_data = None
    # show_list(dll1)

    print("*" * 100)
