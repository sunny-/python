

def sq(x,e):
    low = 0
    count = 0
    high = x
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
        print ('low ' + str(low))
        print ('high ' + str(high))
        print ('g ' + str(g))
        print ('   ')


    print ('count ' + str(count))
    return g
