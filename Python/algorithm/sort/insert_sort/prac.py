# 이미 정렬된 리스트에 적절한 곳에 삽입시키므로 삽입정렬이다.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        value = arr[i]
        idx = i - 1
        while idx >= 0 and arr[idx] > value:
            arr[idx + 1] = arr[idx]
            idx -= 1
        arr[idx + 1] = value
        print(arr)


if __name__ == "__main__":
    arr = [7, 2, 5, 12, 3, 10]
    insertion_sort(arr)
    print(arr)
