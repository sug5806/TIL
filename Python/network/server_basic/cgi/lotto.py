#! /home/martine/.pyenv/shims/python3
# 로또 예상 번호 5 게임 출력하기
import random as rd

# 로또는 1게임당 1~45 사이의 정수 중 6개를 중복없이 뽑아야 한다.
# 1. 랜덤하게 숫자 뽑아서 채우기
numbers = []
while len(numbers)<6:
    number = rd.randint(1, 45)
    if number not in numbers:
        numbers.append(number)

# 1-1 리스트 대신 set사용
numbers = ()
while len(numbers) < 6:
    number = rd.randint(1,45)
    numbers.add(number)

# 2. 원본을 만들어 두고 랜덤하게 몇개 뽑는 방법
original_numbers= [x for x in range(1,46)]
numbers = rd.sample(original_numbers, 6)

rd.shuffle(original_numbers)
# 처음부터 6개
numbers = original_numbers[:6]
# 뒤에서 6개 뽑기
numbers = original_numbers[-6:]

print("Contest-type: text/html\n")
print("<html><head><title>CGI테스트</title></head></html><body>" + str(numbers) + "<br></body>")

# 랜덤 숫자 뽑기 -> 랜덤 문자열 -> UUID