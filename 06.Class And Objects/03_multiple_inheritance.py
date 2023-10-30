#Example for : Multiple inheristance 

class class1:
    def __init__(self):
        print("class1 - init ")
    
    def class1_msg(self):
        print("I am class1 msg function")

class class2:
    def __init__(self):
        print("class2 - init ")
    
    def class2_msg(self):
        print("I am class2 msg function")

class class3(class1,class2):
    def __init__(self):
        print("class3 - init ")
    
obj = class3()
print("Access class1 functions from class3 using multiple inheristance")
obj.class1_msg()
print("Access class2 functions from class3 using multiple inheristance")

obj.class2_msg()