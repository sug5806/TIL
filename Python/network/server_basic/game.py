import random as rd

rd.seed(a=None)


for i in range(6):
    lotto = []
    while len(lotto) < 6:
        ran = rd.randint(1, 45)
        if ran not in lotto:
            lotto.append(ran)
    print("{} 회차 : {}".format(i+1, lotto))


