# 특정 케이스를 만들고 그것에 대해 알고리즘을 만들어서 푼다

def merge(arr, start, mid, end):
    left = start
    right = mid+1
    li = []

    while left <= mid and right <= end:
        if arr[left] <= arr[right]:
            li.append(arr[left])
            left += 1
        else:
            li.append(arr[right])
            right += 1

    # 만약 right가 남아있다면
    while right <= end:
        li.append(arr[right])
        right += 1

    # 만약 left가 남아있다면
    while left <= mid:
        li.append(arr[left])
        left += 1

    arr[start:end+1] = li


def merge_sort(arr, start, end):
    # base case
    if start >= end:
        return

    mid = (start+end)//2

    # divide 를 먼저한다
    merge_sort(arr, start, mid)
    merge_sort(arr, mid+1, end)

    # conquer
    merge(arr, start, mid, end)


if __name__ == "__main__":
    arr = [7, 2, 6, 1, 10, 9, 12, 11, 8]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)
