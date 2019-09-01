class Heap:
    def __init__(self):
        self.container = [None]

    def __swap(self, parent, idx):
        self.container[parent], self.container[idx] = \
            self.container[idx], self.container[parent]

    def parent(self, idx):
        return idx // 2

    def left_child(self, idx):
        left = idx * 2
        if left > len(self.container) - 1:
            return None
        return left

    def right_child(self, idx):
        right = idx * 2 + 1
        if right > len(self.container) - 1:
            return None
        return right

    def insert(self, data):
        self.container.append(data)
        i = len(self.container) - 1
        # root로 올때까지 반복
        while i > 1:
            parent = self.parent(i)
            if self.container[parent] < data:
                self.__swap(parent, i)
                i = parent
            else:
                break

    def delete(self):
        ret_data = self.container[1]
        self.__swap(1, len(self.container) - 1)
        self.container.pop()
        self.heapify(1)
        return ret_data

    def heapify(self, idx):
        left_idx = self.left_child(idx)
        right_idx = self.right_child(idx)
        flag = False

        if left_idx is None and \
                right_idx is None:
            return

        if left_idx is not None and \
                self.container[left_idx] > self.container[idx]:
            max = left_idx
        else:
            max = idx

        if right_idx is not None and \
                self.container[right_idx] > self.container[max]:
            max = right_idx

        if max != idx:
            self.__swap(max, idx)
            flag = True

        if not flag:
            return

        self.heapify(max)

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
        heap.delete()
        heap.show_heap()
