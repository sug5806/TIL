# 해당 위치에 어울리는 값을 '선택'한다


def selection_sort(arr):
    n = len(arr)

    for i in range(0, n-1):
        min_index = i
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        print(arr)


if __name__ == "__main__":
    arr = [7, 2, 5, 12, 3, 10, 1]
    selection_sort(arr)

