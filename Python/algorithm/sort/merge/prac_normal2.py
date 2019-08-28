def merge(arr, start, mid, end):
    left = start
    right = mid + 1

    merged = list()

    while left <= mid and right <= end:
        if arr[left] < arr[right]:
            merged.append(arr[left])
            left += 1
        else:
            merged.append(arr[right])
            right += 1

    while left <= mid:
        merged.append(arr[left])
        left += 1

    while right <= end:
        merged.append(arr[right])
        right += 1

    arr[start:end+1] = merged

def merge_sort(arr, start, end):
    if start >= end:
        return

    mid = (start + end) // 2

    merge_sort(arr, start, mid)
    merge_sort(arr, mid + 1, end)

    merge(arr, start, mid, end)


if __name__ == "__main__":
    arr = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    merge_sort(arr, 0, len(arr) - 1)
    print(f'merge_sort_normal2 : {arr}')
