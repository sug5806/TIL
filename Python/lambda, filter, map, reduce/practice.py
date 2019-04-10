from functools import reduce


li = [5, 2, 3, 1, 8, 10]
def pred(x):
    return x % 2

li.sort(key=pred, reverse=True)

li.sort(key= lambda x : x % 2)

#
li = [1, -2, 6, -21, 34, 29, -92, 7]
li2 = list(filter(lambda x : x>0, li))
print(f"filter 양수반환 {li2}")

# 양수만 뽑아서 각 원소를 제곱한다음 리스트로 반환
li2 = list(map(lambda x :x**2 , filter(lambda x : x>0, li)))
print(f'map 양수인 각 원소를 제곱하여 출력 : {li2}')

# 하나씩 뽑아서 계산
li3 = reduce(lambda a, b : a+b, li)
print(f'reduce li에서 하나씩 뽑아서 계산 : {li3}')
print(f'sume 위와 같음 : {sum(li)}')


li = ['a', 'a', 'b', 'c', 'e', 'q', 't', 't', 'w', 'c']

word = reduce(lambda dic, b : dic.update({b:dic.get(b,0)+1}) or dic, li, {})
print(word)