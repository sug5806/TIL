class Node:
    def __init__(self, data = None):
        self.__data = data
        self.__link = None
    
    # 소멸자
    # 객체가 사라지기 전에
    # 반드시 한번 호출 하는것을 보장한다
    def __del__(self):
        print(f"node[{self.__data}] deleted!! ")


    @property
    def data(self):
        return self.__data


    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def link(self):
        return self.__link

    @link.setter
    def link(self, link):
        self.__link = link


class SLinkedList:
    def __init__(self):
        self.head=None
        self.d_size=0
    
    def empty(self):
        if self.d_size == 0:
            return True
        else:
            return False

    def size(self):
        return self.d_size
    
    def add(self, data):
        new_node = Node(data)
        new_node.link = self.head
        self.head = new_node
        self.d_size += 1

    def search(self, target):
        temp = self.head
        while temp:
            if temp.data == target:
                return temp.data
            else : 
                temp = temp.link
        return temp 
        

    def delete(self):
        if self.head == None:
            return
        
        else:
            self.head = self.head.link
            self.d_size -= 1


def show_list(sll):
    cur = sll.head
    for _ in range(sll.size()):
        print(cur.data, end= "  ")
        cur = cur.link

if __name__ == "__main__":
    SLL = SLinkedList()
    SLL.add(1)
    SLL.add(3)
    SLL.add(4)
    SLL.add(5)
    SLL.add(8)
    show_list(SLL)
    print()
    print('*' * 100)

    target = 4
    result = SLL.search(target)
    if result:
        print(f'target = {target}')
        print(f'searched data : {result}')
    else:
        print(f'there is no such data')


    print()