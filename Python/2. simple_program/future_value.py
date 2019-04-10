# 안내 메시지 출력
print("This porgram calculates the future value")
print("of a 10-year investment.")

# 원금의 액수를 입력받음
principal = eval(input("Enter the initial principal: "))

# 연간 이자율을 입력받음
apr = eval(input("Enter the annual interest rate:  "))

# 10번 반복
for i in range(10):
    principal = principal * (1 + apr)

# 출력
print(f"The value in 10 years is: {principal:0.2f}")

