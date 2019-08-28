def bubble_sort(arr):
    length = len(arr)

    for i in range(length):
        flag = False
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                flag = True
        if not flag:
            return
        print(f'{i}회차 정렬: {arr}')


if __name__ == "__main__":
    # arr = [1, 4, 2, 10, 9]
    arr = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    bubble_sort(arr)
    print(f'정렬 완료후 리스트: {arr}')
