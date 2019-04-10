# (계속 변화하는)공격 종류를 추상화한다.
# 다형성을 이용 
# OPEN FOR EXTENSION
# 공격 종류를 확장한다.

# 시스템이 확장할 때 (Extension)
# '변화하는 부분' --> 추상클래스를 통해 추상화 하고
# 확장되는 부분을 상속을 통해 클래스 확장을한다. 
# 디자인 패턴중 abstract factory가 쓰임

from abc import ABCMeta, abstractmethod

# 상황에 알맞는 객체를 반환해준다
# 객체 생성을 위임받음
def AttackKindFactory(kind):
    if kind == 'Fire':
        return FireAttackKind()
    elif kind == 'Ice':
        return IceAttackKind()
    elif kind == 'Stone':
        return StoneAttackKind()
    elif kind == 'Kungfu':
        return KungfuAttackKind()
    elif kind == 'Arrow':
        return ArrowAttackKind()


# 추상클래스
class AttackKind(metaclass=ABCMeta):

    # 자식 클래스가 여기로 들어가서 속성?만 뽑아냄
    @classmethod
    def __get_attack_kind(cls):
        return cls.__name__.replace('AttackKind', '')

    def __init__(self):
        self.kind = self.__get_attack_kind()

    def get_kind(self):
        return self.kind

    @abstractmethod
    def attack(self):
        pass

# 게임 개발 초기에 확정된 두 개의 공격 종류

class FireAttackKind(AttackKind):
    def attack(self):
        print(f"under the attack of {self.get_kind()}")

class IceAttackKind(AttackKind):
    def attack(self):
        print(f'under the attack of {self.get_kind()}')

# 추후 게임 규모가 커지면서 두 개의 공격 종류가 확장(EXTENSION)

class StoneAttackKind(AttackKind):
    def attack(self):
        print('Aimming at the player!')

class KungfuAttackKind(AttackKind):
    def attack(self):
        print('Kungfu!!')

class ArrowAttackKind(AttackKind):
    def attack(self):
        print('Arrow!!')

if __name__=="__main__":
    fa=FireAttackKind()
    fa.attack()
    ia=IceAttackKind()
    ia.attack()

    # 추상클래스라 객체생성 X
    #ak=AttackKind()