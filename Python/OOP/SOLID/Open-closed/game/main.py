from attack_kind import AttackKindFactory
from Character import Player
from monsters import FireMonster, IceMonster, StoneMonster, KungfuMonster, ArrowMonster


if __name__ == "__main__":
    fm = FireMonster()
    im = IceMonster()
    sm = StoneMonster()
    kfm = KungfuMonster()
    ar = ArrowMonster()

    monsters = []
    monsters.extend((fm, im, sm, kfm, ar))

    player = Player('john', 120, 20, 'Fire', 'Ice')

    print(player)

    for mon in monsters:
        player.attack(mon, 'Fire')

    for mon in monsters:
        print(mon)
    print("*" * 30)
    print("Monster Turn")
    print()
    for mon in monsters:
        print(mon.get_attack_kind() + "_Monster Attack")
        mon.attack(player, mon.get_attack_kind())
        print()

    print(player)


# 게임 루프 -> 게임속에서는 while문으로 돔
# while 1:
