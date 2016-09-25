# This program gives nth prime number.
# For example here n=1000
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

pc = 1
y = 3
while pc < 1000:
	if prime(y) == True:
		pc = pc + 1

	y = y + 1

if pc == 1000:
	print (y-1)	

