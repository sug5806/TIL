def fibo_recursion(n):
    # base case
    if n<= 1:
        return 0
    elif n==2:
        return 1
    
    return fibo_recursion(n-2) + fibo_recursion(n-1) # 꼬리 재귀 --> while문으로 치환가능

def fibo_iteration(n):
    a = 0
    b = 1
    for _ in range(n-1):
        a, b = b, a+b
    return a


if __name__=="__main__":
    for i in range(1, 11):
        print(fibo_recursion(i), end=" ")
        print(fibo_iteration(i), end=" ")