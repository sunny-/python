# this program returns sum of all numbers staring
# from number n to 1 using recursion
def add(n):
    if n < 0:
        print('Enter positive number')
        return None
    if n == 0 :
        return 0
    else:
        return n + dd(n-1)


    
# checks for given number for palindrome
def palindrome(n):
    c= str(n)
    if len(c) == 1:
        print ('Palindrome')
        return True
    elif c[0] == c[-1] and palindrome(c[1:-1]) :
        print ('Palindrome')
        return True
    else:
        print ('Not a palindrome')
        return False




# returns adition of numbers in the list
c = [12,13,3,4]
def addition(c):
    if len(c) == 0:
        return None
    if len(c) == 1:
        return c[0]
    else:
        return c[0] +  addition(c[1:])




# give a maximum number in a list
def maximum(c):
    if len(c) == 1:
        return c[0]
    else:
        if c[0]> maximum(c[1:]):
            return c[0]

        else:
            return maximum(c[1:])
    
    











        
