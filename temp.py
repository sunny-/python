# If a five-digit number is input through the keyboard, write a
# program to calculate the sum of its digits.
x= 11111
i=10000
total=0
while i>=1:
	q=x//i
	r=x%i
	total= total + q
	x=r
	i=i/10
print (total)




