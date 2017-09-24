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



class Distance():

##    def __init__(self,km,miles):
##        self.km = km
##        self.miles = miles

    def miles_to_km(self,miles):
        return miles*1.7

    def km_to_miles(self,km):
        return km*0.621
        
dis_1 = Distance()
