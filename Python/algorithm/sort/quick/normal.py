import random as rd

def get_pivot_index(li, start, mid, end):
    """
    get_pivot_index(li, start, mid, end) -> index
    리스트의 맨 처음 값, 가운데 값, 마지막 값 중에서
    중간 값을 가진 인덱스를 반환한다
    """
    idx_li=[start, mid, end]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]
    if li[idx_li[1]] > li[idx_li[2]]:
        idx_li[1], idx_li[2] = idx_li[2], idx_li[1]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]

    return idx_li[1]
     

def quick_sort_sub(li, start, end):
    # base case
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

    quick_sort_sub(li, start, right)
    quick_sort_sub(li, left, end)

if __name__ == "__main__":
    while True:
        num_data = int(input("데이터 개수(종료:0) : "))
        if not num_data:
            break

        data = [rd.randint(1,100) for _ in range(num_data)]
        print(data)
        quick_sort_sub(data, 0, len(data)-1)
        print(data)