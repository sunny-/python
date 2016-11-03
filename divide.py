#Find the smallest number that can be divided by
# each of the numbers from 1 to 10 without any remainder.


def divide(s,e): #s is the starting number and e is the ending number.
    '''s is the starting number and e is the ending number'''
    n = 10
    ans = False
    
    while ans == False: #this loops runs till answer is found
        c=0
        for i in range (s,e):
            if n % i == 0:
                c = c+1 #counter counts,whether the number is divided by all number in range
                if c == (e-s):
                    print (n)
                    ans = True
        n = n+10






#Find the smallest number that can be divided by
# each of the numbers from 1 to 20 without any remainder.


def divide_n():
    import time
    start_time = time.time()
    n = 20
    ans = False
    
    while ans == False:
        c=0
        for i in range (11,21):
            if n % i == 0:
                c = c+1
                if c == 10:
                    print ("Program Execution Time (in seconds) is : " + str(time.time()-start_time))
                    return n
                    ans = True
        n = n+20
                  


