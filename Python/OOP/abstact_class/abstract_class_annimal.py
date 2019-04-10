from abc import ABCMeta, abstractmethod # abstract base class

# 추상클래스
class Animal(metaclass=ABCMeta):
    # 추상메서드 -> 파생클래스에서 반드시 구현해야함
    @abstractmethod
    def say(self):
        pass

# 파생클래스에서 추상 메소드를 구현하지 않으면
# 파생클래스 또한 추상클래스가 됨

# 추상클래스의 장점 : 1. 구현을 깜빡한 사용자 프로그래머에게 구현을 하도록 유도할수있음

# 객체에서의 interface -> 유저가 사용할 수있는 behavior or operation의 목록
# 유저프로그래머들은 공개되어있는 operation만 가져다 쓰면 됨
# 인터페이스를 공개를한다 : 사용자들은 공개된 메소드만으로도 충분히 사용할 수 있고 추상클래스를 상속받는 사람들에게는 다형성을 제공함

class Lion(Animal):
    # pass 
    def say(self):
        print("어흥")


class Duck(Animal):
    def say(self):
        print("꽥꽥")
        
class Dog(Animal):
    def say(self):
        print("멍멍")

class Deer(Animal):
    def say(self):
        print("사슴")

if __name__ == "__main__":
    animals = []
    animals.extend((Lion(), Duck(), Deer(), Dog(), Duck()))

    #ani=Animal()
    #ani.say()

    # 다형성 코드 -> 객체에따라 결과가 다름
    for animal in animals:
        animal.say()