class Heap:
    def __init__(self):
        self.container = [None]
        self.heap_size = 0

    def __get_parent(self, idx):
        return idx // 2

    def __get_left_child(self, idx):
        left = idx * 2
        if left > self.heap_size:
            return None

        return left

    def __get_right_child(self, idx):
        right = idx * 2 + 1
        if right > self.heap_size:
            return None

        return right

    def __swap(self, parent, child):
        self.container[parent], self.container[child] = \
            self.container[child], self.container[parent]

    def insert(self, data):
        self.container.append(data)

        temp_idx = len(self.container) - 1
        while temp_idx > 1:
            parent = self.__get_parent(temp_idx)

            if data > self.container[parent]:
                self.__swap(temp_idx, parent)
                temp_idx = parent
            else:
                return

    def delete(self):
        ret_data = self.container[1]
        self.__swap(len(self.container) - 1, 1)
        self.container.pop()
        self.__heapify(1)
        return ret_data

    def __heapify(self, idx):
        left_idx = self.__get_left_child(idx)
        right_idx = self.__get_right_child(idx)
        flag = False

        if left_idx is None and \
                right_idx is None:
            return

        if left_idx is not None and \
                self.container[left_idx] > self.container[idx]:
            change_idx = left_idx
        else:
            change_idx = idx

        if right_idx is not None and \
                self.container[right_idx] > self.container[change_idx]:
            change_idx = right_idx

        if change_idx != idx:
            self.__swap(change_idx, idx)
            flag = True

        if not flag:
            return

        self.__heapify(change_idx)

    def show_heap(self):
        print(self.container)


if __name__ == "__main__":
    heap = Heap()
    heap.insert(10)
    heap.insert(12)
    heap.insert(5)
    heap.insert(8)
    heap.insert(26)
    heap.insert(1)
    heap.insert(2)
    heap.insert(7)
    heap.insert(9)

    heap.show_heap()
    print()

    for _ in range(9):
        ret_data = heap.delete()
        # print(f'삭제한 데이터: {ret_data}')
        heap.show_heap()
        # print()
