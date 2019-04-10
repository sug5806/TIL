class Person:
    def __init__(self, name, money):
        self.name = name
        self.money = money

    @property
    def money(self):
        print("money getter executed")
        return self.__money

    @money.setter
    def money(self, money):
        print("setter executed")
        if money < 0:
            self.__money = 0
        else:
            self.__money = money


if __name__ == "__main__":
    peo = Person("john", 5000)
    print(peo.name, peo.money)
    