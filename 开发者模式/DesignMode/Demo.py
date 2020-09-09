#Author:bangchui
# encoding:utf-8
_date_ = "Date 13:18"

class Gun():
    name = ""
    price = 0.0

    def getPrice(self):
        return self.price

    def setPrice(self, price):
        self.price = price

    def getName(self):
        return self.name
class AK(Gun):
    def __init__(self):
        self.name = "无敌的AK"
        self.price = 10.0
class Awm(Gun):
    def __init__(self):
        self.name = "人人都想要的awm"
        self.price = 15.0


class gunFactory():
    def creategun(self,name):
        print( " 工厂生产一个实例.")
        if name == "ak":
            ak  = AK()
            return ak
        elif name == "awm":
            awm = Awm()
            return awm
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

class chuizhiDecorator(Decorator):
        def __init__(self, beverage):
            self.beverage = beverage

        def getName(self):
            return self.beverage.getName() + " +垂直"

        def getPrice(self):
            return self.beverage.getPrice() + 0.3

class beijingDecorator(Decorator):
        def __init__(self, beverage):
            self.beverage = beverage

        def getName(self):
            return self.beverage.getName() + " +15倍镜"

        def getPrice(self):
            return self.beverage.getPrice() + 0.5

class CashNorml():
    def accept_money(self,money):
        return money

class CashRate():#会员打折
    def __init__(self,rate):
        self.rate = rate

    def accept_money(self,money):
        return money*self.rate

class Context():#调用策略
    def __init__(self,accpeet):
        self.accpeet = accpeet

    def get_Ruselt(self,money):
        return self.accpeet.accept_money(money)


if __name__ == "__main__":
    gun_factory = gunFactory()
    gunstore = gunStore(gun_factory)
    s = gunstore.oreder(input("本店现有ak,awm\n请问您需要哪个->"))
    print(f"武器类型：{s.getName()},\n武器的价格{s.getPrice()}$")
    fujian = input("本店配件有倍镜和握把\n请问您需要什么（1 or 2）")
    if fujian =="1":
        ice_coke = beijingDecorator(s)
        print("Name:%s" % ice_coke.getName())
        print("Price:%s" % ice_coke.getPrice())
    elif fujian =="2":
        ice_coke = chuizhiDecorator(s)
        print("Name:%s" % ice_coke.getName())
        print("Price:%s" % ice_coke.getPrice())
    else:
        print(f"武器类型：{s.getName()},\n武器的价格{s.getPrice()}$")
    price = ice_coke.getPrice()
    celue = input("您是本店会员吗(y/n)")
    dz = Context(CashRate(0.9))
    yj = Context(CashNorml())
    if celue == "y":
        accpeet = dz
    elif celue == "n":
        accpeet = yj
    p = str(accpeet.get_Ruselt(price))
    print(p[0:4])