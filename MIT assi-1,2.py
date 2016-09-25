# 
import math
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

sum = 0
n = 9
for i in range(2,n+1):
	if prime(i):
		sum = sum + math.log(i)

print (n)
print (sum/n)



