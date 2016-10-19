# find a factorial of given number n using recursion

def fac(n):
    if n < 0:
        print ('enter positive number')
        return None
    if n == 0 or n == 1:
        return 1
    else:
        return n * fac(n-1)
    
