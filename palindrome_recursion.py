##Check a given number/word, whether its a palindrome or not
##Use recursion to do the task

def is_palindrome(num): #argument alays takes int.
    n= str(num) #input ('Enter number or word') #input alays takes string.
    if len(n) <= 1:
        
        return True

    elif n[0] == n[-1] and is_palindrome(n[1:-1]):
        
        return True

    return False
                              
            
                
            
