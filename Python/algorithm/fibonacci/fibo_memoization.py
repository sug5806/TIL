# Memoization --> 넓은 의미로는 dynamic programming라 할수도 있음
# 이미 기억해 놓은것을 기준으로 접근횟수를 현저히 줄임

def make_fibo():
    cache = [0, 1]
    def inner(n):
        if len(cache) < n:
            cache.append(inner(n-2) + inner(n-1))
        return cache[n-1]
    return inner

if __name__ == "__main__":
    fibo=make_fibo()
    for i in range(1, 11):
        print(fibo(1), end= " ")