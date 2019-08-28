def merge_sort(a):
    length = len(a)
    # print(a)
    if length <= 1:
        return

    mid = length // 2
    sub_li1 = a[mid:]
    sub_li2 = a[:mid]
    merge_sort(sub_li1)
    merge_sort(sub_li2)

    g1_idx = 0
    g2_idx = 0
    ori_idx = 0

    g1_len = len(sub_li1)
    g2_len = len(sub_li2)

    while g1_idx < g1_len and g2_idx < g2_len:
        if sub_li1[g1_idx] < sub_li2[g2_idx]:
            a[ori_idx] = sub_li1[g1_idx]
            ori_idx += 1
            g1_idx += 1

        else:
            a[ori_idx] = sub_li2[g2_idx]
            ori_idx += 1
            g2_idx += 1

    while g1_idx < g1_len:
        a[ori_idx] = sub_li1[g1_idx]
        ori_idx += 1
        g1_idx += 1

    while g2_idx < g2_len:
        a[ori_idx] = sub_li2[g2_idx]
        ori_idx += 1
        g2_idx += 1

    print(a)


if __name__ == "__main__":
    # d = [6, 8, 3, 9, 10, 1, 2, 4, 7, 5]
    d = [5, 1, 3, 2, 7]
    merge_sort(d)
    print(d)
