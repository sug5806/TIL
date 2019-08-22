def bubble_sort(li):
    length = len(li)

    print(f'원본 리스트: {li}')
    for i in range(length):
        flag = False
        # 밑에서 j + 1을 하므로 -1을 해준다.
        for j in range(length - i - 1):
            if li[j] > li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
                flag = True
        if not flag:
            return
        print(f'{i}회차 정렬 실행후 리스트: {li}')


if __name__ == "__main__":
    # li = [1, 4, 2, 10, 9]
    li = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    bubble_sort(li)
    print(f'정렬 완료후 리스트: {li}')
