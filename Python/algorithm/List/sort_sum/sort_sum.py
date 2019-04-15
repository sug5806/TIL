import sys
sys.stdin = open("sort_sum.txt", "r")

T = int(input())

def get_pivot_idx(li, start, mid, end):
    idx_li = [start, mid, end]

    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]
    if li[idx_li[1]] > li[idx_li[2]]:
        idx_li[1] , idx_li[2] = idx_li[2], idx_li[1]
    if li[idx_li[0]] > li[idx_li[1]]:
        idx_li[0], idx_li[1] = idx_li[1], idx_li[0]
    
    return idx_li[1]

def quick_sort(li, start, end):
    if start >= end:
        return

    left = start
    right = end
    mid = (start+end)//2
    pivot_idx = get_pivot_idx(li, left, mid, right)
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


# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))
    num_li = list(map(int, input().split()))
    _sum = 0
    

    quick_sort(num_li, 0, len(num_li)-1)

    for i in range(num[1]):
        _sum += num_li[-1-i] - num_li[i]

    print(f'#{test_case} {_sum}')

    
    
