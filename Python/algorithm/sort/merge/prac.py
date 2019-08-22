def merge_sort(li):
    n = len(li)
    if n <= 1:
        return

    mid = n // 2

    sub_li1 = li[:mid]
    sub_li2 = li[mid:]
    merge_sort(sub_li1)
    merge_sort(sub_li2)

    idx_li1 = 0
    idx_li2 = 0
    idx_ori_li = 0

    while idx_li1 < len(sub_li1) and idx_li2 < len(sub_li2):
        if sub_li1[idx_li1] <= sub_li2[idx_li2]:
            li[idx_ori_li] = sub_li1[idx_li1]
            idx_li1 += 1
            idx_ori_li += 1

        else:
            li[idx_ori_li] = sub_li2[idx_li2]
            idx_li2 += 1
            idx_ori_li += 1

    while idx_li1 < len(sub_li1):
        li[idx_ori_li] = sub_li1[idx_li1]
        idx_ori_li += 1
        idx_li1 += 1

    while idx_li2 < len(sub_li2):
        li[idx_ori_li] = sub_li2[idx_li2]
        idx_li2 += 1
        idx_ori_li += 1


if __name__ == "__main__":
    # li = [1, 4, 2, 10, 9]
    li = [1, 5, 2, 74, 25, 22, 17, 9, 3, 67, 98, 33, 21, 6]
    merge_sort(li)
    print(f'정렬 완료후 리스트: {li}')
