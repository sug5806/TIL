def binary_serarch(a, n, data):
    low = 0
    high = n - 1
    while low <= high:
        mid = low + (high - low) // 2
        if a[mid] == data:
            return mid
        elif a[mid] < data:
            low = mid + 1
        else:
            high = mid - 1
    return -1


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    n = len(a)
    search = 7

    print(f'{search}의 index는: {binary_serarch(a, n, 7)}')
