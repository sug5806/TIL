class MaxHeap:
    MAX = 1024

    def __init__(self):

        self.container = [None for _ in range(MaxHeap.MAX)]
        self.heap_size = 0

    def __get_parent_index(self, cur):
        return cur // 2

    def __get_left_child_index(self, cur):
        return cur * 2

    def __get_right_child_index(self, cur):
        return cur * 2 + 1

    def __get_bigger_child_idx(self, cur):
        left_child_idx = self.__get_left_child_index(cur)

        if left_child_idx > MaxHeap.MAX:
            return None
        elif left_child_idx == MaxHeap.MAX:
            return left_child_idx
        else:
            right_child_idx = self.__get_right_child_index(cur)

            left_child = self.container[left_child_idx]
            right_child = self.container[right_child_idx]

            if left_child > right_child:
                return left_child_idx
            else:
                return right_child_idx

    def is_empty(self):
        if self.heap_size <= 0:
            return True
        else:
            return False

    def is_full(self):
        if self.heap_size == MaxHeap.MAX:
            return True
        else:
            return False

    def push(self, key):
        if self.is_full():
            return
        else:
            self.heap_size += 1
            self.container[self.heap_size] = key
            idx = self.heap_size

            while idx > 1:
                parent_idx = self.__get_parent_index(idx)
                if key > self.container[parent_idx]:
                    self.container[idx], self.container[parent_idx] = \
                    self.container[parent_idx], self.container[idx]

    def pop(self):
        if not self.is_empty():
            ret = self.container[1]
            temp = self.container[self.heap_size]
            ret_idx = 1
            bigger_child_idx = self.__get_bigger_child_idx(ret_idx)

            while bigger_child_idx and temp <






