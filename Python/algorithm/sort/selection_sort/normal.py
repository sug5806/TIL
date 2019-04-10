import random
import time

def selection_sort(li):
    n = len(li)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if li[min_idx] > li[j]:
                min_idx = j    
        li[i] , li[min_idx] = li[min_idx], li[i]



if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        start = time.time()
        data=[random.randint(1, 100) for _ in range(num_data)]
        end = time.time()
        elips = end - start
        #print(data)
        selection_sort(data)
        #print(data)
        print("{:0.2f}".format(elips))  