# design패턴중 adapter pattern이 적용됨
# 내부에서 사용하는 구현체가 있는데
# 상호 작용하는 객체와 인터페이스가 맞지 않을 때
# 인터페이스를 맞춰주는 클래스

class Queue:
    def __init__(self):
        # 내부 구현체
        self.container = list()

    def empty(self):
        if self.container:
            return True
        else: return False

    # wrapping function
    def enqueue(self, data):
        self.container.append(data)

    def dequeue(self):
        return self.container.pop(0)

    def peek(self):
        return self.container[0]

    def get_length(self):
        return len(self.container)

    def ret_Queue(self):
        return self.container


if __name__ == "__main__":
    Q = Queue()
    for i in range(1, 6):
        print("{}번째 원소 삽입".format(i))
        Q.enqueue(i)
        print("{}번째 원소 :  {}".format(i, Q.peek()))

    while not Q.empty():
        print(Q.dequeue(), end="  ")
    

    