# 확장할 때 마다 Character 클래스와
# Monster 클래스의 코드가 변한다.

from abc import ABCMeta, abstractmethod
from attack_kind import AttackKindFactory

# abstract class
# parent class
class Character(metaclass=ABCMeta):
    # class member <-- 
    # 전역 변수를 대체할 수 있다.
    def __init__(self, name, hp, power):
        self.name=name
        self.hp=hp
        self.power=power

    # 추상 메서드
    # 바디(body)가 없는 함수
    # 반드시 하나 이상 존재
    # 추상 클래스로 
    @abstractmethod
    def attack(self, other, kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return f'{self.name} : {self.hp}'

# attack, get_damage를 반드시 재정의(메서드 오버라이딩)
# 다형성을 강제
class Player(Character):
    def __init__(self, name='player', hp=100, power=10, *attack_kinds):
        # 부모 클래스의 생성자 --> name , hp, power
        # 위임
        super().__init__(name, hp, power)
        # 새롭게 추가된 멤버
        # 플레이어 한테는 스킬이 있음
        self.skills=[]
        for attack_kind in attack_kinds:
            self.skills.append(attack_kind)

    def attack(self, other, a_kind):
        # for문말고 다른 방식으로 수정할것이 남아 있는듯
        for attack_kind in self.skills:
            if a_kind == attack_kind.get_kind():
                other.get_damage(self.power, a_kind)
                # 다형성 코드
                attack_kind.attack()
        
    def get_damage(self, power, a_kind):
        for attack_kind in self.skills:
            if a_kind == attack_kind.get_kind():
                self.hp -= (power//2)
                return
        self.hp -= power
        

# 추상 클래스(추상클래스인 캐릭터를 상속 받음)
class Monster(Character):
    @classmethod
    def get_monster_kind(cls):
        return cls.__name__.replace('Monster', '')

    def __init__(self, name='Monster', hp=50, power=5):
        super().__init__(name, hp, power)
        self.name = self.get_monster_kind() + name
        self.attack_kind = AttackKindFactory(self.get_monster_kind())
        # AttackKindFactory가 하는 일? 역할은 무엇인가? 중요성을 느끼는 게 중요!
        # 얻을 수 있는 이점은??

    # other = 플레이어
    def attack(self, other, a_kind):
        if a_kind == self.attack_kind.get_kind():
            # 다른 객체의 상태 정보를 변경할 때
            # message passing
            other.get_damage(self.power, a_kind)
            self.attack_kind.attack()

    # 데미지를 입는다
    def get_damage(self, power, a_kind):
        if a_kind == self.attack_kind.get_kind():
            self.hp += power
        else:
            self.hp -= power

    def get_attack_kind(self):
        return self.attack_kind.get_kind()

    @abstractmethod
    def generate_gold(self):
        pass


