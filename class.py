class Point:
   pass

blank = Point()



blank.x = 3.0
blank.y = 4.0
import copy
p1 = copy.copy(blank)



class Rectangle:
    pass

box = Rectangle()

box.w = 100.0
box.h = 200.0

box.corner = Point()

box.corner.x = 0.0
box.corner.y = 0.0


def center_box(box):
    center = Point()
    center.x = box.corner.x + (box.w/2)
    center.y = box.corner.y - (box.h/2)
    ans = '('+ str(center.x) +','+ str(center.y)+')'
    return ans
    
    



































    


