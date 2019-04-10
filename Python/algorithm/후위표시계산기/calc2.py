from stack import Stack
import re


def get_weight(ch):
    dic = {'*': 100, 'x': 100, '/': 100, '+': 50, '-': 50, '(': 10}
    return dic[ch]


def change_definition(num):
    li_exp = []
    s = Stack()
    # 정의되지 않은 연산자를 넣었을 경우, Error 발생
    p = re.compile('[^ 0-9x\+\-\*\/\(\)]')
    if p.search(num):
        raise
    # 후위표기법으로 변환
    for i in num:
        if i.isdigit():
            li_exp.append(i)
            continue
        else:
            while True:
                # ')'일 때 '('만날 때 까지 뽑아낸다.
                if i == ')':
                    while s.peek() != '(':
                        li_exp.append(s.pop())
                    # '(' 날리기
                    s.pop()
                    break
                # '('이거나 스텍이 비어있을 때, 바로 넣는다.
                elif i == '(' or s.empty():
                    s.push(i)
                    break
                else:
                    # 연산자 비교후, 클 경우만 넣는다.
                    if get_weight(s.peek()) < get_weight(i):
                        s.push(i)
                        break
                    else:
                        # 연산자 비교후, 거나 작을 경우, 위에꺼 뽑아내고 다시 비교
                        li_exp.append(s.pop())
    # 스텍에 남은 연산자 모두 넣는다.
    while not s.empty():
        li_exp.append(s.pop())
    return ''.join(li_exp)


def operate(a, b, ty):
    if ty == '+':
        return a + b
    elif ty == '-':
        return a - b
    elif ty == '*' or ty == 'x':
        return a * b
    else:
        return a // b


def calculation():
    while True:
        num_org = input('식을 입력하세요. (종료 : 0) : ')
        num = num_org.replace(' ', '')
        if num == '0':
            print('계산기를 종료합니다.')
            return True
        else:
            s = Stack()
            try:
                input_num = change_definition(num)
                for i in input_num:
                    if i.isdigit():
                        s.push(int(i))
                    else:
                        b = s.pop()
                        a = s.pop()
                        result = operate(a, b, i)
                        s.push(result)
                print(f'{num_org} = {s.pop()}\n')
            except:
                print('잘못된 수식을 입력하였습니다.\n')
                continue


calculation()