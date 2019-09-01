def quick_sort(arr, start, end):
    # 종료조건
    if start >= end:
        return

    left = start
    right = end

    pivot = arr[(start + end) // 2]

    while left <= right:
        while pivot > arr[left]:
            left += 1
        while pivot < arr[right]:
            right -= 1

        if left <= right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    quick_sort(arr, start, right)
    quick_sort(arr, left, end)


if __name__ == "__main__":
    arr = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    quick_sort(arr, 0, len(arr) - 1)
    print(arr)
