import random as rd

def get_pivot_index(li, start, mid, end):
    
    idx_li = [start, mid, end]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]
    if li[idx_li[1]] > li[idx_li[2]]:
        idx_li[1], idx_li[2] = idx_li[2], idx_li[1]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]

    return idx_li[1]
     
def quick_sort(li, start, end):
    if start >= end:
        return

    left = start
    right = end
    mid = (start+end)//2
    pivot_idx = get_pivot_index(li, left, mid, right)
    li[pivot_idx], li[mid] = li[mid], li[pivot_idx]

    while left <= right:
        while li[left] < li[pivot_idx]:
            left += 1
        while li[right] > li[pivot_idx]:
            right -= 1


        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1

    quick_sort(li, start, right)
    quick_sort(li, left, end)


if __name__ == "__main__":
    while True:
        num_data = int(input("데이터 개수(종료:0) : "))
        if not num_data:
            break

        data = [rd.randint(1,100) for _ in range(num_data)]
        print(data)
        quick_sort(data, 0, len(data)-1)
        print(data)