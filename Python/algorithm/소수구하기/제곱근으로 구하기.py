n = 5
prime = [2, 3]
count = 0

# 소수는 홀수이므로 홀수만 비교
for n in range(5, 1000 + 1, 2):
    j = 1
    flag = 0
    # n의 제곱근보다 작은 소수에게 나누어지면 소수가 아님
    while (prime[j] * prime[j]) <= n:
        count += 2
        if n % prime[j] == 0:
            flag = 1
            break
        j += 1
    if flag == 0:
        prime.append(n)

print(f'count : {count}')
print(f"소수 : {prime}")
