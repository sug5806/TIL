import random

def insert(li):
    n = len(li)
    temp = None
    for i in range(1, n):
        temp = li[i]
        j = i -1
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
        li[j + 1] = temp
        
        

if __name__=="__main__":
    while True:
        num_data=int(input('데이터 개수(종료:0):'))
        if not num_data:
            break
        data=[random.randint(1, 100) for _ in range(num_data)]
        print(data)
        insert(data)
        print(data)