# 안내 메시지 출력
print("This porgram calculates the future value")

# 원금의 액수를 입력받음
principal = eval(input("Enter the initial principal: "))

# 기간을 입력받음
period = eval(input("Enter the period: "))

# 연간 이자율을 입력받음
apr = eval(input("Enter the annual interest rate:  "))

# 10번 반복
for _ in range(period):
    principal = principal * (1 + apr)

# 출력
print(f"The value in {period} years is: {principal:0.2f}")

