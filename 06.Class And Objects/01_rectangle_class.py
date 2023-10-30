#Problem : Create a Rectangle class with methods to calculate its area and perimeter. Initialize it with length and width attributes.

class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width 
    
    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

rect1 = Rectangle(4,3)

print("Area:", rect1.area())
print("Perimeter:", rect1.perimeter())