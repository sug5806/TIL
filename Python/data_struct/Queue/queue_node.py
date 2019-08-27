class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        if self.head is None:
            return True
        else:
            return False

    def enqueue(self, data):
        new_node = Node(data)

        if self.is_empty():
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        ret_data = self.head.data
        self.head = self.head.next
        return ret_data

    def peek(self):
        return self.head.data


if __name__ == "__main__":
    Q = Queue()

    Q.enqueue(1)
    Q.enqueue(3)
    Q.enqueue(5)
    Q.enqueue(7)
    Q.enqueue(9)

    print(Q.dequeue())
    print(Q.dequeue())

    Q.enqueue(11)

    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
    print(Q.dequeue())
