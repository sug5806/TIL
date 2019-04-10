# 확장할 때 마다 Character 클래스와
# Monster 클래스의 코드가 변한다.

from abc import ABCMeta, abstractmethod
from attack_kind import AttackKindFactory

# 추상클래스
# parent class
class Character(metaclass=ABCMeta):
    # class member <-- composition
    # 전역 변수를 대체할 수 있다.
    #attacks = Attacks()
    def __init__(self, name, hp, power):
        self.name = name
        self.hp = hp
        self.power = power

    # 추상 메서드
    # 바디가 없는 메서드
    # 반드시 하나 이상 존재해야함
    @abstractmethod
    def attack(self, other, kind):
        pass

    @abstractmethod
    def get_damage(self, power, attack_kind):
        pass

    def __str__(self):
        return f'{self.name} : {self.hp}'

# attack, get_damage를 반드시 재정의, 다형성을 강제
# 추가적으로 스킬이 들어감
class Player(Character):
    def __init__(self, name = 'player', hp = 100, power = 10, *a_kinds):
        # 부모 클래스의 생성자 --> name, hp, power
        # 위임
        super().__init__(name, hp, power)
        # 새롭게 추가된 멤버
        # 플레이어 한테는 스킬이 있음
        self.skills = []
        for attack_kind in a_kinds:
            self.skills.append(attack_kind)

    # other = 몬스터
    def attack(self, other, a_kind):
        if a_kind in self.skills:
            # 다른 객체의 상태 정보를 변경할 때
            # message passing
            other.get_damage(self.power, a_kind)

            # 이러한 방식은 객체를 계속 생성하므로
            # 리소스를 많이 잡아먹음
            AttackKindFactory(a_kind).attack()

    # 데미지를 입는다
    def get_damage(self, power, a_kind):
        if a_kind in self.skills:
            self.hp -= (power//2)
        else:
            self.hp -= power


# 추상 클래스(추상클래스인 캐릭터를 상속 받았으므로)
class Monster(Character):
    @classmethod
    def get_monster_kind(cls):
        return cls.__name__.replace('Monster', '')

    def __init__(self, name='Monster', hp=50, power=5):
        super().__init__(name, hp, power)
        self.name = self.get_monster_kind() + name
        self.attack_kind = self.get_monster_kind()

    # other = 플레이어
    def attack(self, other, a_kind):
        if a_kind == self.attack_kind:
            other.get_damage(self.power, a_kind)
            AttackKindFactory(a_kind).attack()

    def get_damage(self, power, a_kind):
        if a_kind == self.attack_kind:
            self.hp += power
        else:
            self.hp -= power

    def get_attack_kind(self):
        return self.attack_kind

    @abstractmethod
    def generate_gold(self):
        pass

# # 게임 개발 초기의 몬스터 종류는 두 가지
# class FireMonster(Monster):
#     def generate_gold(self):
#         return 10

# class IceMonster(Monster):
#     def __init__(self):
#         super().__init__()
#         self.hp = 100

#     def generate_gold(self):
#         return 20

# # 게임 규모가 커지면서 추가된 몬스터 
# class StoneMonster(Monster):
#     def generate_gold(self):
#         return 0

# class KungfuMonster(Monster):
#     def generate_gold(self):
#         return 1000

# class ArrowMonster(Monster):
#     def generate_gold(self):
#         return 500