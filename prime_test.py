# For a given number x, this program 
# checks whether x is prime or not.
def prime(x):
	i = 2 # loop variable - divisor
	if x < 2 or isinstance (x,float):
	        return False
	        
	elif x==2 or x==3:
	        return True

	else:
	        while i <= (x**0.5):
	                if x%i == 0:
	                        return False
	                        break
	                i=i+1
	                
	        else: 
	                return True	
