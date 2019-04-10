import openpyxl as op
from functools import reduce
import math

workbook = op.load_workbook('class_1.xlsx')
ws = workbook.active
g = ws.rows

student = dict()

for name_cell, score_cell in g:
    student[name_cell.value] = score_cell.value

# avarage : 학생 평균
scores = tuple(student.values())
avrg = reduce(lambda a, b : a + b, scores) / len(scores)

# variance : 학생 점수 분산
variance = reduce(lambda res, x : (x-avrg)**2 + res, scores, 0) / len(scores)

# std_div : 표준편차
std_dev = math.sqrt(variance)


print("평균:{}, 분산:{}, 표준편차:{}".format(avrg, variance, std_dev))



if avrg < 50 and std_dev > 20:
    print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
elif avrg > 50 and std_dev > 20:
    print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
elif avrg < 50 and std_dev < 20:
    print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
elif avrg > 50 and std_dev < 20:
    print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')