# 定义基础枪类
class Gun():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name
# 定义ak类继承基础类
class AK(Gun):
    def __init__(self):
        self.name = "无敌的AK"
        self.price = 10.0
# 定义awm类继承基础类
class Awm(Gun):
    def __init__(self):
        self.name = "人人都想要的awm"
        self.price = 15.0
# 定义造枪的工厂类
class gunFactory():
    def creategun(self,name):
        if name == "ak":
            ak  = AK()
            return ak
        elif name == "awm":
            awm = Awm()
            return awm

# 定义卖枪的商店类
class gunStore():
    def __init__(self,factory):
        self.factory =factory

    def oreder(self,name):
        creategun = self.factory.creategun(name)
        return creategun
# 装饰器
class Decorator():
        def getName(self):
            pass

        def getPrice(self):
            pass
# 定义垂直握把装饰类
class VerticalwrapDecorator(Decorator):
    def __init__(self, beverage):
        self.beverage = beverage

    def getName(self):
        return self.beverage.getName() + " +垂直"

    def getPrice(self):
        return self.beverage.getPrice() + 0.3
# 定义倍镜装饰类
class TimesmirrorDecorator(Decorator):
        def __init__(self, beverage):
            self.beverage = beverage

        def getName(self):
            return self.beverage.getName() + " +15倍镜"

        def getPrice(self):
            return self.beverage.getPrice() + 0.5
#原价
class CashNorml():
    def accept_money(self,money):
        return money
# 会员价
class CashRate():
    def __init__(self,rate):
        self.rate = rate

    def accept_money(self,money):
        return money*self.rate
#调用策略
class Context():
    def __init__(self,accpeet):
        self.accpeet = accpeet

    def get_Ruselt(self,money):
        return self.accpeet.accept_money(money)

class main():
    try:
        gun_factory = gunFactory()
        gunstore = gunStore(gun_factory)
        s = gunstore.oreder(input("本店现有ak,awm\n请问您需要哪个->"))
        print(f"武器类型：{s.getName()},\n武器的价格{s.getPrice()}$")

        accessories = input("本店配件有倍镜和握把\n请问您需要什么（1 or 2）")
        if accessories == "1":
            ice = TimesmirrorDecorator(s)
            print("Name:%s" % ice.getName())
            print("Price:%s" % ice.getPrice())
        elif accessories == "2":
            ice2 = VerticalwrapDecorator(s)
            print("Name:%s" % ice2.getName())
            print("Price:%s" % ice2.getPrice())
        # else:
        #     print(f"武器类型：{s.getName()},\n武器的价格{s.getPrice()}$")
        price = ice.getPrice()
        celue = input("您是本店会员吗(y/n)")
        dz = Context(CashRate(0.9))
        yj = Context(CashNorml())
        if celue == "y":
            accpeet = dz
        elif celue == "n":
            accpeet = yj
        p = str(accpeet.get_Ruselt(price))
        print(p[0:4])
    except Exception:
        print("操作错误")

if __name__ == "__main__":
    main()




