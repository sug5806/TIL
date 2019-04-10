from single_linked_list import Node, SLinkedList


class Queue:
    def __init__(self):
        self.sll = SLinkedList()

    def enqueue(self, data):
        self.sll.add(data)

    def dequeue(self):
        temp1 = self.sll.head
        temp2 = self.sll.head
        #print(temp1.data)
        #print(temp2.data)
        cnt = 0
        while temp1.link != None:
            cnt += 1
            temp1 = temp1.link
            #print(temp1.data)

        #print("%"*100)
        for _ in range(cnt-1):
            temp2 = temp2.link
            #print(temp2.data)

        ret = temp1.data
        temp2.link = temp1.link
        print("dequeue {}".format(ret))
        return 


# def show_list(arg):
#     que.sll.show_list(arg)


if __name__ == "__main__":
    que = Queue()

    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.enqueue(4)
    que.enqueue(5)

    #print(que.sll.head.data)
    que.dequeue()
    que.dequeue()
    que.dequeue()
    que.dequeue()
    print("*"*100)