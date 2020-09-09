#药房业务系统
#构造药品类和工作人员类
class Medicine:
    name=""
    price=0.0
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price
    def accept(self,visitor):
        pass
#抗生素
class Antibiotic(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
#感冒药
class Coldrex(Medicine):
    def accept(self,visitor):
        visitor.visit(self)
class Visitor:
    name=""
    def setName(self,name):
        self.name=name
    def visit(self,medicine):
        pass
class Charger(Visitor):#划价员
    def visit(self,medicine):
        print ("CHARGE: %s lists the Medicine %s. Price:%s " % (self.name,medicine.getName(),medicine.getPrice()))
class Pharmacy(Visitor):#药房管理员
    def visit(self,medicine):
        print ("PHARMACY:%s offers the Medicine %s. Price:%s" % (self.name,medicine.getName(),medicine.getPrice()))

class ObjectStructure:
    pass
#构建处方
class Prescription(ObjectStructure):
    medicines=[]
    def addMedicine(self,medicine):
        self.medicines.append(medicine)
    def rmvMedicine(self,medicine):
        self.medicines.append(medicine)
    def visit(self,visitor):
        for medc in self.medicines:
            medc.accept(visitor)

if __name__=="__main__":
    yinqiao_pill=Coldrex("Yinqiao Pill",2.0)
    penicillin=Antibiotic("Penicillin",3.0)
    doctor_prsrp=Prescription()
    doctor_prsrp.addMedicine(yinqiao_pill)
    doctor_prsrp.addMedicine(penicillin)
charger=Charger()
charger.setName("Doctor Strange")
pharmacy=Pharmacy()
pharmacy.setName("Doctor Wei")
doctor_prsrp.visit(charger)
doctor_prsrp.visit(pharmacy)

