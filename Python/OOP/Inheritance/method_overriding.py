class CarOwnder:
    def __init__(self, name):
        self.name = name
    def concentrate(self):
        print("{} is concentrating!".format(self.name))

class Car():
    def __init__(self, owner_name):
        self.car_owner=CarOwnder(owner_name)

    def drive(self):
        self.car_owner.concentrate()
        print(f'{self.car_owner.name} is driving!')


# 자율주행차는 운전자가 집중할 필요는 없지만 운전기능은 있음
class SelfDrivingCar(Car):
    # 비슷한 기능을 자식에 맞춰서 
    # 메서드를 재정의한다.
    def drive(self):
        print("driving by itself")



if __name__ == "__main__":
    car1 = Car('John')
    car2 = Car('james')
    car3 = SelfDrivingCar('hong')

    cars = []
    cars.extend((car1, car2, car3))

    # 다형성 코드
    for car in cars:
        # 객체에 의존하여 호출을한다
        # 객체에 따라 결과물이 다르다
        car.drive()
