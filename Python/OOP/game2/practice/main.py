from attack_kind import AttackKindFactory, FireAttackKind, IceAttackKind
from Character import Player#, Monster, FireMonster, IceMonster, StoneMonster, KungfuMonster
from monsters import MonstersFactory


if __name__=="__main__":
    # fm=FireMonster()
    # im=IceMonster()
    # sm=StoneMonster()
    # kfm=KungfuMonster()
    fm = MonstersFactory("Fire")
    im = MonstersFactory("Ice")
    sm = MonstersFactory("Stone")
    kfm = MonstersFactory("Kungfu")

    monsters=[]
    monsters.extend((fm, im, sm, kfm))

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