class Gun:
    def __init__(self, kind):
        self.kind=kind

    def bangbang(self):
        print(f'{self.kind} bangbang!!!!!')

class Police:
    def __init__(self, name):
        self.name = name
        self.gun = None

    # gun 객체를 받음
    def acquire_gun(self, gun):
        self.gun = gun


    def release_gun(self):
        gun = self.gun
        self.gun = None
        return gun

    def shoot(self):
        if not self.gun:
            print("You don't have a gun")
        else:
            # 내가 가지고 있지는 않지만 가지고 있는 객체를 통해 기능을 구현함
            # 
            self.gun.bangbang()


if __name__ == "__main__":
    pol = Police('john')
    gun = Gun('glock')

    pol.shoot()

    # police 객체가 gun 객체를 얻은 시점
    pol.acquire_gun(gun)
    # pol.gun과 gun이 둘다 가리키므로 gun을 None으로 하여 pol.gun에게 소유권이 넘어감
    gun = None
    pol.shoot()

    # 다시 반납하면서 소유권 이전
    gun = pol.release_gun()
    pol.shoot()

    del pol