# start, end는 인덱스이다
# pivot -> start + end // 2 곧 mid 값
# left와 right가 교차할때까지 반복 pivot과 값이 같아도 멈춤

def quick_sort(li, start, end):

    if start>=end:
        return
    left = start
    right = end
    pivot = li[(start+end)//2]

    while left <= right:
        while li[left] < pivot:
            left += 1
        while li[right] > pivot:
            right -= 1
        
        if left <= right:
            li[left], li[right] = li[right], li[left]
            left += 1
            right -= 1
    
    quick_sort(li, start, right)
    quick_sort(li, left, end)

if __name__ == "__main__":        
import random
import time
def quick_sort(li, start, end):
    if start >= end:
        return
    left=start
    right=end
    pivot=li[(left+right)//2]
    while left <= right:
        while li[left] < pivot:
            left+=1
        while li[right] > pivot:
            right-=1
        
#         if left <= right:
#             li[left], li[right]=li[right], li[left]
#             left+=1
#             right-=1

#     quick_sort(li, start, right)
#     quick_sort(li, left, end)

# if __name__=="__main__":
#    # while True:
#     #    num_data=int(input('데이터 개수(종료:0):'))
#     # 