# 연산자 오버로딩(operator overloading)
# 다형성의 특별한 케이스

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def coord(self):
        tu = (self.x, self.y)
        return tu

    @coord.setter
    def coord(self, tu):
        self.x = tu[0]
        self.y = tu[1]

    def __str__(self):
        return f'{self.x} , {self.y}'

    # +수행할 이름이 정해진건 아니고 봤을때 딱 +를 한다는 느낌만 있으면 됨
    def __add__(self, num):
        new_x = self.x + num
        new_y = self.y + num
        return Point(new_x, new_y)

    def __radd__(self, num):
        return self + num # p.__add__(num)
    
    def __sub__(self, num):
        new_x = self.x - num
        new_y = self.y - num
        return Point(new_x, new_y)

    def __rsub__(self, num):
        return self - num

    def __mul__(self, num):
        new_x = self.x * num
        new_y = self.y * num
        return Point(new_x, new_y)

    def __rmul__(self, num):
        return self * num
        


if __name__ == "__main__":
    p = Point(10, 20)
   # print(p)
   # print(p.coord)
    p.coord=(5,10)
   # print(p)

    p2 = p + 3
   # print(p) # 5, 10
   # print(p2) # 8, 13

    p3 = 3 + p2
    print(p2)
    print(p3)
    print("*" * 30)
    p4 = p - 10
    print(p4)
    p5 = 10 - p2
    print(p5)
    print("*" * 30)
    p6 = 10 * p
    print(p6)