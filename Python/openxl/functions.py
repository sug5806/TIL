import openpyxl as op
from functools import reduce
import math

# get_raw_data(filname) -> dict
def get_raw_data(filename):
    """
    get_raw_data(filname) -> dict
    """
    workbook = op.load_workbook(filename)
    ac = workbook.active
    g = ac.rows
    student = dict()
    for name, score in g:
        student[name.value] = score.value
    
    return student

# 래핑함수 같은 기능을 하지만 좀더 보기 편하게 함수 시그니처를 변경함(여기서는 함수이름)
def get_scores(student):
    """
    get_scores(student) -> tuple
    student = {'name1' : score1, 'name2' : score2, ...}
    ret tuple(score)
    """
    return tuple(student.values())



def get_evaluation(avg, std_dev, avg_rag, std_rag=20):
    """
    get_evaluation(avg, std_dev, avg_rag, std_rag=20) -> None
    avg = 우리반 평균
    avg_arg = 학년 평균
    """
    if avg < avg_rag and std_dev > std_rag:
        print('성적이 너무 저조하고 학생들의 실력 차이가 너무 크다.')
    elif avg > avg_rag and std_dev > std_rag:
        print('성적은 평균 이상이지만 학생들의 실력 차이가 크다. 주의 요망!')
    elif avg < avg_rag and std_dev < std_rag:
        print('학생들의 실력 차이는 크지 않지만 성적이 너무 저조하다. 주의 요망!')
    elif avg > avg_rag and std_dev < std_rag:
        print('성적도 평균 이상이고 학생들의 실력 차이도 크지 않다.')





if __name__=="__main__":
    student = get_raw_data('class_1.xlsx')
    avg = get_average(get_scores(student))
    var = get_variance(get_scores(student), avg)
        # = get_variance(student.values())
    std_dev = get_std_dev(var)
            # = get_std_dev()
    avg_range = 50
    std_dev_range = 20
    print("평균:{}, 분산:{}, 표준편차:{}".format(avg, var, std_dev))
    get_evaluation(avg, std_dev, avg_range, std_dev_range)
# = get_evaluation()