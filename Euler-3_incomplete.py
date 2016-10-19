#checks where a given number is prime or not.
def is_prime(n):
        for i in range (2,int((n+1)/2)):
                if n%i == 0:
                        #print ('not a prime number')
                        return False

        #print ('its a prime number')
        return True

    

#(Euler -3) The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143?

def l_prime(n):
    if n<=0:
        print('Give positive number')

    elif is_prime(n) == True:
        return n
    
    for i in range (1,n):
        if n%i == 0 and is_prime(i) == True:
            p = i
    return p






