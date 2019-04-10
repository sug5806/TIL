# utility class (관련 기능만 모아놓은 클래스, 멤버가 없음)

# Single responsibility principle
# 통계에 대한 하나의 책임만 진다

import math
from functools import reduce

class Stat:
    def get_average(self, scores):
        """
        get_average(scores) -> float<2>
        """
        avg = reduce(lambda sum ,x : sum + x, scores) / len(scores)
        return round(avg,2)

    def get_variance(self, scores, avg):
        """
        get_variance(scores, avg) -> float<2>
        """
        var = reduce(lambda res, x : (x-avg)**2+res, scores, 0) / len(scores)
        return round(var,2)

    def get_std_dev(self, var):
        """
        get_std_dev(var) -> float<2>
        var : 분산
        ret : 표준편차(소수점 2자리)
        """
        return round(math.sqrt(var),2)



class Reader:
    pass

class Writer:
    pass

# 파일시스템은 read와 write의 버퍼가 따로있으므로 coposition으로 작성해야함
class FileSystem:
    def __init__(self):
        self.reader = Reader()
        self.writer = Writer()