#Problem : Calculator using class and object 


class calc:
    def __init__(self):
        self.result = 0

    def add(self,value):
        self.result += value

    def sub(self,value):
        self.result -= value

    def mul(self,value):
        self.result *= value

    def div(self,value):
        if value !=0:
            self.result /= value

    def get(self):
        return(self.result)



obj = calc()

obj.add(10)
print(obj.get())
obj.sub(1)
print(obj.get())
obj.mul(2)
print(obj.get())
obj.div(3)
print(obj.get())

