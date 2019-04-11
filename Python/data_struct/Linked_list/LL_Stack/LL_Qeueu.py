class Node:
    def __init__(self, data=None):
        self.__data=data
        self.__next=None

    @property
    def data(self):
        return self.__data
    
    @data.setter
    def data(self, data):
        self.__data=data
    
    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, n):
        self.__next=n

class LQueue:
    def __init__(self):
        self.left = None
        self.right = None
        
    def enqueue(self, data):
        new_node = Node(data)
        if self.empty():
            self.left = new_node
            self.right = new_node
            return
        else:
            self.right.next = new_node
            self.right = new_node

    def empty(self):
        if self.left is None:
            return True
        else:
            return False    


    def dequeue(self):
        if self.empty():
            return
        
        if self.left.next is self.right.next:
            temp = self.left.data
            self.left = None
            self.right = None
            return temp
        else:
            temp = self.left.data
            self.left = self.left.next
            return temp
            
    def peek(self):
        return self.left.data

if __name__ == "__main__":
    q = LQueue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)

    while not q.empty():
        print(q.dequeue(), end='  ')