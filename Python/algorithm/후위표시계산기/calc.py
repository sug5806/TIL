from stack import Stack

st = Stack()


# 각 연산자 마다 가중치를 위한 함수
def weight(ch):
    # if ch == "*" or ch == "/":
    #     return 5
    # elif ch == "+" or ch == "-":
    #     return 3
    # elif ch == "(":
    #     return 0
    # elif ch == ")":
    #     return -1
    dic = {'*': 5, '/': 5, '+': 3, '-': 3, '(': 0, ')': -1}
    return dic[ch]


# 연산자에 해당하는 연산 수행
def operator_cal(ch, first_pop, second_pop):
    if ch == "*":
        return second_pop * first_pop
    elif ch == "+":
        return second_pop + first_pop
    elif ch == "-":
        return second_pop - first_pop
    elif ch == "/":
        return second_pop // first_pop


# 중위 표기법을 후위 표기법으로 변환
def make_post(str):
    listExpt = []

    # 혹시나 있을 공백 제거
    for i in str.replace(" ", ""):
        if i.isdigit():
            listExpt.append(i)
            continue
        else:
            # 스택이 비어있으면 푸쉬
            if st.empty():
                st.push(i)
            else:
                # i의 가중치
                cur_wgt = weight(i)
                # 스택 맨위에 있는 원소?의 가중치
                st_wgt = weight(st.peek())
                # i의 가중치가 스택 최상단의 가중치보다 크기나 i가 "("라면
                if cur_wgt > st_wgt or i == "(":
                    st.push(i)
                else:
                    if i == ")":
                        while True:
                            listExpt.append(st.pop())
                            if st.peek() == "(":
                                st.pop()
                                break
                    else:
                        while True:
                            listExpt.append(st.pop())
                            # 스택이 비어있거나 스택 최상단이 "("이거나 i의 가중치가 스택 최상단의 가중치가 더 클경우
                            if st.empty() or cur_wgt > weight(st.peek()):
                                st.push(i)
                                break

    while not st.empty():
        listExpt.append(st.pop())
        if st.empty():
            break

    return listExpt


def post_cal(convert):
    for i in convert:
        if i.isdigit():
            st.push(int(i))
        else:
            st.push(operator_cal(i, st.pop(), st.pop()))
    return st.peek()


str = input("계산식을 적어주세요 : ")
convert = ''.join(make_post(str.strip()))
print(f'후위 표기법 : {convert}')
result = post_cal(convert)
print(f'결과값 : {result}')
