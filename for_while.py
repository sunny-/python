# For a given number x, this program 
# prints factors for that number using for loop
x= 10000 # input number factor to be found
if x>=1:
	for i in range(1,x+1):
		if x%i==0:
			print (i)
		i=i+1
else:
	print('invalid number') # factors can only be of positive number..
	
