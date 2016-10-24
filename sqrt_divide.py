
##calculate a squareroot of given number x, with and error within e.

def sq(x,e):
    low = 0
    count = 0
    high = max(x,1.0)
    g = (high + low)/2.0

    assert x >= 0 
    assert e > 0 
    while (g**2-x) > e or count <= 100:
        if g**2 > x:
            high = g
            
        else:
            low = g

        count += 1
        g = (high + low)/2.0
        
    return g

# takes test cases for the program above
def test():
    print (sq(2,0.0001))
    print (sq(0.5,0.000001))
    print (sq(100,0.0001))


## calculate a squareroot of given number x, with and error within e.
## use newton ralphs methos to calculate it .



def sq_newton(x,e):
    
    count = 0
    
    g = x/2.0
    diff = (g**2-x)
    assert x >= 0 
    assert e > 0 
    while abs(diff) > e or count <= 100:
        
        g = g - diff/(2*g)
        diff = (g**2-x)
        count += 1

        
    return g








