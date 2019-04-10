class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def web_surf(self):
        print("surfing")

    def work(self):
        print('working')
    

# 모든 멤버와 메소드를 가짐
class Laptop(Computer):
    # 1. 멤버가 추가될 때
    # method overriding
    def __init__(self, cpu, ram, bettery):
        # 부모 클래스의 생성자 이용
        super().__init__(cpu, ram)
        self.bettery=bettery

    # 2. 메서드가 추가될 때        
    ## 노트북은 가지고 다닐 수 있으니 기능 추가
    def move(self, where_to):
        print('move to {}'.format(where_to))



if __name__ == "__main__":
    com = Computer('i5', 12)
    com.web_surf()

    notebook=Laptop('i5-8265', 16, '19V_4.1am80W')
    notebook.web_surf()
    notebook.move('office')

