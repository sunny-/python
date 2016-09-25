# For a given number x, this program 
# prints factors for that number using while loop
x= 0.1 # input number factor to be found
i= 1 # iteration counter
if x>=1:
	while i <= x:
		if x%i==0:
			print (i)
		i=i+1
else:
	print('invalid number') # factors can only be of positive number
