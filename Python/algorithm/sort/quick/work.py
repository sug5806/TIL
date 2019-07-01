def quick_sort(arr, start, end):

    # 종료조건
    if start >= end:
        return
    left = start
    right = end
    pivot = arr[(left + right) // 2]

    # left 와 right 가 교차하기 전이라면
    while left <= right:
        while arr[left] < pivot:
            left += 1

        while arr[right] > pivot:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr, start, right)
    quick_sort(arr, left, end)


if __name__ == "__main__":
    arr = [7, 2, 5, 12, 3, 10, 4, 19]
    quick_sort(arr, 0, len(arr)-1)
    print(arr)

