# 최대 공약수 구하기

def GCD(a, b):
    i = min(a, b)
    while True:
        if a % i == 0 and b % i == 0:
            return i
        i -= 1
    return None

print(f'1와 5의 최대 공약수 : {GCD(1, 5)}')
print("{}와 {}의 최대 공약수 : {}".format(3, 6, GCD(3, 6)))
print("{}와 {}의 최대 공약수 : {}".format(60, 24, GCD(60, 24)))
print("{}와 {}의 최대 공약수 : {}".format(81, 27, GCD(81, 27)))
    