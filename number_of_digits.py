#This program returns number of digits in a positive whole number.
n=20748743387 #input number
c=0 #digits counter
q=1 #quotient
while n>=1:	
	q=n/10
	c=c+1
	n=q

print(c)

