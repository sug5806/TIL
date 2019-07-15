"""
MAX_Heap(데이터의 값이 가장 큰게 우선순위가 높다)
1. 완전 이진트리
2. 배열, heapsize-> 데이터의 갯수
3. priority Queue
4. ADT
    - 1. is_empty() -> bool
    - 2. is_full() -> bool
    - 3. push(data) -> None
    - 4. pop() -> 삭제된 원소
    - 5. top() -> 다음번에 pop될 원소

HEAP property
 1. 완전 이진트리인가?
 2. 어떤 노드를 선택해도 키값이 자식보다 크거나 같아야한
"""


class Element:
    def __init__(self, key):
        self.__key = key

    @property
    def key(self):
        return self.__key

    @key.setter
    def key(self, k):
        self.__key = k


class MaxHeap:
    MAX = 1024

    def __init__(self):
        self.__heap_size = 0
        # 클래스 멤버는 클래스명을 앞에 붙인다
        self.__container = [None for _ in range(MaxHeap.MAX)]

    # 내부에서 사용하는 편의 함수이기 때문에 __(던더)를 붙여준다
    def __get_parent_index(self, cur):
        return cur // 2

    def __get_left_child_idx(self, cur):
        return cur * 2

    def __get_right_child_idx(self, cur):
        return cur * 2 + 1

    def __get_bigger_child_idx(self, cur):
        left_child_idx = self.__get_left_child_idx(cur)

        if left_child_idx > self.__heap_size:
            return None
        elif left_child_idx == self.__heap_size:
            return left_child_idx
        else:
            right_child_idx = self.__get_right_child_idx(cur)

            left_child = self.__container[left_child_idx]
            right_child = self.__container[right_child_idx]

            if left_child > right_child:
                return left_child_idx
            else:
                return right_child_idx

    def is_empty(self):
        if self.__heap_size <= 0:
            return True
        else:
            return False

    def is_full(self):
        if self.__heap_size >= MaxHeap.MAX:
            return True
        else:
            return False

    def push(self, key):
        if self.is_full():
            return
        else:
            self.__heap_size += 1
            self.__container[self.__heap_size] = key
            cur = self.__heap_size

            while cur > 1:
                parent_cur = self.__get_parent_index(cur)
                if key > self.__container[parent_cur]:
                    self.__container[cur], self.__container[parent_cur] = self.__container[parent_cur], self.__container[cur]
                    cur = parent_cur
                else:
                    return

    def pop(self):
        if not self.is_empty():
            ret = self.__container[1]
            temp = self.__container[self.__heap_size]
            cur_idx = 1
            bigger_child_idx = self.__get_bigger_child_idx(cur_idx)

            while bigger_child_idx and temp < self.__container[bigger_child_idx]:
                self.__container[cur_idx] = self.__container[bigger_child_idx]
                cur_idx = bigger_child_idx
                bigger_child_idx = self.__get_bigger_child_idx(cur_idx)

            self.__container[cur_idx] = temp
            self.__heap_size -= 1
            return ret

    def top(self):
        if self.is_empty():
            raise IndexError("The heap is empty")
        ret = self.__container[1]
        return ret


if __name__ == "__main__":
    heap = MaxHeap()
    heap.push(10)
    heap.push(7)
    heap.push(12)
    heap.push(3)

    while True:
        if not heap.is_empty():
            print(heap.pop(), end=" ")
        else:
            break
