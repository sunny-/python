class Rectangle():

    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        area = self.length*self.breadth
        return area

    def perimeter(self):
        return 2*(self.length+self.breadth)
    



Rect_1 = Rectangle(2,4)
Rect_1.area()
