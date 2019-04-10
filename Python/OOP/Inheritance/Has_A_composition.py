# same life cycle
# strongly coupled

class CPU:
    def __init__(self, manu):
        self.manu=manu

class RAM:
    def __init__(self, giga):
        self.giga = giga


# HAS-A
# 객체의 멤버로서 다른 객체를 포함해서 사용한다.-> composition, aggregation 

# composition
# 객체들의 생성시점이 같음
# 객체들의 소멸시점도 같음
# cpu, ram, computer 강하게 커플링 되어 있다

# 코드 재사용성을 위해서 관계를 구축하는 거라면
# 상속보다는 컴포지션을 사용한다.

class Computer:
    def __init__(self, manu, giga):
        # 멤버에 객체를 할당함
        self.cpu = CPU(manu)
        self.ram = RAM(giga)



if __name__ == "__main__":
    comp1 = Computer("intel", 16)
    comp2 = Computer("AMD", 16)
    print(comp1)
    print(comp2)

    del comp1.cpu
    print(comp1)
    print(comp1.cpu)
    print(comp1.ram)