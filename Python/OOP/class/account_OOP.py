import copy

class Account:
    # 클래스 멤버(class member)
    # 모든 객체가 공유한다.
    # 전역변수(global variable)를 대체함
    # Ex) 이자율
    interest_rate = 0.08
    num_of_account = 0


    # 클래스 메서드(class method)
    # 객체가 하나도 없는 상태에서도 호출이 가능!!
    # 전역함수(global variable)를 대체
    # 전역 함수를 대체할 때는 static method를 쓸 수도 있다
    # ***대체 생성자(alternative constructor)

    # static method는 method가 아니라 함수다 : 전역 함수
    # 전역함수를 용납할수 없다 최소한 어딘가에 속해있어야 해서 나온 개념

    @staticmethod
    def func(a, b):
        return a + b


    @classmethod
    def get_num_of_account(cls):
        """
        Account.get_num_of_account() -> integer
        return : 개설된 계좌 수 
        """
        return cls.num_of_account

    # 대체생성자
    @classmethod
    def string_constructor(cls, string):
        data = string.split('_')
        clnt_name = data[0]
        __balance = int(data[1])
        return cls(clnt_name, __balance)


    # 생성자(constructor) : 파이썬은 오직 1개
    # 객체(object)가 생성될때 반드시 한번 호출 된다를 보장
    def __init__(self, clt_name, __balance): # 실행을 할때 무조건 1번은 실행을 하라
        # 인스턴스 멤버(instance member) -> 상태정보 = 데이터
        self.clt_name = clt_name

        # __를 붙이면 비공개! 외부에서 쓰면 안된다.
        self.__balance = __balance
        #self.identification='111111-2222222'

        # 클래스 멤버에 접근하는 방법
        Account.num_of_account += 1
    
    # 인스턴스 메소드(instance method) --> 함수랑 비슷하게 생겼지만 함수랑은 다름
    def deposit(self, money):
        """
        a.deposit(money) -> boolean
        만약에 money > 0 이면 입금 성공!
        아니면 에러 메시지 출력 후 실패
        """
        if money < 0:
            print("입금은 0원 미만은 입금할 수 없습니다.")
            return False

        self.__balance += int(money)
        return True
    
    def withdraw(self, money):
        """
        a.withdraw(money) -> integer
        return : 인출된 돈
        만약 잔고가 모자라면 None 
        """
        if self.__balance < money :
            print("잔액이 부족합니다.")
            return None
        else:
            self.__balance -= money
            return money

    # message passing
    def transfer(self, other, money):
        # 내 객체가 가지고 있는 값
        self.__balance -= money

        # message passing
        # 다른 객체(other)의 상태정보(멤버)를 변경할 때는 반드시 상대 객체가 가진 메서드를 이용한다
        other.deposit(money)
        
    # 객체를 출력할때 주소대신 출력할 것을 만듬
    def __str__(self):
        return f'{self.clt_name} : {self.__balance}'


if __name__ == "__main__":
    # print(f'클래스로 실행 : {Account.interest_rate}')
    # print(f'클래스로 실행 : {Account.get_num_of_account()}')
    # # # 메모리에 객체를 생성
    me = Account('greg',5000)
    your = Account('john', 2000)

    # 이것을 통해 접근이 가능함
    # print(me._Account__balance)
    # print(me.interest_rate)
    # print(me.get_num_of_account())
    # print(Account.func(4, 5))

    # print(type(Account.func))
    # print(type(Account.get_num_of_account))
    # print(type(me))
    # print(type(me.deposit))


    # # 대체 생성자를 이용한 객체의 생성
    # s = 'james_6000'
    # his_acnt=Account.string_constructor(s)
    # print(his_acnt)



    # # instance method 호출하는 방법
    # me.deposit(7000)
    # print(me)

    # # 함수와 메서드의 차이점
    # # 함수 : 같은 입력에 대해 같은 출력을 리턴해야한다.
    # # 메서드 : 입력 + 인스턴스멤버(데이터, 상태정보)에 의존적이다
    #     # 인스턴스멤버 (상태 정보)를 바꾸는 역할을 함
    # res1 = me.withdraw(3000)
    # res2 = your.withdraw(1000)

    # print(res1)
    # print(res2)

    # # 객체 간의 상호 작용
    # # interection by method에 의해 일어나야함!!

    
    # # 절대 해서는 안되는 코드
    # # me.__balance-=1000
    # # your.__balance+=1000
    # # print(me)
    # # print(your)




# 함수와 딕셔너리를 활용하여 account 클래스 제작