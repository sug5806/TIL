# 실제로 게임이 진행되는 게임 월드
from character import Player
from attack_kind import FireAttackKind, IceAttackKind
from monsters import (FireMonster, IceMonster, StoneMonster, 
                        KungfuMonster)

fm=FireMonster()
im=IceMonster()
sm=StoneMonster()
kfm=KungfuMonster()

monsters=[]
monsters.extend((fm, im, sm, kfm))

# Dependency Injection : DI
player = Player('john', 120, 20, FireAttackKind(), IceAttackKind())


print(player)

for mon in monsters:
    player.attack(mon, 'Fire')

for mon in monsters:
    print(mon)

    print()
    print("Monster Attack!")
for mon in monsters:
    print(mon.get_attack_kind())
    mon.attack(player, mon.get_attack_kind())
    print()

print(player)