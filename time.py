class Time:

    def __init__(self,hours=0,minutes=0,seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    
    def convertToSeconds(self): 
        minutes = self.hours * 60 + self.minutes 
        seconds = minutes * 60 + self.seconds 
        return seconds 

t = Time(10,12,46)
print (t.convertToSeconds())


#**************************************


class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return ('('+str(self.x)+','+str(self.y)+')')


    def __add__(self,other):
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self,other):
        return Point(self.x-other.x, self.y-other.y)
    
    def __mul__(self, other): 
        return Point(self.x * other.x + self.y * other.y)

    def __rmul__(self, other): 
        return Point(other * self.x,  other * self.y) 
        
        

p1 = Point(1.0, 2.0)
p2 = Point(3.0,4.0)
p3 = p1+p2
print(p3)
p4 = p1-p2
print(p4)
p5 = p1*p2
print(p5)
a=6
p6 = a*p2
print(p6)






#***************************************


class Rectangle:
    
    def __init__(self,h=0,w=0):
        self.h = h
        self.w = w
        
    def __str__(self):
        return ('('+str(self.h)+','+str(self.w)+')')
        

r = Rectangle(100,200)

print(r)


#****************************************







































