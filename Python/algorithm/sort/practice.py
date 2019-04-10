import random

def get_pivot_index(li, left, mid, right):
    idx = [left, mid, right]
    if li[idx[0]] > li[idx[1]]:
        idx[0], idx[1] = idx[1], idx[0]
    if li[idx[1]] > li[idx[2]]:
        idx[1], idx[2] = idx[2], idx[1]
    if li[idx[0]] > li[idx[1]]:
        idx[0], idx[1] = idx[1], idx[0]
    
    return idx[1]
    
def quick_sort(li, start, end):
    if start >= end:
        return
    left = start
    right = end
    mid = (start+end)//2
    pivot_idx = get_pivot_index(li, left, mid, right)
    li[mid], li[pivot_idx] = li[pivot_idx], li[mid]

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
        num_data = int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        quick_sort(data, 0, len(data)-1)
        print(data)
        
    



