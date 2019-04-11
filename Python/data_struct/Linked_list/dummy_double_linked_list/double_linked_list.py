class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__previous = None
        self.__next = None


    def __del__(self):
        print(f"deleted data : [{self.__data}]")

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def previous(self):
        return self.__previous

    @previous.setter
    def previous(self, link):
        self.__previous = link

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, link):
        self.__next = link




class DoubleLinkedList:
    def __init__(self):
        # 더미의 생성시점은 DLL이 만들어 질때
        # head, tail, d_size
        self.head = Node()
        self.tail = Node()
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

    # insert 계열
    # 리스트의 맨 앞(HEAD의 오른쪽)에 데이터 추가
    def add_first(self, data):
        new_node = Node(data)
        
        # new_node를 연결
        new_node.next = self.head.next
        new_node.previous = self.head

        # 기존 node에 new_node를 연결
        self.head.next.previous = new_node
        self.head.next = new_node

        self.d_size += 1
        
    # 리스트의 맨 뒤(TAIL의 왼쪽)에 데이터 추가
    def add_last(self, data):
        new_node = Node(data)

        # new_node를 연결
        new_node.next = self.tail
        new_node.previous = self.tail.previous

        # 기존 node에 new_node를 연결
        self.tail.previous.next = new_node
        self.tail.previous = new_node

        self.d_size += 1

    # 특정 리스트의 오른쪽에 데이터 추가
    def insert_after(self, data, node):
        if node == None:
            print("노드가 존재안함")
            return
        new_node = Node(data)

        # new_node를 연결
        new_node.previous = node
        new_node.next = node.next

        # 기존 node에 new_node 연결
        node.next.previous = new_node
        node.next = new_node

        print(f"{data} 추가 완료")

        self.d_size += 1

    # 특정 리스트의 왼쪽에 데이터 추가
    def insert_before(self, data, node):
        if node == None:
            print("노드가 존재안함")
            return
        new_node = Node(data)

        # new_node를 연결
        new_node.next = node
        new_node.previous = node.previous

        # 기존 node에 new_node 연결
        node.previous.next = new_node
        node.previous = new_node
        print(f"{data} 추가 완료")

        self.d_size += 1


    # Search 계열
    def search_forward(self, target):
        temp = self.head.next
        while temp is not self.tail:
            if temp.data == target:
                return temp
            else:
                temp = temp.next
        return None


    def search_backward(self, target):
        temp = self.tail.previous
        while temp is not self.tail:
            if temp.data == target:
                return temp
            else:
                temp = temp.previous
        return None
        

    # Delete 계열
    def delete_first(self):
        if self.empty():
            print("connected Node is nothing")
            return 
        self.head.next = self.head.next.next
        self.head.next.previous = self.head

        self.d_size -= 1

    def delete_last(self):
        if self.empty():
            print("nothing connected Node")
            return 
        self.tail.previous = self.tail.previous.previous
        self.tail.previous.next = self.tail

        self.d_size -= 1

    def delete_node(self, node):
        if self.empty():
            print("nothing connected Node")
            return
        node.previous.next = node.next
        node.next.previous = node.previous

        self.d_size -= 1



    # 편의 함수 - gennerator
    def traverse(self, start=True):
        # 리스트의 첫 데이터부터 순회!
        if start:
            temp = self.head.next    
            while temp is not self.tail:
                yield temp
                temp = temp.next
        else: 
            # 리스트의 마지막 데이터부터 순회!
            temp = self.tail.previous
            while temp is not self.head:
                yield temp
                temp = temp.previous

def show_list(d_list):
    g = d_list.traverse()
    for node in g:
        print(node.data, end=" ")
    print()          

if __name__ == "__main__":
    dll1 = DoubleLinkedList()
    # dll2 = DoubleLinkedList()
    dll1.add_last(1)
    dll1.add_last(3)
    dll1.add_last(5)
    dll1.add_last(7)
    dll1.add_last(9)
    
    # print()

    # dll2.add_last(1)
    # dll2.add_last(3)
    # dll2.add_last(5)
    # dll2.add_last(7)
    # dll2.add_last(9)
    # show_list(dll2)

    dll1.insert_after(4,dll1.search_forward(3))
    dll1.insert_before(2,dll1.search_forward(3))

    show_list(dll1)
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
    show_list(dll1)

    print("*"*100)



