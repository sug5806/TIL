n = 0 
a = "A" # 출발
b = "B" # 중간
c = "C" # 도착

def hanoi(n, a, b, c):
    if n == 1:
        print("{}번째 원반을 {}로 이동".format(n, c))
        return 

    hanoi(n-1, a, c, b)
    print("{}번째 원반을 {}로 이동".format(n, c))
    hanoi(n-1, b, a, c)

hanoi(3, a, b, c)