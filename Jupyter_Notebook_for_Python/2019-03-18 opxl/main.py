# USER PROGRAMMER
# 만드는 사람을 유저 프로그래머라고 함

import sys
from functions import (get_raw_data, get_average, get_evaluation, 
                        get_scores, get_std_dev, get_variance)
# functions.py 파일의 코드를 다 긁어다가 붙인것

if not len(sys.argv)==3 and not len(sys.argv) == 4:
    print("usage : python main.py <exel filename> <total_avg> <sd=20>")
    exit(-1)

filename = sys.argv[1]
total_avg = float(sys.argv[2])
if len(sys.argv) == 4:
    sd = float(sys.argv[3])

# raw_data = get_raw_data(sys.argv[1])
raw_data = get_raw_data(filename)
scores=get_scores(raw_data)
avg = get_average(scores)
var = get_variance(scores, avg)
std_dev = get_std_dev(var)

print(f"평균 : {avg}, 분산 : {var}, 표준편차 : {std_dev}")

if len(sys.argv) == 4:
    get_evaluation(avg, total_avg, std_dev, sd)
elif len(sys.argv) == 3 :
    get_evaluation(avg, total_avg, std_dev)
