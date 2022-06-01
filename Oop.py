class student():

    def __init__(self, name, course, fees):
        self.a = name
        self.b = course
        self.s = fees

    def PrintInfo(self):
        print(self.a, "has enrolled for the course of", self.b)

    def FeesInfo(self, paid):
        bal = self.s - paid
        print('The balance fees is INR ', bal)

class citizen():

    def __init__(self, aadhar):
        self.i = aadhar

    def CitizenInfo(self):
        print(self.i, 'is a verfied AADHAR number')


class scholar(student, citizen):

    def __init__(self, name, course, fees, aadhar):
        self.a = name
        self.b = course
        self.s = fees
        self.i = aadhar

obj1 =student("rajesh","python",10000)
obj1.FeesInfo(5000)
obj2 = scholar("vas","c",10000, 2345678)
obj2.PrintInfo()
obj2.FeesInfo(2000)