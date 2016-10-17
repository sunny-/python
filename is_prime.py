#checks where a given number is prime or not.
def is_prime(n):
        for i in range (2,int((n+1)/2)):
                if n%i == 0:
                        print ('not a prime number')
                        return False

        print ('its a prime number')
        return True

