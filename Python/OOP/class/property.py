# modeling : 내가 만들고 있는 프로그램에서 필요한 만큼의 속성만

class Person:
    def __init__(self, name, money):
        self.name = name
        # __를 없애면서 밑에서 property로 선언한 money를 불러오기 위함
        self.money = money


    # property는 오버로딩법칙에서 예외임
    # getter
    @property
    def money(self):
        print("getter executeed")
        return self.__money


    @money.setter
    # property의 함수와 이름이 똑같아야함
    def money(self, money):
        print("setter executeed")
        if money < 0:
            try:
                # 만들어진 money객체가 없는데 객체를 할당하려고 하니 오류가 남
                self.__money = self.__money
            except AttributeError:
                # 객체를 만들면서 초기화 시킴
                self.__money=0
            finally:
                return
        self.__money=money


    # access function
    # getter
    # def get_money():
    #     return self.__money

    # access function
    # setter
    # def set_money(money):
    #     return self.__money = money


if __name__ == "__main__":
    john=Person('john', 5000)
    # 객체의 멤버에 접근 -> getter 수정 -> setter 
    # 을 수행할때는 method function을 이용해야함

    # john.money=-5000 -> 직접접근 절대 금지

    # user 프로그래머는 객체의 멤버처럼 취급하면 된다.
    # 하지만 내부적으로는 getter 혹은 setter를 호출한다.
    # 반드시 메서드를 통해 실제 멤버에 접근
    print(john.money)

    # setter
    john.money = -6000
    print(john.money)