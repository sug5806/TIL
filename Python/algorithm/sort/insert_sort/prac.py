# 이미 정렬된 리스트에 적절한 곳에 삽입시키므로 삽입정렬이다.


def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        temp = arr[i]
        j = i - 1
        while j != -1:
            if arr[j] > temp:
                arr[j + 1] = arr[j]
                j -= 1
            else:
                break
        arr[j + 1] = temp


if __name__ == "__main__":
    arr = [7, 2, 5, 12, 3, 10]
    insertion_sort(arr)
    print(arr)
