import random
import time

def merge(li, start, end):
    n = len(li)
    if n <= 1:
        return

    mid = (start+end) // 2
    sub_li1 = li[:mid]
    sub_li2 = li[mid:]

    merge(sub_li1, 0, len(sub_li1))
    merge(sub_li2, 0, len(sub_li2))
    li1 = 0
    li2 = 0
    o_li = 0

    while li1 < len(sub_li1) and li2 < len(sub_li2):
        if sub_li1[li1] < sub_li2[li2]:
            li[o_li] = sub_li1[li1]
            li1 += 1
            o_li += 1
        else:
            li[o_li] = sub_li2[li2]
            li2 += 1
            o_li += 1
    
    while li1 < len(sub_li1):
        li[o_li] = sub_li1[li1]
        li1 += 1
        o_li += 1

    while li2 < len(sub_li2):
        li[o_li] = sub_li2[li2]
        li2 += 1
        o_li += 1



if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        start = time.time()
        print(data)
        merge(data, 0, len(data)-1)
        print("실행 시간 : {:0.2f}".format(time.time()-start))
        print(data)
        
