# circular queue (원형 큐)
# - 1. 크기가 정해져 있는 배열(list)
# - 2. head, tail
# - 3 - 1. 비어있는 큐를 어떻게 표현할 것이냐?
# - 3 - 2. Out of Index 를 어떻게 할 것이냐?

# head와 tail을 같은곳에 둔다 => h와 t가 같으면 empty이다
# --> 큐가 가득 찬것과 비어있는 것을 어떻게 구분할 것이냐?
# tail은 값을 넣은 후에 움직인다. -> 마지막 데이터의 다음을 가리키고 있다.
# -> t + 1 == h이면 full이다

# ADT -> Abstract Data Type (추상 자료형)


class CQueue:
    MAXSIZE = 10

    def __init__(self):
        self.__container = [None for _ in range(CQueue.MAXSIZE)]
        self.__head = 0
        self.__tail = 0

    def is_empty(self):
        if self.__head == self.__tail:
            return True
        return False

    def is_full(self):
        next = self.__step_forward(self.__tail)
        if next == self.__head:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            raise Exception("The queue is full")
        self.__container[self.__tail] = data
        # tail은 마지막 데이터의 다음을 가리킨다
        self.__tail = self.__step_forward(self.__tail)

    def dequeue(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        ret = self.__container[self.__head]
        self.__head = self.__step_forward(self.__head)
        return ret

    def peek(self):
        if self.is_empty():
            raise Exception("The queue is empty")
        return self.__container[self.__head]

    # 편의 함수
    def __step_forward(self, x):
        x += 1
        if x >= CQueue.MAXSIZE:
            x = 0
        return x


if __name__ == "__main__":
    cq = CQueue()

    for i in range(9):
        cq.enqueue(i)
        for j in range(10):
            print(cq._CQueue__container[j], end="  ")

        print()

    # for i in range(5):
    #     print(cq.dequeue(), end="  ")
    #
    # # print()
    # # for i in range(10):
    # #     print(cq._CQueue__container[i], end="  ")
    # print()
    #
    #
    # for i in range(8, 14):
    #     cq.enqueue(i)
    #     # print(cq._CQueue__container[i], end="  ")
    # print()
    #
    #
    #
    # print()
    # while not cq.is_empty():
    #     print(cq.dequeue(), end="  ")
    #
    # print()
    # for i in range(10):
    #     print(cq._CQueue__container[i], end="  ")
