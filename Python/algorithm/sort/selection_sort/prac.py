# 해당 위치에 어울리는 값을 '선택'한다
# 먼저 최소값을 찾은 후 정렬된 값을 제외한 맨 왼쪽 숫자와 교환한다.

def selection_sort(arr):
    length = len(arr)

    # 파이썬은 range가 n-1까지이다 그러나 끝에서 2번째를 정렬하고 나면 마지막이 남는데
    # 마지막 남은 하나는 정렬을 수행하지 않아도 되므로 n-1을 해준다
    for i in range(length):
        min_idx = i
        for j in range(i + 1, length):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


if __name__ == "__main__":
    arr = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    selection_sort(arr)
    print(arr)
