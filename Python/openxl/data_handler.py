from statistics import Stat
import openpyxl as op

# dataHandler가 계산을 담당하지는 않으므로 composition으로 하는게 좋음
class DataHandler:
    # composition
    calculator = Stat()

    @classmethod
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

    def __init__(self):
        # 아직 인스턴스가 만들어지지 않았는데 생성자가 인스턴스 메소드를 호출하는게 논리적으로 맞지 않으므로 수정함
        # 물론 self.으로해도 잘 작동함
        self.year_class = filename.split('_')[1]
        self.raw_data = DataHandler.get_raw_data(filename)
        self.scores =list(self.raw_data.values())
        self.cache={}

    def get_average(self):
        self.calculator.get_average()
        return avg

    def get_std_dev(self):
        pass
