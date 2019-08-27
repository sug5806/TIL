class Queue:
    def __init__(self):
        self.container = list()

    def empty(self):
        if self.container:
            return False
        else:
            return True

    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def queue_size(self):
        return len(self.container)

    def peek(self):
        return self.container[-1]


if __name__ == "__main__":
    Q = Queue()
    for i in range(1, 6):
        print("{}번째 원소 삽입".format(i))
        Q.enqueue(i)
        print("{}번째 원소 :  {}".format(i, Q.peek()))

    print('*' * 100)
    print(f'Q.dequeue() 실행: {Q.dequeue()}')
    print(f'Q.dequeue() 실행: {Q.dequeue()}')
    print(f'원소 {10} 삽입')
    Q.enqueue(10)
    print(f'Q.dequeue() 실행: {Q.dequeue()}')
    print(f'Q.dequeue() 실행: {Q.dequeue()}')
    print(f'Q.dequeue() 실행: {Q.dequeue()}')
    print(f'Q.dequeue() 실행: {Q.dequeue()}')

    # while not Q.empty():
    #     print(f'Q.dequeue() 실행: {Q.dequeue()}')