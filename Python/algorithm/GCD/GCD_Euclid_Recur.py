# 유클리드 알고리즘으로 최대공약수 구하기

def GCD_Euclid_Re(a, b):
    if b == 0:
        return a
    else:
        return GCD_Euclid_Re(b, a%b)

print(GCD_Euclid_Re(1, 5))
print(GCD_Euclid_Re(3, 6))
print(GCD_Euclid_Re(60, 24))
print(GCD_Euclid_Re(81, 27))

