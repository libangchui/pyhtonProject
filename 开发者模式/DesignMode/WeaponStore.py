
class Weapon(object):
    """武器父类"""
    def aim(self):
        print("开启瞄准镜")

    def shoot(self):
        print("dadadada...")
    def pirce(self):
        pirce = 0.0
class Ak47(Weapon):

    def aim(self):
       super().aim()

    def shoot(self):
        print("Ak47-->哒哒哒哒哒哒...")

    def pirce(self):
        pirce = 10000

# class Ump9(Weapon):
#     def aim(self):
#        super().aim()
#
#     def shoot(self):
#         print("Ump9-->突突突突突突...")
#
# class S686(Weapon):
#     def aim(self):
#         super().aim()
#
#     def shoot(self):
#         print("S686->砰，砰，砰")

class WeaponFactory():
    def new_weapon(self,name):
        if name == "Ak47":
            ak47 = Ak47()
            return ak47
        # elif name == "Ump9":
        #     ump9 = Ump9()
        #     return ump9
        # elif name == "S686":
        #     s686 = S686()
        #     return s686


class WeaponStore():
    def __init__(self,factory):
        self.factory =factory
    def inventory(self):
        """清单"""
        print()
    def order(self,name):
        """订单"""
        new_weapon = self.factory.new_weapon(name)
        return new_weapon

    def ok(self):
        print("购买成功!")

weaponfactory = WeaponFactory()
weaponstore = WeaponStore(weaponfactory)
weapon = weaponstore.order(input("请输入您需要的枪械->"))
weaponstore.ok()
weapon.aim()
weapon.shoot()

