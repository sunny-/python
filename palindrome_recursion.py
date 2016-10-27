##Check a given number/word, whether its a palindrome or not
##Use recursion to do the task

def pal(num): #argument alays takes int.
    n= str(num) #input ('Enter number or word') #input alays takes string.
    if len(n) <= 1:
        
        return True

    elif n[0] == n[-1] and pal(n[1:-1]):
        
        return True

    return False
                              



## 4. A palindromic number reads the same both ways.
##Find the largest palindrome made from the product of two 2-digit numbers
##(Hint- Ans is 9009 = 91 × 99 )


def two_pal():
    for i in range (10,99):
        for j in range(10,99):
            p=i*j
            c= []
            if pal(p) == True:
                c.append(p)
    return max(c)             
                
            
