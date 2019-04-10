class My_Stack:
    def __init__(self):
        self.container = list()

    def empty(self):
        """
        s.empty() -> bool
        만약 스택에 요소가 있다면 False
        아니면 True
        """
        if not self.container:
            return True
        else:
            return False

    def push(self, data):  # 내가 구현한 push는 어댑터 / 기존에 있는 append를 컨테이너
        """
        s.push(data) -> None
        리스트의 append 함수를 이용해서 구현
        """
        self.container.append(data)

    def pop(self):
        """
        s.pop() -> data
        스택의 맨 꼭대기 값을 반환하면서 삭제
        리스트의 pop 함수를 이용해서 구현
        """
        return self.container.pop()

    def peek(self):
        """
        s.peek() -> data
        스택의 맨 꼭대기 값을 반환만 함
        """
        return self.container[-1]

