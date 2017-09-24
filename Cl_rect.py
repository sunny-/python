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


##Create a Student class and initialize it with name and
##roll number. Make methods to :
##1. Display - It should display all informations of
##the student.
##2. setAge - It should assign age to student
##3. setMarks - It should assign marks to the student.

class Student():

    def __init__(self,name,roll_num):
        self.name = name
        self.roll_num = roll_num
        
    def display (self):
        return self.name, self.roll_num

    def age (self,age):
        self.age = age

    def marks(self,marks):
        self.marks = marks
    

mish = Student('mishra',2)

mish


































