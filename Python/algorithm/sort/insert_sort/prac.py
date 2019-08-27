# 이미 정렬된 리스트에 적절한 곳에 삽입시키므로 삽입정렬이다.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


if __name__ == "__main__":
    arr = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    insertion_sort(arr)
    print(arr)
