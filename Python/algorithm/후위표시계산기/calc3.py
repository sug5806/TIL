stack = Stack()
collected_list = []  # 입력값을 모아놓은 리스트
back_list = []       # 후위표기로 변환된 리스트

def is_input() :
   # 사용자로부터 입력값을 받는 함수
   global collected_list
   while True:
       button_input = input("한자리 숫자와 부호를 입력해주세요 : ")
       if button_input in ["+", "-", "*", "/", "(", ")", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9",\
                           -1, -2, -3, -4, -5, -6, -7, -8, -9] :
           collected_list.append(button_input)
       elif button_input == '=':
           break
   return collected_list

def weight(a) :
   # 가중치를 더하는 함수
   if a == '*' or a == '/' :
       return 4
   elif a == '+' or a == '-' :
       return 3
   elif a == '(' :
       return 2
   elif a == ')' :
       return 1

def back_ward(char):
   #후위표기법으로 변환하는 함수
   global back_list
   for i in range(len(char)) :
       if char[i].isdigit() :
           back_list.append(char[i])
       elif stack.empty() or char[i] == '(' :
           stack.push(char[i])
       elif char[i] == ')' :
           while stack.peek() != '(' :
                 back_list.append(stack.pop())
           stack.pop()
       elif weight(char[i]) > weight(stack.peek()) :
           stack.push(char[i])
       else :
           while weight(char[i]) <= weight(stack.peek()) :
               back_list.append(stack.pop())
               if stack.empty() :
                   stack.push(char[i])
                   break
               elif weight(char[i]) > weight(stack.peek()) :
                   stack.push(char[i])
                   break
   while stack.empty() == False :
       back_list.append(stack.pop())

def calculate(char) :
   #후위표기법 계산하는 함수
   is_input()
   back_ward(collected_list)
   for i in range(len(char)) :
       if char[i].isdigit() :
           stack.push(char[i])
       else :
           b = int(stack.pop())
           a = int(stack.pop())
           if char[i] == '+' :
               c = a + b
               stack.push(c)
           elif char[i] == '-' :
               c = a - b
               stack.push(c)
           elif char[i] == '*':
               c = a * b
               stack.push(c)
           elif char[i] == '/':
               c = a // b
               stack.push(c)
   return stack.pop()

print(calculate(back_list))